"""One-Sentence Absurd Invention Pitch

Writes one line to /output/entry.txt. Stdlib only, deterministic.
"""
import os

ENTRY = "A sock that files a formal complaint with the washing machine every time it loses its pair - and the machine has to respond in writing by Friday."

assert 1 <= len(ENTRY) <= 220, len(ENTRY)
p = "/output/entry.txt"
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
with open(p, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == ENTRY, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")
