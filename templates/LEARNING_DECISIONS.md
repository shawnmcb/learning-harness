# LEARNING_DECISIONS — Conclusions Log

Traceable-rationale log. Every LD entry: claim, evidence (provenance-tagged),
confidence (0–100%), falsification conditions, staleness fields. Append-only —
a changed mind gets a new entry that supersedes and links the old one.

Entry types, staleness invariant (T1–T5), and verification protocols: see
PROTOCOLS.md in the harness package. Triage: TRIAGE-RUBRIC.md.

---

## LD-001 — <short claim title> (<date>)

**Claim**: <the conclusion, stated so it could be wrong>

**Evidence**:
- <source or basis> — [corpus recollection]            <!-- or: [READ <date>] -->
- <source or basis> — [READ <date>; <what was confirmed>]

**Confidence**: <NN>% — <one sentence on why this number, tied to provenance>

**Would change my mind**:
- <observable condition 1>
- <observable condition 2>

**Verification**: <none yet | passed VT-00N (<date>)>

`last_verified`: never
`decay_trigger`: defaults (T1–T5)

---

## Triage runs

<!-- Log each /triage-knowledge run: date, scores per entry, top-3 with
     one-sentence rationales. -->

## Verification events

<!-- VT entries (immutable). Under protocol: hardened-v1.1 each records:
     the numbered answer key (logged before rebuttal), the F-numbered rebuttal,
     grade with the three booleans (caught-exact, steelman-novel,
     rebuttal-cites-discriminator), and grader mapping(s). -->

<!-- VB entries (skill domains): pre-declared exercise + 2–4 recording-
     adjudicable criteria; per-criterion pass/fail from the recording. -->

## Durability signals

<!-- DS entries: signal_type resistance|gap; the three calibration questions. -->
