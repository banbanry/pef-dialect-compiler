# dsh-tool-pef-phi-compiler

把哲学/宗教/工程/AI 架构方言文本编译到 **PEF 公共语法**（P + ΔV → J + 三条错误处理规则）的 DSH 工具插件。

对齐 `dsh-pef-plugins` 仓库的插件封装格式（范本：`dsh-tool-mmc-compiler`）。**原仓库不改动**，本插件作为 pef-dialect-compiler 的独立子目录维护。

## 安装

```bash
# 1. 把插件目录复制/链接到 DeepSeek Harness 插件目录
#    （或直接本地引用）
# 2. 设置脚本路径环境变量（可选，默认 ./scripts/pef_compile.py 相对于插件根）
export PEF_PHI_PATH="/path/to/pef-dialect-compiler/scripts/pef_compile.py"
```

## 用法

注册后暴露工具 `pef_phi_compile`：

| 参数 | 必填 | 说明 |
|---|---|---|
| `input` | 是 | 待编译的方言文本文件路径（UTF-8） |
| `dialect` | 是 | `auto`（按信号识别）\| `daojia` \| `buddhism` \| `quantum` \| `ai_arch` |
| `seq` | 否 | π 锚序号（固定后可复现同一编译结果） |

```json
{
  "input": "examples/daojia.txt",
  "dialect": "daojia",
  "seq": "7"
}
```

输出为三段 JSON（`schema: pef-phi-1.0`）：
- `compiled`：方言识别、π 锚、逐句 claims（文本/承诺级/锚/结构映射/角色/建议）、术语归一
- `dialect`：命中方言与信号
- `audit`：残留率 ρ'（主指标=无锚占比）、结构未映射率、哈希、时间戳

## 输出解读（诚实边界）

| 字段 | 含义 |
|---|---|
| `rho_unanchored` | **主指标** = 无锚断言占比，即「边界厚度」。ρ' 高=不可说多；ρ' 低=已说尽。 |
| `rho_unmapped_auto` | 结构映射未满占比。**半自动**：三槽拆解是语义判断，脚本只给候选，`UNMAPPED(需人工编译)` 由人/LLM 终审。 |
| `roles` / `hints` | 句式模式命中（BOUNDARY / J≠源 / J / ΔV / P→J / ANCHOR）与人工编译建议。 |
| `anchor` | `hard`（可独立复现）/ `pledged`（押金类比）/ `soft`（仅文本，不进结构）/ `none` |

## 与 mmc-compiler 的关系

- **继承**：π 表同源、三段 schema、审计链、承诺分级。
- **改造**：方言注册表（模型厂商 → 哲学传统）、锚检测（硬锚/押金/软锚）、结构映射（语义级句式模式）、ρ' 主指标。
- **不依赖**：不调用任何模型 API，纯本地 stdlib（pef_compile.py 仅用 Python 标准库）。

## 验证

```bash
python scripts/pef_compile.py compile --input examples/daojia.txt --source-dialect daojia --seq 7
python scripts/pef_compile.py compile --input examples/quantum.txt --source-dialect quantum --seq 8
```

预期：道家 ρ'=1.0（悖论式断言多，边界厚）、量子 ρ'=0.25（贝尔/Lindemann 硬锚，边界薄）。
