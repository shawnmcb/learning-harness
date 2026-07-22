---
name: learning-harness
description: Run the learning-harness cycle — triage-ranked study queue, planted-misconception verification with blind grading, event-driven staleness checking, and durability logging over flat-file LEARNING_SPEC.md / LEARNING_DECISIONS.md. Modes mirror the docs — triage, verify, benchmark, check-staleness, cold-start.
argument-hint: "[cold-start | triage | verify <entry-id> | benchmark <sub-area> | check-staleness | status]"
test-contract:
  triggers:
    - "run my learning triage"
    - "which learning entry should I work on next"
    - "verify LD-001 with a planted misconception"
    - "check my decisions log for stale entries"
    - "cold-start the learning harness for a new domain"
  anti-triggers:
    - "research this topic and write a report"
    - "explain this concept to me"
    - "review this code"
---

# Learning Harness — Claude Code entrypoint

This skill is an OPTIONAL adapter: the harness is deliberately tool-agnostic and
fully operable by a human following the docs. When run from Claude Code, the
assistant executes the same protocols — it does not replace them.

Canonical references (read the relevant one before acting; do not restate rules
from memory):
- `COLD-START.md` — day-one sequence (mode: `cold-start`)
- `TRIAGE-RUBRIC.md` — V2 scoring; string tests only (mode: `triage`)
- `PROTOCOLS.md` — entry types, T1–T5 staleness, VT/VB/DS protocols incl.
  `hardened-v1.1` (modes: `verify`, `benchmark`)
- `KILL-CONDITIONS.md` — pre-registered falsification; consult before proposing
  any redesign
- `check_staleness.py` — run for mode `check-staleness`:
  `python3 check_staleness.py <path>/LEARNING_DECISIONS.md`

## Mode behavior

- **cold-start**: walk the 8 steps of COLD-START.md interactively; copy templates;
  refuse to pre-fill provenance tags optimistically.
- **triage**: run the checker, score every LD/SY/CDS by the rubric's string tests,
  emit the FULL ranked list with one-sentence rationales, and log the run. Never
  score from memory of the entries — read them.
- **verify `<entry-id>`**: run the blind VT protocol. The steelman generator must
  be a fresh agent given ONLY the claim text (grader-independence rules bind);
  the user's (or learner-agent's) rebuttal is committed before any reveal; grade
  with the three booleans; log with `protocol: hardened-v1.1`.
- **benchmark `<sub-area>`**: define the VB entry (exercise + 2–4
  recording-adjudicable criteria) BEFORE the attempt; grade only from the
  recording.
- **check-staleness**: run the script; apply judgment to the T1/T5 items it
  lists; report stale entries with the specific event that clears each.
- **status**: per-sub-area coverage, entries pending verification, current queue
  head.

## Human-in-the-loop tiers

- Automatic (no confirmation): running the checker, computing triage scores,
  drafting entries for review.
- Confirm before writing: appending any entry to LEARNING_DECISIONS.md (the log
  is append-only and permanent).
- Never automatic: grading your own rebuttal (grader independence), marking a
  kill condition triggered, changing the rubric (version bump required).

## Quality gates

- No entry logs without all required fields (the PRIMITIVES.md instantiation
  test for its type).
- No VT logs without passing the protocol lint (`check_staleness.py` reports it).
- No confidence ≥80% over evidence lines still tagged UNREAD (corpus-knowledge
  rule).
