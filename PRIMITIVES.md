# Primitives Manifest

Each primitive is defined as an instantiation test: for any given action or file,
the definition answers yes/no — "does this instantiate the primitive?"

- **LEARNING_SPEC**: instantiated iff the domain file contains 3–5 sub-areas, each
  with enumerated "understanding = able to answer/do" questions, plus a three-tier
  source-quality table and the corpus-knowledge rule (no ≥80% confidence from
  recollection alone).
- **LD entry**: instantiated iff it carries all of: claim; evidence lines each
  bearing a provenance tag (`[READ <date>]` or an UNREAD marker); confidence %;
  would-change-my-mind conditions; `last_verified`; `decay_trigger`.
- **SY / CDS entry**: instantiated iff it names ≥2 prior entries (CDS: from
  different sub-areas), states reinforcement-or-tension, derives a claim quoted in
  no constituent, and (CDS only) logs an intersection-misconception marked
  `PENDING VERIFICATION TARGET`.
- **VT event**: instantiated iff the steelman came from a party given only the
  claim text; the rebuttal was committed before the reveal; the event is a
  different session than the target entry's creation; the grade records the three
  booleans (caught-exact, steelman-novel, rebuttal-cites-discriminator); and,
  under `protocol: hardened-v1.1` (required for new events): a numbered
  "asserts P; actually ¬P because Q" answer key logged before the rebuttal,
  F-numbered rebuttal points, independent grader mappings compared only after
  commitment, and non-unanimity auto-grading `partial`.
- **VB event**: instantiated iff the exercise and 2–4 recording-adjudicable pass
  criteria were written before the attempt and every criterion is graded from the
  recording.
- **DS entry**: instantiated iff attached to a named VT/VB, carrying
  `signal_type: resistance | gap`, and answering the three calibration questions
  (what it proves; which mechanism produced it; what would have flipped it).
- **Staleness invariant + checker**: instantiated iff every LD/SY/CDS carries the
  two staleness fields, all triggers are events (T1–T5, no calendar terms), and
  the scanner separates mechanical findings from judgment items.
- **Triage rubric + queue**: instantiated iff every LD/SY/CDS is scored S+T+G by
  the string-level tests, the full ranked list is logged with rationales, and the
  queue head becomes the next session's default opener.
- **TVL (triage-verification loop)**: instantiated iff a gauntlet was generated
  against the current queue head, each claim is annotated with the rubric
  dimension that produced resistance or permitted a slip, and post-run scores are
  recomputed.
- **PRECISION_DRILL**: instantiated iff a claim is restated under all three
  constraints (jargon-free skeptic rebuttal; machine-checkable criterion;
  falsifiable form) and logged with a target gap.
- **Gauntlet escalation ladder**: instantiated iff consecutive clean rounds
  trigger a harder class next (self-play → least-verified sub-area →
  source-grounded), with the diminishing-information rationale logged.
- **Resistance/gap orthogonality**: a single VT can set BOTH the resistance tag
  (≥1 caught-exact/novel/discriminator item) AND G=2 via a SLIP on another item —
  the verdicts are independent and both are recorded.
