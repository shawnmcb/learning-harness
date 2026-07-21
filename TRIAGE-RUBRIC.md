# Triage Rubric (V2) — /triage-knowledge

Generates the "learn this next" queue from the log's own fields. Applies to every
LD/SY/CDS entry. VT/VB/DS are events and are never scored. Any scorer applying
the string tests below must reach the same numbers; if two scorers diverge, the
rubric is broken, not the scorers (see `KILL-CONDITIONS.md`, K1).

## Shared definitions (string-level, case-insensitive)

- An evidence line is **READ** if it contains a `[READ <date>` tag.
- An evidence line is **UNREAD** if it contains `corpus recollection`, `recalled`,
  or `derived this cycle` (self-inference counts as unread — no external ground).
- A VT/VB event **targets** an entry iff the event's text names the entry's ID, or
  the entry's `last_verified` names the event AND the event is not marked
  `non-probative` and not annotated `pre-entry`.

## S — staleness (input: checker output + logged trigger judgments)

- **S=0**: no mechanical finding for the entry AND no semantic trigger (T1/T5)
  judged firing.
- **S=1**: a T2 finding where ≥1 evidence line is READ (partial provenance
  clearing), OR a semantic trigger judged "partial" with the judgment sentence
  recorded.
- **S=2**: `last_verified: never`/missing; OR a T3 finding; OR a T2 finding with
  zero READ lines; OR any trigger judged fully firing.

## T — trust deficit (input: the entry text alone)

SR (source-read) = every evidence line is READ and none is UNREAD.
BV (blind-verified) = ≥1 valid VT/VB targets the entry.

- **T=0**: SR AND BV. **T=1**: exactly one. **T=2**: neither.

## G — gap exposure

GT = ≥1 VT targets the entry (same test as BV);
DSGAP = a `signal_type: gap` DS names this entry or one of its evidence legs;
PT = entry contains `PENDING VERIFICATION TARGET` not marked resolved;
SLIP = any VT records `missed`/`partial` against this entry.

- **G=0**: GT AND none of DSGAP/PT/SLIP.
- **G=1**: (GT false OR DSGAP true) while PT and SLIP are both false.
- **G=2**: PT true OR SLIP true.

## Combination

**Risk = S + T + G** (equal-weight additive, 0–6).
Why additive: the axes are compensatory — any one axis firing should keep an
entry queued. Multiplication zeroes total risk whenever one axis is clean;
lexicographic ordering lets one axis dominate regardless of severity elsewhere;
unequal weights are unearned until you have outcome data (triage rank vs. later
verification failures) — if you add weights, log it as V3 and stop comparing
scores across versions.

**Tiebreak 1**: load-bearingness — count of OTHER LD/SY/CDS entries whose body
contains this entry's ID (VT/DS mentions don't count). Higher first.
**Tiebreak 2**: lexicographic entry ID.

**Recency note** (a common first question): S has no time term anywhere. Your
newest entry ranking top is CORRECT — it ranks high because it is unverified
(`last_verified: never` → S=2), not because it is new. Age neither protects nor
penalizes.

## Worked example (a real entry, abridged)

Entry LD-002 with evidence lines:
```
- Bedrock SAE mechanics (...) — [corpus recollection, high-consensus material]
- Auto-interp critique literature — [corpus recollection, specifics unread]
- Discovery pathway (...) — [READ 2026-07-21; confirmed ...]
last_verified: 2026-07-21 (VT-004, pre-entry — ...)
```
Checker reports: `LD-002: T2 — corpus-recollection evidence while cited elsewhere`.
No VT names LD-002. The only gap-DS names a different entry. No PT string, no SLIP.

- S: T2 finding present (not S=0); ≥1 READ line → **S=1**.
- T: UNREAD lines present → SR false; last_verified's event is annotated
  `pre-entry` → excluded → BV false → **T=2**.
- G: GT false → at least 1; PT and SLIP false → **G=1**.
- **Risk = 4.**

This example was reproduced exactly (1/2/1 = 4, same derivations) by a
context-blind scorer given only this rubric, the entry, and the checker line.

## Procedure

Run the checker → score every entry → emit the FULL ranked list with one-sentence
rationales → the head is the next session's default opener → log the ranking in
the decisions file under "Triage runs." Change the rubric only by editing this
file, and version it when you do.
