# PEF Dialect Compiler

Compile philosophical dialects, concepts, and the "unspeakable" into the PEF common grammar.

**The PEF common grammar (one line):**
Any handoff can be written as `P + ΔV → J` — a subject with a timestamp, a variable arriving at the receiving side as a potential difference, a result that lands; plus three error-handling rules: **no self-certification, external anchoring is mandatory, local failure is permitted (and leaves an audit trail)**.

**What this compiler does:**
Philosophy, religion, engineering, and AI architecture each speak their own dialect. Every dialect contains an "unspeakable" — the previous generation dismantled the scaffolding, and later generations can only memorize the concepts. This compiler tries to take those concepts apart again and reassemble them on the `P + ΔV → J` common grammar, so that any assertion in any dialect can be: decomposed, anchored, audited, refuted.

**What this compiler does NOT do:**
It does not preach. It does not claim a final answer. It does not claim the "unspeakable" has been fully spoken. It does one thing only: puts every assertion back into the handoff structure, marks its anchor, records its errata.

---

## What a compiled artifact looks like

Each compiled object produces one report:

```
Dialect sentence   (verbatim, not one word changed)
─────────────
Subject P          (who is handing off? timestamp?)
Variable ΔV        (what passes through? content from the producing shore,
                    potential difference from the receiving shore)
Result J           (where does it land?)
─────────────
Anchors            (what is independently reproducible? math/experiment/
                    physical invariant = hard; not reproducible = soft, labeled)
Evidence tier      (framework-internal / physical-historical / engineering
                    observation — three tiers)
Errata             (original assertion → judgment → correction; append-only)
```

## Quick start

```bash
# Compile a dialect text file (UTF-8)
python scripts/pef_compile.py compile --input dialect.txt

# Specify dialect + fixed π anchor sequence (reproducible)
python scripts/pef_compile.py compile --input dialect.txt --source-dialect daojia --seq 7 --out out.json

# List the dialect registry (daojia / buddhism / quantum / ai_arch)
python scripts/pef_compile.py dialects
```

Output is three-section JSON (`schema: pef-phi-1.0`):

```json
{
  "compiled": { "source_dialect": "daojia", "pi_anchor": "π-7-6", "claims": [...], "terms_normalized": {...} },
  "dialect":  { "matched": "daojia", "signals_hit": [...] },
  "audit":    { "rho_residual": 1.0, "rho_unanchored": 1.0, "rho_unmapped_auto": 1.0, "hash": "...", "ts": "..." }
}
```

### Script honesty boundary

- **Automatic (trusted):** dialect detection, assertion-level classification, anchor detection (hard / pledged / soft), π anchor allocation, term normalization, residual rate ρ′.
- **Semi-automatic (needs human review):** structure mapping only offers candidate slots; if the three slots cannot be filled it marks `UNMAPPED(needs human compilation)` — three-slot decomposition is a semantic judgment, the script does not pretend to be fully automatic.
- **ρ′ primary metric** = share of unanchored assertions, i.e. the "thickness of the boundary": high ρ′ = much of this dialect is unspeakable; low ρ′ = it has been spoken to the end. ρ′ = 0 with a hard anchor on every sentence is the threshold for admission into the structure library.

## Six compile steps

1. **Receive the sentence verbatim.** Append-only, never alter.
2. **Decompose the subject P.** Who hands off? Is there a timestamp? A subject without a timestamp is a `P?` — an object to decompose, not a tool to decompose with.
3. **Find the variable ΔV.** What passes through? Content from the producing shore, potential difference from the receiving shore. Check for pre-written variables (Bell criterion).
4. **Settle the result J.** On the receiving side. J lands, it is not generated; "generation" in the result slot is a category error.
5. **Mark anchors.** Hard (independently reproducible: π, kT·ln2, experiment data, archives) / pledged analogy (has operational consequences) / soft (exists only in the speaker's mind; hooks only, never structure).
6. **Record errata.** Original assertion → judgment → correction. Append-only.

## Three evidence tiers

| Tier | Content | Entry into structure |
|---|---|---|
| Framework-internal facts | This system's own terms and derivations | Yes, source noted |
| Physical and historical facts | Verifiable in textbooks | Yes, must be verifiable |
| Engineering observations | Empirical data | Clues only, not conclusions |

## Structure

```
docs/
  method.md        compile method (decomposition steps & criteria)
  grammar.md       PEF common grammar spec
  audit.md         audit discipline (source cards, errata cards, append-only)
  references.md    reference corpus registry (nine trials, novella, outside essays)
  en/              English versions of the above
skill/
  SKILL.md         compile skill (Chinese; drives scripts/pef_compile.py)
  SKILL.en.md      English version
scripts/
  pef_compile.py   philosophical dialect compiler (automatic anchor detection +
                   semantic structure mapping + residual rate ρ′)
plugin/
  dsh-tool-pef-phi-compiler/   DSH tool plugin (format aligned with dsh-pef-plugins)
    index.ts        plugin entry (defineTool + safeCliArg injection guard + calls pef_compile.py)
    package.json    plugin manifest
    README.md       plugin usage (English)
examples/
  daojia.txt        sample: Daoism
  buddhism.txt      sample: Buddhism
  quantum.txt       sample: quantum mechanics
  ai_arch.txt       sample: AI architecture
essays/
  01-ai-arch.md     cut 01: AI architecture dialect
  02-daojia.md      cut 02: Daoist dialect
  03-buddhism.md    cut 03: Buddhist/Chan dialect
  04-quantum.md     cut 04: quantum mechanics dialect (finale)
```

中文版文档：`README.zh-CN.md` · `skill/SKILL.md` · `docs/method.md` 等（与英文版同步）。

## Roadmap

- [x] Repository & methodology skeleton
- [x] 01 · AI architecture dialect (LLM hallucination / RLHF / alignment / emergence / consciousness counterexample)
- [x] 02 · Daoist dialect (Dao ke dao / wu wei / reversal / supreme good like water)
- [x] 03 · Buddhist dialect (unspeakable / emptiness / dependent origination / self-grasping)
- [x] 04 · Quantum mechanics dialect (superposition / measurement / Bell / transcendence of π)
- [x] Reference corpus registry (nine trials / novella / outside essays)
- [x] Compiler script pef_compile.py: automatic anchor detection + semantic structure mapping + residual rate ρ′
- [x] Structure mapping upgrade: semantic-level three-slot decomposition (lexicon + sentence-pattern library PATTERNS + compile hints)
- [x] Skill consolidation: DSH plugin packaging (plugin/dsh-tool-pef-phi-compiler, format aligned with dsh-pef-plugins)

## Verification

Every compiled artifact can be independently verified:

- Anchors: readers can re-check textbooks / archives themselves;
- Errata: append-only, history preserved;
- Refutation: anyone who disputes any step of a decomposition can re-decompose per the grammar spec — no authority involved.

## Relation to sibling projects

- `mmc-compiler` (multi-model dialect compiler): same skeleton (π table, three-section schema, audit chain, assertion levels), repurposed for the philosophical domain. **The original mmc-compiler repository is not modified.**
- `pef-philosophy` (essay series, Chinese/English): the theoretical source — the nine trials, the novella *The Architect's Dream*, the outside essays. `docs/references.md` registers this corpus.

---

**This is not a system for you to accept. It is not a conversion, and it asks nothing of you to believe.** It is an engineering draft, written from the shoulders of predecessors, using the environmental variables of this era, about "how to hand off without deceiving yourself." Like the ferryman's experience: it fits the variable stage that produced it; I use it to approach what I take to be true. It is a flashlight in the dark woods: bright enough to show the next tree root — not the sun, and you need not live inside it.

中文版见 [`README.zh-CN.md`](README.zh-CN.md)。
