"""Fix describe= params to use fn name without calling them."""
import re

FILE = "game/levels/level_prologue.py"

with open(FILE) as f:
    text = f.read()

# Fix: describe=_beach_describe(state), → describe=_beach_describe,
text = re.sub(r'describe=(\w+)\(state\),', r'describe=\1,', text)

with open(FILE, "w") as f:
    f.write(text)

print("Fixed describe params!")
