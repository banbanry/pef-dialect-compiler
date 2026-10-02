#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PEF Phi-Compiler (pef-dialect-compiler) — 哲学方言编译器
骨架继承自 mmc-compiler (同源 π 表 / 三段 schema / 审计链), 按哲学域做适应性调整:
  - 输入不是模型输出 JSON, 是哲学/宗教/工程/AI 架构的原文文本或概念
  - 核心从"格式归一"变为"结构映射 + 锚检测": 每句拆 P/ΔV/J 三槽, 标锚, 算残留率 ρ'
  - ρ' = 装不进 P+ΔV→J 的句子占比 + 无锚断言占比 —— "边界"的数值化

命令:
  python pef_compile.py compile --input <文本文件> [--source-dialect auto|daojia|buddhism|quantum|ai_arch] [--seq N] [--out out.json]
  python pef_compile.py dialects            # 列方言注册表
零第三方依赖 (stdlib only)
"""
import argparse, hashlib, json, os, re, sys, time

# ---- π 预置表 (与 mmc-compiler 同源, 前 120 位; 编译坐标不可自算, 只可查表) ----
PI_DIGITS = ("314159265358979323846264338327950288419716939937510582097494"
             "459230781640628620899862803482534211706798214808651328230664")

# ---- 哲学方言注册表: 各传统/领域的方言特征 (断言模式/术语信号) ----
DIALECTS = {
    "daojia": {
        "name": "道家",
        "signals": ["道可道", "非常道", "无为", "反者", "上善若水", "无名", "玄", "朴",
                    "不争", "柔", "阴阳", "德", "自然", "天下", "圣人", "周行"],
        "note": "道家/道德经: 悖论式自否、借喻（水/朴/婴儿）、无主语断言",
    },
    "buddhism": {
        "name": "佛学/禅",
        "signals": ["不可说", "空", "缘起", "我执", "无自性", "色即是空", "般若", "涅槃",
                    "五蕴", "无我", "诸法", "心经", "金刚经", "菩萨", "烦恼", "菩提", "法身"],
        "note": "佛学/禅: 否定式断言、无主语、四句否定（非有非无）",
    },
    "quantum": {
        "name": "量子力学",
        "signals": ["叠加", "坍缩", "测量", "贝尔", "纠缠", "薛定谔", "波函数", "概率幅",
                    "量子", "退相干", "不预设", "Tsirelson", "CHSH", "态", "本征"],
        "note": "量子力学: 数学式断言、实验锚引用、概率语言",
    },
    "ai_arch": {
        "name": "AI 架构",
        "signals": ["RLHF", "幻觉", "对齐", "涌现", "思维链", "模型", "训练", "推理",
                    "token", "prompt", "参数", "偏好", "标注", "智能体", "认知", "AI"],
        "note": "AI 架构: 术语黑话、工程断言、系统行为描述",
    },
}

# ---- 术语归一 (异名同义; 哲学域扩展版) ----
TERM_MAP = {
    "道": "dao", "常道": "dao_const", "德": "de",
    "空": "sunya", "无自性": "no_self_nature", "缘起": "pratityasamutpada",
    "我执": "self_grasping", "无我": "anatman",
    "叠加态": "superposition", "坍缩": "collapse", "测量": "measurement",
    "波函数": "wavefunction", "纠缠": "entanglement",
    "幻觉": "hallucination", "对齐": "alignment", "涌现": "emergence",
    "思维链": "chain_of_thought",
    "主体": "subject", "变量": "variable", "结果": "result",
    "推理": "reasoning", "思考": "reasoning",
}

# ---- 承诺语气 (语义方言; 与 mmc 同规则) ----
HEDGE = r"可能|也许|或许|大概|据说|估计|possibly|maybe|perhaps|类比|好比|如同|像"
STRONG = r"一定|必须|绝对|必然|definitely|certainly|must|唯一"

# ---- 锚信号 ----
# 硬锚: 可独立复现 (年份/人名+年份/公式/实验/教科书常数)
HARD_ANCHOR = [
    r"(18|19|20)\d{2}",                          # 年份
    r"贝尔|CHSH|Tsirelson|GHZ|Lindemann|Lambert|Landauer|Bennett|Schaeffer|Wei\b",
    r"2√2|2\\sqrt\{2\}|kT·ln2|0\.828|3\.74×10|11\.5σ",
    r"π|超越数|无理数|不可计算",
    r"实验|定理|证明|档案|教科书",
    r"FActScore|InstructGPT",
]
# 软锚: 只在说话者心里, 不可独立复现
SOFT_ANCHOR = r"直觉|体验|感觉|权威|我相信|我悟|顿悟|据说|玄学|高维|能量场|感应"
# 押金类比: 有可操作后果的类比 (多角度可累积可收敛 / 可检验)
PLEDGE = r"押金|可检验|可复现|多角度|可累积|可收敛|层析|收敛"

# ---- 结构映射词 (P/ΔV/J 三槽) ----
P_WORDS = ["测量者", "计算者", "说者", "主体", "我", "佛", "圣人", "心", "观察者", "接收", "AI", "模型", "编译器"]
DV_WORDS = ["变量", "势能差", "缘", "过手", "传递", "接收", "输入", "测量", "投影", "内容", "相", "波函数", "偏好", "标注"]
J_WORDS = ["结果", "落地", "果", "输出", "现象", "读数", "色", "J", "断言", "结论", "数字", "下一位"]

def _sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def detect_dialect(text, source_dialect):
    """方言识别: 指定或 auto 按信号命中数"""
    if source_dialect != "auto":
        return source_dialect, [s for s in DIALECTS[source_dialect]["signals"] if s in text][:5]
    best, best_hits = "daojia", []
    for name, d in DIALECTS.items():
        hits = [s for s in d["signals"] if s in text]
        if len(hits) > len(best_hits):
            best, best_hits = name, hits
    return best, best_hits[:5]

def split_sentences(text):
    """句切分: 现代标点 + 古汉语无标点断句 (以语气词/结构词为界)"""
    parts = re.split(r"(?<=[。！？!?；;])\s*|\n+", text)
    out = []
    for p in parts:
        p = p.strip()
        if len(p) < 3:
            continue
        # 古汉语: 无标点长句按 之乎者也矣焉哉/， 断
        if not re.search(r"[。！？!?；;，,]", p) and len(p) > 18:
            sub = re.split(r"(?<=[之乎者也矣焉哉])", p)
            out.extend(s.strip() for s in sub if len(s.strip()) >= 3)
        else:
            out.append(p)
    return out

def classify_level(s):
    """承诺等级 → 证据档: FACT(可复现) / JUDGMENT(框架内断言) / GREY(待定类比)"""
    if re.search(STRONG, s):
        return "JUDGMENT"
    if re.search(HEDGE, s):
        return "GREY"
    return "FACT"

def classify_anchor(s):
    """锚类型: hard(可独立复现) / pledged(押金类比) / soft(仅说话者心里) / none"""
    if re.search("|".join(HARD_ANCHOR), s):
        return "hard"
    if re.search(PLEDGE, s):
        return "pledged"
    if re.search(SOFT_ANCHOR, s):
        return "soft"
    return "none"

def map_structure(s):
    """结构映射(半自动): 词表给出候选槽. 装不满 = UNMAPPED, 需人工编译.
    定位: 脚本不假装全自动——三槽拆解是语义判断, 自动词表只给候选, 人/LLM 复核."""
    p = [w for w in P_WORDS if w in s]
    dv = [w for w in DV_WORDS if w in s]
    j = [w for w in J_WORDS if w in s]
    # 无时间戳主体的标记: 出现"我/心/佛"等主体词但没有测量/计算/接收动作词 → P?
    has_action = any(w in s for w in ["测量", "计算", "说", "看", "传", "接收", "写", "验证"])
    p_flag = " (P?)" if (p and not has_action) else ""
    mapped = {}
    if p:
        mapped["P"] = p[0] + p_flag
    if dv:
        mapped["ΔV"] = dv[0]
    if j:
        mapped["J"] = j[0]
    # 装不满三槽 → UNMAPPED(需人工编译), 不是"装不进结构"
    complete = len(mapped) >= 2
    if not complete:
        mapped = "UNMAPPED(需人工编译)"
    return mapped, complete

def compile_text(text, source_dialect, seq):
    """编译主流程: 方言识别 → 句切分 → 分级 → 结构映射 → 锚检测 → π锚 → ρ'"""
    matched, hits = detect_dialect(text, source_dialect)
    sentences = split_sentences(text)
    pos = seq % len(PI_DIGITS)
    pi_anchor = f"π-{pos}-{PI_DIGITS[pos]}"

    claims, unanchored, unmapped = [], [], []
    used_terms = {}
    for s in sentences:
        level = classify_level(s)
        anchor = classify_anchor(s)
        structure, complete = map_structure(s)
        claims.append({
            "text": s[:120],
            "assertion_level": level,
            "anchor": anchor,
            "structure": structure,
            "origin_offset": text.index(s),
        })
        if anchor in ("none", "soft"):
            unanchored.append(s[:60])
        if not complete:
            unmapped.append(s[:60])
        for zh, en in TERM_MAP.items():
            if zh in s and en not in used_terms:
                used_terms[en] = zh

    # 残留率 ρ': 主指标 = 无锚断言占比 (锚检测正则可靠, 自动化可信)
    # 辅助指标 = 装不满三槽占比 (结构映射是半自动候选, 需人工复核)
    rho_anchor = round(len(unanchored) / max(1, len(claims)), 4)
    rho_struct = round(len(unmapped) / max(1, len(claims)), 4)
    compiled = {
        "schema": "pef-phi-1.0",
        "source_dialect": matched,
        "pi_anchor": pi_anchor,
        "seq": seq,
        "claims": claims[:40],
        "terms_normalized": used_terms,
    }
    audit = {
        "rho_residual": rho_anchor,
        "rho_unanchored": rho_anchor,
        "rho_unmapped_auto": rho_struct,
        "note": "rho_unanchored 为主指标(锚检测自动可信); rho_unmapped_auto 为半自动候选, 需人工复核",
        "unanchored": unanchored[:10],
        "unmapped_auto": unmapped[:10],
        "hash": _sha(json.dumps(compiled, sort_keys=True, ensure_ascii=False)),
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    return {
        "compiled": compiled,
        "dialect": {"matched": matched, "signals_hit": hits, "registered": list(DIALECTS)},
        "audit": audit,
    }

def cmd_compile(a):
    if not os.path.exists(a.input):
        sys.exit(f"✗ 输入不存在: {a.input}")
    try:
        text = open(a.input, encoding="utf-8").read()
    except OSError as e:
        sys.exit(f"✗ 读取失败: {e}")
    seq = a.seq if a.seq is not None else int(time.time()) % 1000
    out = compile_text(text, a.source_dialect, seq)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
        json.dump(out, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"\n已存: {a.out}")
    return 0

def cmd_dialects(a):
    print(f"{'方言':<12}{'领域':<10}{'信号数':<6}{'说明'}")
    print("-" * 80)
    for name, d in DIALECTS.items():
        print(f"{name:<12}{d['name']:<10}{len(d['signals']):<6}{d['note']}")
    return 0

def main():
    ap = argparse.ArgumentParser(description="PEF 哲学方言编译器 (pef-phi)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("compile", help="编译哲学文本到 PEF 标准 schema")
    p.add_argument("--input", required=True, help="方言文本文件 (UTF-8)")
    p.add_argument("--source-dialect", default="auto", choices=list(DIALECTS) + ["auto"],
                   help="来源方言 (默认 auto 按信号识别)")
    p.add_argument("--seq", type=int, default=None, help="π 锚序号 (默认按时间)")
    p.add_argument("--out", default=None, help="输出 JSON 路径")
    sub.add_parser("dialects", help="列方言注册表")
    a = ap.parse_args()
    rc = {"compile": cmd_compile, "dialects": cmd_dialects}[a.cmd](a)
    sys.exit(rc or 0)

if __name__ == "__main__":
    main()
