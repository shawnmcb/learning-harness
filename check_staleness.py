#!/usr/bin/env python3
"""Staleness checker for LEARNING_DECISIONS.md (mechanical triggers only).

Usage: python3 check_staleness.py [path/to/LEARNING_DECISIONS.md]
       (default: ./LEARNING_DECISIONS.md next to this script)

Parses LD-*/SY-*/CDS-* entries and evaluates the event-driven triggers that are
mechanically decidable:
  T2  recollection-tagged evidence on an entry that other entries reference
  T3  last_verified is 'never'/missing, cites an ID with no parsed VT/VB event
      block (mention-only, typo, or fabricated), or cites only non-probative
      events; event blocks are bullets, blockquoted bullets, or ##/### headings
  missing-fields  entry lacking last_verified or decay_trigger
Plus a VT protocol lint: events marked `protocol: hardened-v1.1` must carry all
required elements; unmarked events are reported as legacy.

T1 (superseded/contradicted) and T5 (spec-shift) need semantic judgment and are
listed as judgment items for the caller. T4 (recall-failure) is an in-session
event, not a log property.

Exit 0 always; output is the report. Not a gate — a surfacing tool.
"""
import re, sys, pathlib

LOG = (pathlib.Path(sys.argv[1]) if len(sys.argv) > 1
       else pathlib.Path(__file__).parent / "LEARNING_DECISIONS.md")
if not LOG.exists():
    print(f"check_staleness: no log found at {LOG}")
    sys.exit(0)
text = LOG.read_text(encoding="utf-8")
# HTML comments are documentation, not log content — template skeletons and
# user notes must never register as entries, events, or citations
text = re.sub(r"<!--.*?-->", "", text, flags=re.S)

# entries: "## LD-001 — title (date)", "## SY-001 — ...", "## CDS-001 — ...";
# a body ends at the NEXT heading of any depth 2–3, so heading-style event
# blocks are never swallowed into the preceding entry
entries = {}
for m in re.finditer(r"^## ((?:LD|SY|CDS)-\d+) — (.+)$", text, re.M):
    start = m.start()
    nxt = re.search(r"^#{2,3} ", text[m.end():], re.M)
    end = m.end() + (nxt.start() if nxt else len(text) - m.end())
    entries[m.group(1)] = {"title": m.group(2).strip(), "body": text[start:end]}

# ---- VT/VB event blocks, parsed FIRST: bullets, blockquoted bullets, headings.
# Everything downstream (existence, non-probative status, protocol lint) derives
# from these parsed blocks — a bare mention of an ID is never an event.
event_bodies = {}
for pat in (
    r"^(?:>\s*)?[-*] \*\*((?:VT|VB)-\d+)([^\n]*\*\*.*?)(?=^(?:>\s*)?[-*] \*\*|^#{2,3} |\Z)",
    r"^#{2,3} ((?:VT|VB)-\d+)([^\n]*\n.*?)(?=^#{2,3} |^(?:>\s*)?[-*] \*\*|\Z)",
):
    for vid, body in re.findall(pat, text, re.M | re.S):
        event_bodies[vid] = event_bodies.get(vid, "") + body
existing_events = set(event_bodies)

# non-probative: marked inside the event's own block, or stated on any single
# line naming the ID (crosses sentence punctuation; a line-level approximation)
nonprobative = {v for v, b in event_bodies.items() if "non-probative" in b.lower()}
for line in text.splitlines():
    if "non-probative" in line.lower():
        nonprobative.update(re.findall(r"\b((?:VT|VB)-\d+)\b", line))

# provenance regexes — single source of truth, matching TRIAGE-RUBRIC.md's
# READ/UNREAD definitions exactly
UNREAD_RE = re.compile(r"corpus recollection|\brecalled\b|derived this cycle", re.I)
READ_RE = re.compile(r"\[READ\s", re.I)

findings, judgment = [], []
for eid, e in sorted(entries.items()):
    b = e["body"]
    lv = re.search(r"`last_verified`:\s*(.+)", b)
    dt = re.search(r"`decay_trigger`:\s*(.+)", b)
    if not lv or not dt:
        findings.append(f"{eid}: MISSING-FIELDS — needs last_verified and/or decay_trigger")
        continue
    lv_val = lv.group(1).strip()
    # T3: never verified, verified only by a non-probative event, or the cited
    # event ID does not exist anywhere in the log (typo / fabricated reference)
    ver_ids = set(re.findall(r"(VT-\d+|VB-\d+)", lv_val))
    phantom = ver_ids - existing_events
    if lv_val.lower().startswith("never") or not ver_ids:
        findings.append(f"{eid}: T3 — no valid verification event on record")
    elif phantom:
        findings.append(f"{eid}: T3 — last_verified cites nonexistent event(s): "
                        + ", ".join(sorted(phantom)))
    elif ver_ids <= nonprobative:
        findings.append(f"{eid}: T3 — last verification is marked non-probative")
    # T2: UNREAD-tagged evidence + cited by another LD/SY/CDS entry or an
    # explicit outward-work marker. Being a VT's *target* is not a citation.
    if UNREAD_RE.search(b):
        refs = [o for o in entries if o != eid and eid in entries[o]["body"]]
        cited_elsewhere = bool(refs) or "cited-outward" in b.lower()
        if cited_elsewhere:
            findings.append(f"{eid}: T2 — UNREAD-tagged evidence while cited elsewhere; "
                            f"clears on primary-source re-read")
    judgment.append(f"{eid}: judge T1 (superseded/contradicted by newer entry or source?) "
                    f"and T5 (spec sub-area rewritten since {lv_val.split('(')[0].strip()}?)")

# ---- VT protocol lint (hardened-v1.1) ----
# VT events carrying the marker must contain all hardened-protocol elements;
# events without the marker are legacy (pre-hardening) and reported as such.
VT_REQUIRED = [
    ("numbered answer key", r"answer key|numbered key"),
    ("structured rebuttal (F-numbers)", r"\bF\d+\b"),
    ("caught-exact boolean", r"caught-exact"),
    ("steelman-novel boolean", r"steelman-novel"),
    ("discriminator boolean", r"discriminator"),
]
# lint runs over the same parsed event blocks (VT only)
vt_blocks = [(v, b) for v, b in event_bodies.items() if v.startswith("VT-")]
vt_findings, legacy = [], []
for vid, body in vt_blocks:
    if "protocol: hardened" in body.lower():
        missing = [name for name, pat in VT_REQUIRED
                   if not re.search(pat, body, re.I)]
        if missing:
            vt_findings.append(f"{vid}: NON-COMPLIANT with hardened-v1.1 — missing: "
                               + ", ".join(missing))
    else:
        legacy.append(vid)

print(f"check_staleness: {len(entries)} LD/SY entries scanned "
      f"({', '.join(entries) if entries else 'none'})")
print()
if findings:
    print("MECHANICAL FINDINGS (stale until cleared):")
    for f in findings: print(f"  - {f}")
else:
    print("MECHANICAL FINDINGS: none — all entries carry fields and valid verification.")
print()
print("JUDGMENT ITEMS (for /check-staleness caller — T1/T5 are semantic):")
for j in judgment: print(f"  - {j}")
print()
print(f"VT PROTOCOL LINT (hardened-v1.1): {len(vt_blocks)} VT events scanned")
if vt_findings:
    for f in vt_findings: print(f"  - {f}")
else:
    print("  - no non-compliant hardened-protocol events")
if legacy:
    print(f"  - legacy (pre-hardening, grandfathered): {', '.join(legacy)}")
