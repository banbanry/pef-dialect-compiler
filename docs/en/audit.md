# Audit Discipline

Everything the compiler produces obeys this discipline. This is the basis for "the compiler can be trusted" — not the author's authority, but reproducible audit records.

## 1. Append-only, never alter

- The dialect sentence is kept verbatim.
- Errata are append-only: the original assertion is always preserved; the judgment and correction are recorded separately.
- Versions only grow: an overturned compiled artifact is not withdrawn, it enters the errata.

## 2. Source cards

Every compiled object must carry a source card recording:

- The provenance of each anchor (theorem, experiment, archive, textbook entry)
- The boundary of analogies and mappings (front end anchored; whether the back end is settled)
- A declaration of "author dialect" (which sentences are framework-internal terms, not general meanings)

A source card takes no position in the main text. It only records: on which anchor this assertion stands.

## 3. Errata cards

Errata card format:

```
Erratum #N: title of the original assertion
Original assertion:  (verbatim)
Judgment:            (where it is wrong)
Correction:          (changed to what, on what basis)
```

The source of the erratum must be noted (self-correction / external audit). The corrected assertion stays on file per the append-only principle.

## 4. Three-review system

Large compiled objects (article-level) should go through:

1. **First review**: does the decomposition hold (are P/ΔV/J placed correctly)?
2. **Second review**: is the anchor really hard (can it be independently reproduced)?
3. **Third review**: is the errata complete (is a counterexample left)?

The three-review conclusion is recorded in the finalization note. The finalization note is deleted at publication, but the archive keeps it.

## 5. Hard boundaries

| Boundary | Handling |
|---|---|
| Physical facts vs analogies | the physical layer has anchors; the cognitive-mapping layer is a pledged analogy, not endorsed inside the card |
| Engineering observations vs physical facts | observation-tier conclusions must not be written as physical facts |
| Soft anchors | hooks only, never structure |
| The "unspeakable" | only concedes "cannot be finished in one utterance", never "cannot be computed" |
| Death clauses | every compiled object pre-writes its own failure modes |
