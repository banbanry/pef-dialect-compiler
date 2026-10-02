# PEF Common Grammar Specification

This file defines the compiler's output language: the precise meaning of `P + ΔV → J` and the three error-handling rules. Every compile report must obey this specification.

## 1. The triad

```
P + ΔV → J
```

- **P (Subject)**: a handoff party with a timestamp. It drifts, it ages, it can be anchored. A "subject" without a timestamp is not a P — it is a `P?` to be decomposed.
- **ΔV (Variable)**: what passes through hands. From the producing shore it is **content**; from the receiving shore it is **potential difference**. The same ΔV, two names on two shores, no contradiction.
- **J (Result)**: what lands on the receiving side. J lands, it is not generated; "generation" is a verb of the producing side and cannot appear in the result slot.

> This triad is not a discovery about the universe. It is a minimal grammar for any handoff: **something is emitted, something is transferred, something lands.** What is genuinely new is the three error-handling rules attached to it.

## 2. The three error-handling rules

### Rule one: No self-certification

The audited party cannot simultaneously be the audit basis.

- A model saying it is aligned — not counted; external evaluation required.
- A system claiming to be the final answer — not counted; self-certification trap.
- "I have awakened, therefore what I say is right" — not counted; `P?` plus soft anchor.

**Counterexample criterion:** if the deviation is self-reported by the audited party, the audit object and the audit reference become one, and the audit structurally fails.

### Rule two: External anchoring is mandatory

Every assertion entering the structure must have an anchor that can be independently reproduced.

- The digits of π can be recomputed (hard).
- kT·ln2 is in textbooks (hard).
- The 129 days of the Tacoma Narrows bridge are in the archives (hard).
- "You're doing the right thing" exists only in the speaker's mind (soft, not structure).

**Soft anchor handling:** soft anchors may exist as hooks, metaphors, literary text, but must not be used as structural evidence.

### Rule three: Local failure is permitted

The system is not required to be always correct. It requires: failures are recorded, auditable, and may fail locally without bringing down the whole.

- Errata cards: append-only, never alter.
- Version management: the original is preserved, corrections recorded separately.
- Death clauses: a system must be able to pre-write its own failure modes.

## 3. Three evidence tiers

| Tier | Content | Entry into structure |
|---|---|---|
| Framework-internal facts | this system's own terms and derivations | yes, source noted |
| Physical and historical facts | verifiable in textbooks | yes, must be verifiable |
| Engineering observations | empirical data | clues only, not conclusions |

## 4. Glossary

| Term | Definition | Common misuse |
|---|---|---|
| P | subject with a timestamp | treated as "eternal self" |
| ΔV | the variable that passes through (content/potential difference) | treated as "pre-existing complete object" |
| J | the result that lands on the receiving side | written as "generation" |
| Hard anchor | independently reproducible | soft anchor passed off as hard |
| Soft anchor | exists only in the speaker's mind | placed into structure as evidence |
| Errata | original → judgment → correction, append-only | altering the original text |
| Source | no reference, prior to time, unobservable | given a name/predicate/perspective |

## 5. Three prohibitions on the "Source" (inherited from *The Source and Its Names*)

1. **Do not predicate it.** Saying "the Source is constant" projects a variable-layer property onto the Source.
2. **Do not give it a perspective.** What has no reference has no "for it."
3. **Do not name it.** A single "it" is already a naming; naming is projection.

Only three grammars are legal for the Source: the negative (what it is not), the indicative (where it points), and the approximate at a distance (what it resembles, within what limits).
