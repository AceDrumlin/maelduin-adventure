"""Patch level_prologue.py to add state-aware describe functions.
Each describe function must be indented 4 spaces (inside register()),
and returns (new_name, new_description) tuple or None."""
import re

FILE = "game/levels/level_prologue.py"

with open(FILE) as f:
    text = f.read()

lines = text.split("\n")

# Describe functions as lists of properly-indented lines
# Each function is: indent + "def fn_name(state):"
# Body: indent + " " + body content
INDENT = "    "  # 4 spaces - inside register()

DESCRIBE_FNS = {
    "ailill_beach": [
        f'{INDENT}def _beach_describe(state):',
        f'{INDENT}    """Beach changes after death is witnessed."""',
        f'{INDENT}    if state.has_flag("time_passed") or state.has_flag("childhood_seen"):',
        f'{INDENT}        return (',
        f'{INDENT}            "The Strand — Empty Shore",',
        f'{INDENT}            "The tide rises and falls on a beach that remembers nothing. The sand is smooth and untroubled. "',
        f'{INDENT}            "The grey sea stretches to the horizon. Whatever happened here has been washed away by time.\\n\\n"',
        f'{INDENT}            "Ailill Ochair Ága lies somewhere beneath the waves, his bones picked clean by fish. "',
        f'{INDENT}            "The Wolf of the Arans is part of the sea now.\\n\\n"',
        f'{INDENT}            "There is nothing left to see here. Only the wind and the gulls and the endless water.\\n\\n"',
        f'{INDENT}            "(Type ONWARD to continue.)"',
        f'{INDENT}        )',
        f'{INDENT}    return None',
    ],
    "foster_village": [
        f'{INDENT}def _foster_describe(state):',
        f'{INDENT}    """Foster village after time has moved on."""',
        f'{INDENT}    if state.has_flag("childhood_seen") and state.has_flag("training_seen"):',
        f'{INDENT}        return (',
        f'{INDENT}            "The Foster Village — Empty Nest",',
        f'{INDENT}            "The village is quiet now. The children who played here have grown. The goats that wandered the lanes "',
        f'{INDENT}            "are gone. An old woman sits in a doorway, weaving. She looks up as you pass, and her eyes widen.\\n\\n"',
        f'{INDENT}            "\'You went, then.\' She nods. \'We all knew you would. The sea always calls its own.\'\\n\\n"',
        f'{INDENT}            "The village feels smaller than you remember. Or perhaps you are bigger."',
        f'{INDENT}        )',
        f'{INDENT}    if state.has_flag("childhood_seen"):',
        f'{INDENT}        return (',
        f'{INDENT}            "The Foster Village — Years Later",',
        f'{INDENT}            "The village is much the same, but you are not. The stones are the same stones. The goats are "',
        f'{INDENT}            "different goats. A familiar DRUID sits by a fire, stirring his eternal pot. He nods as you pass.\\n\\n"',
        f'{INDENT}            "He is patient. He knows you will come to him when you are ready."',
        f'{INDENT}        )',
        f'{INDENT}    return None',
    ],
    "training_field": [
        f'{INDENT}def _training_describe(state):',
        f'{INDENT}    """Training field after companions are recruited."""',
        f'{INDENT}    has_conganchnes = state.has_flag("recruited_young_conganchnes")',
        f'{INDENT}    has_fergus = state.has_flag("recruited_young_fergus")',
        f'{INDENT}    has_diuran = state.has_flag("recruited_young_diuran")',
        f'{INDENT}    all_gone = has_conganchnes and has_fergus and has_diuran',
        f'{INDENT}    if state.has_flag("training_seen") and all_gone:',
        f'{INDENT}        return (',
        f'{INDENT}            "The Training Field — Empty",',
        f'{INDENT}            "The training field is quiet now. Wooden swords lie scattered on the grass, slowly rotting. "',
        f'{INDENT}            "Your companions are gone. Only the ghosts of old training sessions remain.\\n\\n"',
        f'{INDENT}            "Your foster mother no longer comes to watch. She has said her goodbyes.\\n\\n"',
        f'{INDENT}            "The field feels like a memory of a life you used to live."',
        f'{INDENT}        )',
        f'{INDENT}    if state.has_flag("training_seen") and has_conganchnes:',
        f'{INDENT}        return (',
        f'{INDENT}            "The Training Field — One Friend Gone",',
        f'{INDENT}            "The training field feels emptier without Conganchnes. His absence is a hole in the air.\\n\\n"',
        f'{INDENT}            "Fergus studies star charts. Diurán writes poetry. Your foster mother watches from the edge.\\n\\n"',
        f'{INDENT}            "The sea glitters in the distance, waiting."',
        f'{INDENT}        )',
        f'{INDENT}    return None',
    ],
    "feast_hall": [
        f'{INDENT}def _feast_describe(state):',
        f'{INDENT}    """Feast hall after the taunting and recruitment."""',
        f'{INDENT}    if state.has_flag("taunting_seen") and state.has_flag("learned_truth"):',
        f'{INDENT}        return (',
        f'{INDENT}            "The Feast Hall — After the Truth",',
        f'{INDENT}            "The hall is empty now. The fire has burned low, and the benches are cold. "',
        f'{INDENT}            "Lorcán is gone. Your companions are gathering their things.\\n\\n"',
        f'{INDENT}            "The truth has been spoken. The air smells of salt and destiny.\\n\\n"',
        f'{INDENT}            "The druid\'s sanctuary lies to the NORTH."',
        f'{INDENT}        )',
        f'{INDENT}    if state.has_flag("taunting_seen"):',
        f'{INDENT}        return (',
        f'{INDENT}            "The Feast Hall — After the Taunt",',
        f'{INDENT}            "Lorcán\'s words hang in the air like smoke. \'The bastard of Inishmore.\'\\n\\n"',
        f'{INDENT}            "Your father was Ailill Ochair Ága, the Wolf of the Arans, and he was murdered.\\n\\n"',
        f'{INDENT}            "The druid\'s sanctuary is to the NORTH. He will have the full truth."',
        f'{INDENT}        )',
        f'{INDENT}    return None',
    ],
    "druid_sanctuary": [
        f'{INDENT}def _druid_describe(state):',
        f'{INDENT}    """Druid sanctuary changes after truth is learned."""',
        f'{INDENT}    if state.has_flag("learned_truth") and state.has_flag("set_sail"):',
        f'{INDENT}        return (',
        f'{INDENT}            "The Druid\'s Sanctuary — Return",',
        f'{INDENT}            "The grove is quiet. The fire has burned to embers. The druid is gone.\\n\\n"',
        f'{INDENT}            "The magic thread is with you. The sea is waiting.\\n\\n"',
        f'{INDENT}            "There is nothing left for you here."',
        f'{INDENT}        )',
        f'{INDENT}    return None',
    ],
    "village_harbor": [
        f'{INDENT}def _harbor_describe(state):',
        f'{INDENT}    """Harbor changes after sailing."""',
        f'{INDENT}    if state.has_flag("set_sail"):',
        f'{INDENT}        return (',
        f'{INDENT}            "The Harbor — After Departure",',
        f'{INDENT}            "The beach where your curragh lay is empty now. The tide has erased the marks.\\n\\n"',
        f'{INDENT}            "Your foster mother stands alone on the sand, watching the horizon.\\n\\n"',
        f'{INDENT}            "\'The sea takes what it wants,\' she says. \'Be sure it gives you back.\'\\n\\n"',
        f'{INDENT}            "The harbor is a place of farewells. You have made yours."',
        f'{INDENT}        )',
        f'{INDENT}    return None',
    ],
}

# Find Location definitions
loc_blocks = {}  # loc_id -> (start_line, end_line)
i = 0
while i < len(lines):
    line = lines[i]
    m = re.match(r'\s*l\["([^"]+)"\]\s*=\s*Location\(', line)
    if m:
        loc_id = m.group(1)
        depth = line.count("(") - line.count(")")
        start_line = i
        j = i + 1
        while j < len(lines) and depth > 0:
            depth += lines[j].count("(") - lines[j].count(")")
            j += 1
        end_line = j - 1
        loc_blocks[loc_id] = (start_line, end_line)
        i = j
    else:
        i += 1

# Collect insertions: (insert_line_no, text)
insertions = []

for loc_id in DESCRIBE_FNS:
    if loc_id not in loc_blocks:
        print(f"WARNING: {loc_id} not found in location blocks!")
        continue
    
    start_line, end_line = loc_blocks[loc_id]
    fn_lines = DESCRIBE_FNS[loc_id]
    fn_name = fn_lines[0].strip().split()[1][:-1]  # Extract "fn_name" from "def fn_name(state):"
    
    # Insert function definition before the Location constructor
    fn_text = "\n".join(fn_lines)
    insertions.append((start_line, fn_text + "\n"))
    
    # Insert describe= param before the closing )
    # Find the closing paren line and add describe= before it
    close_line = end_line
    # Use same indent as other params 
    param_indent = " " * 8
    insertions.append((close_line, f"{param_indent}describe={fn_name},\n"))

# Apply from bottom to top
for line_no, insert_text in sorted(insertions, key=lambda x: -x[0]):
    print(f"Insert {len(insert_text)} chars at line {line_no+1}")
    lines.insert(line_no, insert_text)

new_text = "\n".join(lines)
with open(FILE, "w") as f:
    f.write(new_text)

print(f"\nPatched {len(DESCRIBE_FNS)} locations!")
for loc_id in DESCRIBE_FNS:
    print(f"  + {loc_id}: {DESCRIBE_FNS[loc_id][0].strip()}")
