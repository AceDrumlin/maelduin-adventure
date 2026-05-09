"""Patch _shared.py to add visible_if conditions to specific NPCs.
Tracks parenthesis depth to find the exact closing paren of each NPC constructor."""
import re

FILE = "game/levels/_shared.py"

with open(FILE) as f:
    text = f.read()

lines = text.split("\n")

# Find NPC definition boundaries by tracking parenthesis depth
npc_blocks = {}  # npc_name -> (start_line, end_line)

i = 0
while i < len(lines):
    line = lines[i]
    m = re.match(r'(\s*)n\["([^"]+)"\]\s*=\s*NPC\(', line)
    if m:
        npc_name = m.group(2)
        depth = line.count("(") - line.count(")")
        start_line = i
        j = i + 1
        while j < len(lines) and depth > 0:
            depth += lines[j].count("(") - lines[j].count(")")
            j += 1
        # j is now past the closing paren
        end_line = j - 1  # line with the closing )
        npc_blocks[npc_name] = (start_line, end_line)
        i = j
    else:
        i += 1

# Define visible_if conditions per NPC ID  
VISIBLE_IF = {
    "ailill": "lambda s: not s.has_flag('witnessed_death')",
    "mother": "lambda s: not s.has_flag('witnessed_death')",
    "beach_mother": "lambda s: s.has_flag('witnessed_death')",
    "young_conganchnes": "lambda s: not s.has_flag('recruited_young_conganchnes')",
    "young_fergus": "lambda s: not s.has_flag('recruited_young_fergus')",
    "young_diuran": "lambda s: not s.has_flag('recruited_young_diuran')",
    "giant": "lambda s: not (s.has_flag('giant_defeated') or s.has_flag('giant_mollified'))",
    "treasure_serpent": "lambda s: not s.has_flag('serpent_passed')",
    "great_hound": "lambda s: not s.has_flag('dog_pacified')",
    "mountain_lion": "lambda s: not (s.has_flag('lion_fought') or s.has_flag('lion_pacified'))",
    "black_pig": "lambda s: not s.has_flag('pig_pacified')",
    "serpent": "lambda s: not s.has_flag('serpent_calmed')",
}

# Build new file content
new_lines = []
modified = set()

for i, line in enumerate(lines):
    # Check if current line is the closing paren of an NPC we want to modify
    for npc_name, (start_line, end_line) in npc_blocks.items():
        if i == end_line and npc_name in VISIBLE_IF:
            # This is the closing paren - insert visible_if before it
            indent = "        "  # 8 spaces, matching the param indent
            new_lines.append(f"{indent}visible_if={VISIBLE_IF[npc_name]},")
            modified.add(npc_name)
            break
    new_lines.append(line)

new_text = "\n".join(new_lines)

with open(FILE, "w") as f:
    f.write(new_text)

print(f"Patched {len(modified)} NPCs: {', '.join(sorted(modified))}")
print(f"Expected {len(VISIBLE_IF)}: {', '.join(sorted(VISIBLE_IF.keys()))}")
if set(VISIBLE_IF.keys()) != modified:
    missing = set(VISIBLE_IF.keys()) - modified
    print(f"MISSING: {missing}")
