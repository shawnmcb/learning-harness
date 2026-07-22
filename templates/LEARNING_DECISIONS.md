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

<!-- VT entries are immutable. Use ONE of these two shapes — the checker's
     protocol lint scans both; anything else silently bypasses it: -->

<!-- Bullet form:
- **VT-001** (<date>, against LD-001; protocol: hardened-v1.1):
  Answer key (logged before rebuttal): 1. asserts P; actually ¬P because Q ...
  Rebuttal: F1 <flaw named> ... F2 ...
  Mapping: F1→key-1. Grade: caught-exact: true|false; steelman-novel: true|false;
  rebuttal-cites-discriminator: true|false. Result + what it confirmed/exposed.
-->

<!-- Heading form (equivalent):
### VT-001 (<date>, against LD-001; protocol: hardened-v1.1)
<same required elements as above>
-->

<!-- VB entries (skill domains): pre-declared exercise + 2–4 recording-
     adjudicable criteria; per-criterion pass/fail from the recording. -->

## Durability signals

<!-- DS entries: signal_type resistance|gap; the three calibration questions. -->
