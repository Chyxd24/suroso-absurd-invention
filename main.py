"""One-Sentence Absurd Invention Pitch

Writes one line to /output/entry.txt. Stdlib only, deterministic.
"""
import os

ENTRY = "An alarm clock that apologises for existing before it rings, then quietly reschedules itself to a time you'll actually forgive it for. It also sends a formal apology email to whoever else is in the room."

assert 1 <= len(ENTRY) <= 220, len(ENTRY)
p = "/output/entry.txt"
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
with open(p, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == ENTRY, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")
