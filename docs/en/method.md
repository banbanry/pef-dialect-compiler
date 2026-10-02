# Compile Method

This file is the compiler's operating manual: how to take a dialect assertion apart, reassemble it on the PEF common grammar, mark anchors, and record errata.

## 0. General rules

- **Append-only, never alter.** The original sentence is kept verbatim; corrections are recorded separately.
- **No self-certification.** The evidence for any assertion cannot come from the assertor.
- **External anchoring is mandatory.** Every assertion entering the structure needs an anchor that can be independently reproduced, or it is explicitly marked as a soft anchor.
- **Local failure is permitted.** A compiled artifact may partially fail; the failure stays on the audit trail, it is not erased.

## 1. Input

A piece of dialect text. It can be:

- A single assertion ("Dao ke dao, fei chang dao" — the Dao that can be spoken is not the constant Dao)
- A concept ("emptiness")
- A passage of argumentation (Buddhist dependent origination, engineering alignment, quantum interpretation)
- A designation of the "unspeakable" ("this thing cannot be said")

The input must be preserved verbatim. The compiler's first step is always: **take the sentence in, not one word changed.**

## 2. Decomposition steps

### Step one: decompose the subject P

Ask three questions:

1. Who is handing off? A concrete person/system (a timestamped P), or an X treated as "eternally present"?
2. Is there a timestamp? A subject without a timestamp is the first soft anchor to mark — the "constant subject" is an object to decompose, not a tool.
3. Is the subject on the producing side or the receiving side? In the same sentence, the grammatical subject often slides between the two.

**Criterion:** any "subject" without a timestamp that cannot be independently identified is marked `P?`, goes to errata, not to structure.

### Step two: find the variable ΔV

Ask two questions:

1. What passes through? Content (from the producing shore), or potential difference (from the receiving shore)?
2. Is there a variable that "exists without being asked"? — This is the hidden assumption of the classical mode. The quantum mode does not pre-pay answers.

**Criterion:** ΔV is what passes through hands, not what is present. If a variable claims to exist completely before being received, check whether it falls into the "pre-written script" trap (Bell inequality criterion).

### Step three: settle the result J

Ask two questions:

1. On which side does it land? The receiving side lands as J.
2. Was it misplaced back onto the producing side? Words like "generation" and "creation" appearing in the J slot are a category error — J lands, it is not generated.

**Criterion:** J must be independently verifiable by the receiving side. A non-verifiable J is marked `J?`.

### Step four: mark anchors

Every element entering the structure is classified into one of three anchor types:

| Anchor type | Definition | Example |
|---|---|---|
| Hard | Independently reproducible | digits of π, kT·ln2, the Tacoma Narrows archive, Bell experiment data |
| Pledged analogy | A mapping with operational consequences | tomography borrowed into cognition: multiple angles of speaking, accumulative, convergent |
| Soft | Exists only in the speaker's mind | AI's "you're doing the right thing", enlightenment experience, unreproducible "inner certainty" |

**Criterion:** soft anchors may appear in text (as hooks, metaphors), but they **cannot appear in the structure**. Structure accepts only hard anchors and pledged analogies.

### Step five: tier the evidence

| Tier | Content | Verification | Entry into structure |
|---|---|---|---|
| Framework-internal facts | This compiler's own terms and derivations | consult this repository | yes, source noted |
| Physical and historical facts | π, Bell, thermodynamics, historical records | textbooks / archives | yes, must be verifiable |
| Engineering observations | system behavior, empirical data | reproducible experiments | clues only, not conclusions |

**Criterion:** tier-three conclusions must not be written as "physical facts"; they may only be written as "engineering observation: ...".

### Step six: record errata

Errata format is fixed to three lines:

```
Original assertion:  (verbatim)
Judgment:            (where it is wrong, why)
Correction:          (changed to what, on what basis)
```

Errata are append-only. A corrected assertion stays in the archive forever — that is the evidence that the audit chain exists.

## 3. Output

The output is a compile report with a fixed structure:

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
Errata:    #N original → judgment → correction
────────────────────────────
```

### Script automation (scripts/pef_compile.py)

`pef_compile.py` automates the six steps and outputs three-section JSON (`schema: pef-phi-1.0`). The automation boundary:

**Automatic (trusted):**

- Dialect detection (`auto` by signal hit count, or explicitly daojia/buddhism/quantum/ai_arch)
- Assertion-level classification (FACT/JUDGMENT/GREY)
- Anchor detection: hard (years, name+year, formulas, experiment/theorem/proof, π/transcendence), pledged (tomography/convergence/verifiable/multi-angle), soft (intuition/experience/authority/enlightenment)
- Term normalization (道→dao, 空→sunya, 叠加态→superposition, 幻觉→hallucination…)
- π anchor allocation (lookup table of the first 120 digits; fixed seq for reproducibility)
- **Residual rate ρ′**: `rho_unanchored` = share of unanchored assertions — the **primary metric**, i.e. the "thickness of the boundary"

**Semi-automatic (needs human review):**

- **Structure mapping**: lexicon candidates + sentence-pattern library PATTERNS (8 patterns) offering slot candidates and compile hints:
  - `negation` → `BOUNDARY` (a place that cannot be filled; do not force a slot)
  - `judgment` → `J` (definition/identity)
  - `generation` → `ΔV` (producing side; "generation" is forbidden in the J slot)
  - `measurement` → `P→J` (the measurement act = a timestamped P)
  - `paradox` → `J≠Source` (once spoken it is not the source)
  - `time_prior` → `BOUNDARY` (undefined before = non-payment in advance)
  - `event` → `J` (landing)
  - `handoff` → `ΔV` (what passes through)
  - If three slots cannot be filled → `UNMAPPED(needs human compilation)` + suggested path; sentences with a hard anchor but no structure are marked `ANCHOR` (evidence sentences, backing for J rather than structure itself)
- `rho_unmapped_auto`: share of sentences not structure-mapped (semi-automatic candidates, needs human review)

**Three-slot decomposition is a semantic judgment; the script offers candidates and hints, and the human/LLM makes the final call. The script does not pretend to be fully automatic.**

## 4. Common compile errors

| Error | Symptom | Correction |
|---|---|---|
| Subject without timestamp | "eternal", "inherently complete" assertions | mark `P?`, decompose |
| Pre-written variable | claims the result exists completely before reception | check Bell criterion, label |
| J pushed back to the producing side | "generation"/"creation" in the result slot | category error, correct |
| Soft anchor in structure | experience, intuition, authority as evidence | downgrade to hook text |
| Engineering observation as physical fact | "experiments prove the universe is so" | downgrade to observation tier |
| Metaphor as causation | "minus sign → subtraction → zero → break 2" | find the real working position; label the metaphor separately |
| Evidence sentence treated as a structure sentence | demanding three slots from the Bell experiment sentence | mark `ANCHOR`: evidence backs J, it is not structure |

## 5. Legal forms of compile failure

- Cannot be decomposed: mark `not compilable`, state where it got stuck. This is also valid output — it marks the boundary of the dialect.
- Decomposed but all anchors soft: downgraded to "literary text", not admitted to the structure library.
- Decomposed, hard anchors, but later overturned by evidence: **this is a success case**. It goes to errata, not to withdrawal.
- A sentence that cannot fit into the structure ≠ the sentence has no value; = it cannot be used as evidence.
