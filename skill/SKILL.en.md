---
name: pef-dialect-compiler
description: Compile philosophical dialects, concepts and the "unspeakable" into the PEF common grammar (P + ΔV → J + three error-handling rules). Given a passage of philosophical/religious/engineering/AI-architecture prose, this skill decomposes it: receive the sentence → decompose the subject → find the variable → settle the result → mark anchors → tier the evidence → record errata, and emits a structured compile report. Use for "what is this philosophical concept actually saying", "translate this dialect into an auditable structure", "decompose the unspeakable/mystical/religious/technical terms", "align AI-architecture jargon". Not for preaching, not for final answers, not for using soft anchors as evidence.
---

# PEF Dialect Compiler

## Boundary

- **Does**: decompose a dialect assertion into P/ΔV/J, mark anchors, tier evidence, record errata.
- **Does not**: does not adjudicate which philosophical system is right; does not claim the "unspeakable" has been fully spoken; does not use soft anchors (experience, authority, intuition) as structural evidence.
- **Input**: a passage of original text (kept verbatim). May be a single assertion, a concept, a passage, a whole terminology.
- **Output**: a structured compile report (template below) — automatic anchor detection + semi-automatic structure candidates + residual rate ρ′.

## Quick use (script)

```bash
# Compile a dialect text file (UTF-8)
python scripts/pef_compile.py compile --input dialect.txt

# Specify dialect + fixed π anchor sequence (reproducible)
python scripts/pef_compile.py compile --input dialect.txt --source-dialect daojia --seq 7 --out out.json

# List the dialect registry (daojia/buddhism/quantum/ai_arch)
python scripts/pef_compile.py dialects
```

Output is three-section JSON (`schema: pef-phi-1.0`), isomorphic to mmc-compiler:

```json
{
  "compiled": { "source_dialect": "daojia", "pi_anchor": "π-7-6", "claims": [...], "terms_normalized": {...} },
  "dialect":  { "matched": "daojia", "signals_hit": [...] },
  "audit":    { "rho_residual": 1.0, "rho_unanchored": 1.0, "rho_unmapped_auto": 1.0, "hash": "...", "ts": "..." }
}
```

### Script honesty boundary

- **Automatic (trusted)**: dialect detection, assertion-level classification, anchor detection (hard/pledged/soft), π anchor allocation, term normalization, residual rate ρ′.
- **Semi-automatic (needs human)**: structure mapping only offers candidate slots; unfilled slots are marked `UNMAPPED(needs human compilation)` — three-slot decomposition is a semantic judgment, the script does not pretend to be fully automatic.
- **ρ′ primary metric** = share of unanchored assertions, i.e. the "thickness of the boundary": high ρ′ = much of this dialect is unspeakable; low ρ′ = it has been spoken to the end. ρ′ = 0 with a hard anchor on every sentence is the admission threshold for the structure library.

## Compile steps (six, for human review)

1. **Receive the sentence verbatim.** Append-only, never alter.
2. **Decompose the subject P.** Who hands off? Is there a timestamp? A subject without a timestamp is marked `P?` — an object to decompose, not a tool.
3. **Find the variable ΔV.** What passes through? Content from the producing shore, potential difference from the receiving shore. Check for pre-written variables (Bell criterion).
4. **Settle the result J.** On the receiving side. J lands, it is not generated; "generation/creation" in the result slot is a category error.
5. **Mark anchors.** Hard (independently reproducible: π, kT·ln2, experiment data, archives) / pledged analogy (operational consequences) / soft (exists only in the speaker's mind; hook text only, never structure).
6. **Record errata.** Original → judgment → correction. Append-only.

## Output template (human version)

```
────────────────────────────
Dialect sentence
────────────────────────────
P:        subject (timestamped)
ΔV:       variable (potential difference / content)
J:        result (lands on the receiving side)
────────────────────────────
Anchors:
  hard:   ...
  pledged analogy: ...
  soft:   ... (text only, not structure)
Evidence tier:   framework-internal / physical-historical / engineering
Errata:   #N original → judgment → correction
────────────────────────────
```

## Three evidence tiers

| Tier | Content | Entry into structure |
|---|---|---|
| Framework-internal facts | this system's own terms and derivations | yes, source noted |
| Physical and historical facts | verifiable in textbooks | yes, must be verifiable |
| Engineering observations | empirical data | clues only, not conclusions |

## Common compile errors (check actively)

- Subject without timestamp (`P?`)
- Pre-written variable (result exists completely before reception)
- J pushed back to the producing side ("generation" in the result slot)
- Soft anchor in structure (experience/intuition/authority as evidence)
- Engineering observation written as physical fact
- Metaphor used as causation

## Legal forms of compile failure

- Cannot be decomposed → label "not compilable" and the sticking point (this is a valid marker of the dialect boundary)
- All anchors soft → downgraded to literary text, not admitted to the structure library
- Hard anchors but overturned → a success case; goes to errata, not withdrawal

## References and verification

- Common grammar spec: `docs/en/grammar.md`
- Compile method details: `docs/en/method.md`
- Audit discipline: `docs/en/audit.md`
- Relation to mmc-compiler: skeleton inherited (same π table, three-section schema, audit chain), core repurposed for the philosophical domain (structure mapping + anchor detection + ρ′); **the mmc-compiler repository is not modified**.
- Compile examples: `essays/01-ai-arch.md` onward; script samples: `examples/`

Every compiled artifact must be independently verifiable: anchors checkable, errata traceable, decomposition refutable.
