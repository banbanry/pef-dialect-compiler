/**
 * dsh-tool-pef-phi-compiler — 哲学方言编译器
 *
 * © 2026 沈鹭 banbanry · 厦门恒元架构科技有限公司 · PEF 架构
 * https://github.com/banbanry/pef-architecture
 * 来源代码：https://github.com/banbanry/pef-dialect-compiler
 *
 * 基于 pef_compile.py 的 DSH 工具封装：把哲学/宗教/工程/AI 架构方言文本编译到
 * PEF 公共语法（P + ΔV → J），自动锚检测（硬锚/押金/软锚）+ 语义级结构映射
 * （句式模式 + 编译建议）+ 残留率 ρ'（边界厚度量化）。
 *
 * 理论依据：PEF 三元原语（P 主体 / ΔV 变量 / J 结果）+ 三条错误处理规则
 * （不可自证、必须外部锚定、允许局部失败且留审计链）。
 * 注意：本插件只做方言编译，不调用任何模型 API，不裁决哲学体系正确性；
 * 结构映射为半自动候选（UNMAPPED 需人工复核），脚本不假装全自动。
 *
 * 注：本文件对齐 dsh-pef-plugins 仓库的插件封装格式（dsh-tool-mmc-compiler 为范本），
 * 仅参考其格式，不改动原仓库。
 */

import type { Context } from '@deepseek-ai/cordis'
import { defineTool } from '@deepseek-ai/dsh-tools'
import { execFile } from 'node:child_process'
import { promisify } from 'node:util'

/** P1 加固：CLI 参数注入防护（路径白名单 + 非法字符拒绝） */
import path from 'node:path'
const ALLOW_ROOT = process.env.PEF_ALLOW_ROOT || process.cwd()

function safeCliArg(value: string, allowRoot: string = ALLOW_ROOT): string {
  if (!value || value.length > 1024) throw new Error('参数非法: 空值或超长')
  if (value.startsWith('-')) throw new Error(`参数非法: 不允许以 "-" 开头（防 CLI 注入）: ${value.slice(0, 40)}`)
  if (/[\s\u0000-\u001f]/.test(value)) throw new Error('参数非法: 不允许空白/控制字符')
  const resolved = path.resolve(value)
  const root = path.resolve(allowRoot)
  if (resolved !== root && !resolved.startsWith(root + path.sep)) {
    throw new Error(`参数非法: 路径越界，必须位于 ${root} 内`)
  }
  return value
}

export const name = 'dsh-tool-pef-phi-compiler'
export const inject = ['tools']

const execFileAsync = promisify(execFile)

/** pef_compile.py 路径，可在部署时通过环境变量覆盖 */
const PEF_PATH = process.env.PEF_PHI_PATH || './scripts/pef_compile.py'
/** 子进程执行超时时间（毫秒） */
const EXEC_TIMEOUT = 60_000

export function apply(ctx: Context) {
  ctx.tools.register(defineTool({
    name: 'pef_phi_compile',
    description: '把哲学/宗教/工程/AI 架构方言文本编译到 PEF 公共语法（P+ΔV→J），自动锚检测 + 语义级结构映射 + 残留率 ρ\'。dialect 可选：auto | daojia | buddhism | quantum | ai_arch',
    parameters: {
      input: {
        type: 'string',
        required: true,
        description: '待编译的方言文本文件路径（UTF-8），如 examples/daojia.txt',
      },
      dialect: {
        type: 'string',
        required: true,
        description: '源方言：auto（按信号识别）| daojia | buddhism | quantum | ai_arch',
      },
      seq: {
        type: 'string',
        required: false,
        description: 'π 锚序号（可复现编译，默认按时间）',
      },
    },
    output: {
      schema: { type: 'string' },
      render: (_args, value) => [{ type: 'text', text: value }],
    },
    async execute(args) {
      const inputPath = safeCliArg(args.input)
      const outPath = `${inputPath}.compiled.json`
      const cmd = [PEF_PATH, 'compile', '--input', inputPath, '--source-dialect', args.dialect, '--out', outPath]
      if (args.seq) cmd.push('--seq', String(args.seq))
      try {
        const { stdout } = await execFileAsync('python', cmd, {
          timeout: EXEC_TIMEOUT,
          encoding: 'utf-8',
          maxBuffer: 10 * 1024 * 1024,
        })
        return stdout.trim() || `已编译: ${args.input} (${args.dialect}) → ${outPath}`
      } catch (err: any) {
        throw new Error(`PEF Phi compile failed: ${err.stderr || err.message}`)
      }
    },
  }))
}
