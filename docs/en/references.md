# Reference Corpus Registry

The compiler's compile objects and methods are taken directly from two existing bodies of material: the **nine trials** (pef-philosophy essays) and the **novella** (*The Architect's Dream*). This file registers what each piece is used for in the compiler.

## The nine trials (essays)

Source repo: `github.com/banbanry/pef-philosophy` (`essays/01`–`09`)

| # | Trial | Use in the compiler |
|---|---|---|
| 01 | The Root of AI (projection chain) | methodological source of "every expression is a lossy projection"; the theoretical basis of the compiler's receive → decompose steps |
| 02 | The Pi Anchor | "RLHF anchored to human preference → sycophancy and hallucination"; direct source of compile object 01-AI architecture, erratum #1 |
| 03 | Arrogance of Pi Anchor | "a single anchor locked into resonance"; warning in the anchoring step — anchors must be detunable |
| 04 | Three Doors to Silicon Death | "digital immortality is a thermodynamic dead end"; the thermodynamic basis of the "local failure permitted" rule |
| 05 | PEF Architecture | the formal definition of the `P + ΔV → J` triad and the three constraints; the source of this compiler's grammar spec |
| 06 | The Ferryman's Seven Days | "dynamic homeostasis = borrow force, do not resist head-on"; mapping source of compile object 02-Daoism "wu wei" |
| 07 | The Master's Shadow | "results can be inherited, protocols must be executed", the definition of soft anchor; source of the rule "soft anchors never enter structure" |
| 08 | The Next Stroke | "the mind is not a mirror, not π, it is the next stroke"; source of the three legal grammars for the Source |
| 09 | The Source and Its Names | the three prohibitions on naming the Source; direct source of the compiler's "three prohibitions on the Source" and the errata institution |

## The novella

Source repo: `github.com/banbanry/the-architects-dream` (9 chapters)

The novella is the compiler's "hook layer" — it does not explain structure, it makes the reader stop and look. The compiler's methodology (decompose, anchor, errata) received its first demonstration in narrative form; *The Ferryman's Seven Days* is the most complete narrative sample of "dynamic homeostasis", and the predecessor narrative of *The Ferryman's Solitary Road* performed the first compilation demonstration of quantum mechanics.

| Novella element | Compiler counterpart |
|---|---|
| The ferryman's seven days | dynamic homeostasis / borrow force, do not resist / unknown undercurrent: pause three circles first (suspend active regulation, pure observation) |
| The handoff of the pole | results can be inherited, protocols must be executed; narrative version of the audit chain |
| Sitting on the riverbed looking at stones when the river dries up | L0 failure clause; "acknowledge there is no executable action when there is none" |

## Outside essay (Chinese)

Source: `pef-philosophy/docs/cn-outside-01.html` *The Ferryman's Solitary Road*

**Prior compilation demonstration** of the quantum mechanics dialect: superposition, measurement, Bell inequality, and the transcendence of π were first decomposed there, with twenty errata entries. The compiler's `04-quantum.md` is its structured reset.

## Usage discipline

- Compile methods come from the published trials; if a compile result conflicts with a trial, the compiler's errata card prevails (append-only).
- The novella serves as hooks and narrative reference only, never as evidence. Evidence is drawn only from trials, textbooks, and experimental archives.
- Framework-internal judgments quoted from the trials must be labeled "framework-internal facts", never written as general conclusions.
