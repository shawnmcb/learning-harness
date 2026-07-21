# Cold Start — Day One Protocol

Eight steps, in order. Inputs and outputs per step. Steps 1–3 are today; step 4 is
deliberately NOT today.

1. **Write your `LEARNING_SPEC.md`** (copy from `templates/`).
   In: a domain you're actively learning. Out: 3–5 sub-areas, each with ~4
   "understanding = being able to answer/do X" questions, plus a three-tier
   source-quality table (authoritative / expert-informal / speculative). Add the
   corpus-knowledge rule: your own recollection — or your AI assistant's — is
   ~tier-B evidence at best, and nothing logs at ≥80% confidence without a
   primary-source read.

2. **Log your first LD entry** in `LEARNING_DECISIONS.md` from your best current
   belief. In: one claim you think you know. Out: an entry with all six fields —
   claim, evidence lines *each carrying a provenance tag* (`[READ <date>]` or
   `corpus recollection`), confidence %, would-change-my-mind conditions,
   `last_verified`, `decay_trigger`. Do not flatter provenance: if you didn't read
   the source today, it's recollection.

3. **Run the checker**: `python3 check_staleness.py <path>/LEARNING_DECISIONS.md`.
   Out: findings. Expect a T2 or T3 finding on day one — a brand-new log SHOULD
   report "unverified, recollection-based." That is the system working.

4. **(Next session — not today.) Run your first blind verification (VT).**
   Hand ONLY the claim text to an uninvolved person or AI instance (no other
   context). They log a numbered answer key first — each item in the form "the
   claim's wrong neighbor asserts P; actually ¬P, because Q." They present the
   planted misconception; you write your rebuttal as numbered flaw-points (F1,
   F2, …) and commit it BEFORE any reveal. Log the VT with the three booleans
   (caught-exact, steelman-novel, rebuttal-cites-discriminator) and the marker
   `protocol: hardened-v1.1`. Why not today: same-session verification measures
   short-term recall, not retention, and a steelman built from your study session
   is one you're primed to catch.

5. **Log a DS (durability signal) on that VT.** signal_type `resistance` or `gap`;
   answer all three questions: what the catch/slip proves about how the knowledge
   is stored; which mechanism produced it; what would have made the opposite
   outcome happen.

6. **Score every entry with the triage rubric** (`TRIAGE-RUBRIC.md`). Out: the
   full ranked list. The head of the queue is your next action — not your
   preference, the queue's.

7. **Execute the queue head.** A source read clears T2 findings (retag evidence
   lines `[READ <date>]`, adjust confidence with a stated reason); a gauntlet
   clears gap exposure; log every event and re-run the checker.

8. **Loop 3→7 each cycle.** Add an SY entry when two entries in one sub-area
   connect; a CDS entry when two sub-areas do (and log its intersection-
   misconception as a pending target). Escalate gauntlets when rounds come back
   clean: self-play → your least-verified sub-area → source-grounded (grader
   reads a primary source you haven't and plants claims against its text).

**Pass test for this protocol**: after one full cycle your log contains the same
entry types and fields as the template — if it doesn't, the protocol failed, not
you; report it (see `KILL-CONDITIONS.md`, K2).
