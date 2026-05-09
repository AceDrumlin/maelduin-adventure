#!/usr/bin/env python3
"""Debug garbh insertion."""
path = "/home/ace/maelduin-adventure/game/levels/_shared.py"
with open(path, "r") as f:
    lines = f.readlines()

target_key = '            "father": (\n'
print(f"Target key repr: {repr(target_key)}")

for i, line in enumerate(lines):
    if line == target_key:
        context = ''.join(lines[max(0,i-5):i])
        has_garbh = 'Garbh' in context
        has_garbh_lower = 'garbh' in context.lower()
        print(f"Line {i}: found 'father' key. Context has 'Garbh': {has_garbh}, 'garbh': {has_garbh_lower}")
        print(f"  Context lines {i-5}-{i-1}:")
        for j in range(max(0,i-5), i):
            print(f"    {j}: {repr(lines[j][:60])}")
        print()

# Find garbh's father key by looking at next line content
for i, line in enumerate(lines):
    if i > 1410 and line == target_key:
        next_line = lines[i+1] if i+1 < len(lines) else ""
        print(f"Line {i}: next line starts: {repr(next_line[:60])}")
