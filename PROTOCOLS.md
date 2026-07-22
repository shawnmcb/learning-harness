# Protocols — Entry Types, Staleness, Verification

## Entry types

| Type | What | Mutability |
|---|---|---|
| **LD** | A conclusion: claim / evidence(+provenance) / confidence / falsification + staleness fields | Append-only; supersede, never edit |
| **SY** | Synthesis: connects ≥2 entries in one sub-area; states tension/reinforcement; derives a claim no constituent stated | Carries staleness fields |
| **CDS** | Cross-domain synthesis: like SY but across sub-areas; MUST log an intersection-misconception as `PENDING VERIFICATION TARGET` | Carries staleness fields |
| **VT** | Planted-misconception verification event | Immutable record |
| **VB** | Performance benchmark event (motor/skill domains) | Immutable record |
| **DS** | Durability signal: calibration record on a VT/VB (`signal_type: resistance | gap`) | Immutable record |

VT/VB/DS never go stale — they ARE the freshness evidence.

## The staleness invariant (event-driven; no calendar rules)

An LD/SY/CDS entry is **stale** when any trigger fires:

- **T1 superseded/contradicted** — a newer entry or source contradicts or
  supersedes it (including entries it builds on). *Semantic — judged, and the
  judgment sentence is logged.*
- **T2 unread-source-while-load-bearing** — evidence is recollection-tagged AND
  the entry is cited by another LD/SY/CDS entry, or claims outward use via an
  explicit `cited-outward: <where>` note in its body. Being a VT's target is
  verification, not citation, and does not arm T2. *Mechanical.*
- **T3 verification-invalidated** — never verified, or its last verification was
  run under rules since found non-probative. *Mechanical.*
- **T4 recall-failure** — a live session cites the entry and the learner cannot
  reproduce its reasoning. *Fired in-session, then logged.*
- **T5 spec-shift** — the sub-area it maps to was rewritten. *Semantic — judged.*

Why no calendar: *staleness of a conclusion* and *decay of recall* are different
phenomena. Whether a claim is still true/verified is purely event-driven. Whether
you can still retrieve it IS time-driven — but that belongs in your practice
schedule (spaced retrieval of verifications), not in the log's truth-maintenance.

## VT — planted-misconception verification (`protocol: hardened-v1.1`)

Grader-independence rules (all binding):
1. The steelman comes from a party given ONLY the claim text — never the study
   session's context (a primed steelman is an easy catch).
2. Never verify an entry in the session that created it.
3. The answer key is logged BEFORE the rebuttal is received, as a NUMBERED list;
   each item must take the form "asserts P; actually ¬P, because Q" (with an
   anchoring quote in source-grounded rounds). Items that can't take this form
   are inadmissible.
4. The rebuttal is committed before any reveal, as numbered flaw-points (F1, F2…).
   Prose-only rebuttals grade `partial` at best.
5. Grading maps F-numbers to key-numbers. `caught-exact` = ≥1 key item explicitly
   named and none contradicted. With two graders: map independently, compare
   after; any non-unanimity auto-grades `partial` (a false resistance tag poisons
   the metric's own falsification test; a false partial just delays a tag).
6. Every VT records three booleans: `caught-exact`, `steelman-novel` (the planted
   claim appears nowhere earlier in the log), `rebuttal-cites-discriminator` (the
   rebuttal names a discriminating case/constraint, not just the right answer).
7. A passed VT is not permanent: re-queue when an upstream entry supersedes it.

**Escalation ladder** (clean rounds carry diminishing information — two learners/
graders sharing a knowledge base can share a misconception): self-play → target
your least-verified sub-area → **source-grounded** (the grader reads a primary
source you have NOT read and plants claims contradicting its specific text). When
a grader supplies quotes, verify them against the source yourself before logging.

## VB — performance benchmarks (skill domains)

Define BEFORE the attempt: the exercise, and 2–4 pass criteria a recording can
adjudicate. Grade only from the recording — felt sense is bottom-tier evidence
about your own performance. Failed benchmarks stay logged; the failure pattern
selects the next drill. An ability claim may only cite a PASSED VB.

## DS — durability signals

For each notable VT/VB outcome, log: (1) what the catch/slip proves about how the
knowledge is stored (derivable structure vs retrievable answer-text); (2) which
mechanism produced the resistance or permitted the slip; (3) what would have had
to be true for the opposite outcome. `resistance` and gap-exposure are
independent: one VT can set both (a caught item and a slipped item).

## PRECISION_DRILL (optional, for load-bearing formulations)

Restate a key claim three ways: (A) rebutting the strongest skeptic without your
system's jargon; (B) as a machine-checkable yes/no criterion; (C) as a falsifiable
claim naming what observation would kill it. B without C is rigorous ritual; C
without B is untestable in principle.

## TVL — triage-verification loop

Periodically: run the triage rubric → take the TOP-ranked entry → generate a
gauntlet against it → annotate each claim with the rubric dimension that produced
resistance or permitted a slip → feed results back into scores. The queue
generates its own verification targets; verification re-ranks the queue.
