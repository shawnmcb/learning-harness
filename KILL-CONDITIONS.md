# Kill Conditions — Pre-Registered Falsification

These are not risks to mitigate; they are observations that mean **redesign, not
iterate**. If you hit one, believe the condition, not the system.

## Transmission kill conditions

- **K1 — reproducibility failure**: two practitioners scoring the same entries
  with the triage rubric diverge on any axis in more than 1 of 10 paired
  scorings. (The rubric's whole claim is that scoring is mechanical.)
- **K2 — structure loss**: a cold-start practitioner's log, after one full cycle
  of `COLD-START.md`, lacks any of {staleness fields, provenance tags,
  commit-before-reveal verification}. The schema did not survive transfer.
- **K3 — triage adds nothing**: over ~90 days, executing queue heads clears
  staleness/trust/gap findings at a rate indistinguishable from self-chosen study
  order. (The queue must beat intuition or it is overhead.)
- **K4 — metric death**: entries whose verification chains show
  caught-exact/novel-steelman events fail later blind verifications at equal or
  higher rates than entries verified only by correct recall, repeatedly beyond
  chance. This kills the system's central bet — that misconception-resistance
  predicts durability better than correct-answer knowledge. The comparison
  cohorts are constructible from the logged booleans alone.
- **K5 — cost dominance**: the median practitioner's per-cycle logging overhead
  exceeds their per-cycle study time (by timestamps) for three consecutive
  cycles. The harness is eating the learning.

## Team-scale pre-registration template

The primitive most vulnerable at team scale is VT grading — specifically the
`caught-exact` reason-match call, because it gates the resistance tag, both the
T and G axes, DS typing, and K4's cohorts simultaneously. The hardened protocol
(numbered keys, F-number mapping, independent commit-then-compare, auto-partial
on disagreement) is the mitigation. If a team adopts this, pre-register before
day one:

- **CONFIRMS (30 days, ≥10 double-graded VTs)**: caught-exact agreement ≥9/10,
  AND each practitioner's resistance-tag base rate within ±20 percentage points
  of the team median.
- **TRIGGERS K1-class kill**: agreement ≤7/10, or the same VT tagged differently
  by a practitioner pair more than once.

Two hardening layers require real team context and are deliberately not claimed
as built: a **grader calibration corpus** (adjudicated steelman/key/rebuttal/tag
sets that new graders must score ≥9/10 against before their tags count, re-run
periodically) and **tag audits** (a third party re-grades a random sample of
caught-exact tags per cycle; per-grader disagreement rates are tracked). Both
double as the data K4 needs, so they pay rent beyond quality control.
