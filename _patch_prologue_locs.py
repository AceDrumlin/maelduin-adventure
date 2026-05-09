"""Patch level_prologue.py to add state-aware descriptions to ALL prologue locations."""
import re

FILE = "game/levels/level_prologue.py"

with open(FILE) as f:
    text = f.read()

lines = text.split("\n")

# Find Location definitions by tracking Location( blocks
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

print("Location blocks found:")
for loc_id, (start, end) in sorted(loc_blocks.items()):
    print(f"  {loc_id}: lines {start+1}-{end+1}")

# For each prologue location, add a describe function
# We'll insert describe functions just before the Location constructor call

describe_fns = {}

# Beach description
describe_fns["ailill_beach"] = '''
    def _beach_describe(state):
        """Beach changes after death is witnessed."""
        # After the player has gone forward in time, the beach is empty
        if state.has_flag("time_passed") or state.has_flag("childhood_seen"):
            return (
                "The Strand — Empty Shore",
                "The tide rises and falls on a beach that remembers nothing. The sand is smooth and untroubled. "
                "The grey sea stretches to the horizon. Whatever happened here has been washed away by time.\\n\\n"
                "Ailill Ochair Ága lies somewhere beneath the waves, his bones picked clean by fish. "
                "The Wolf of the Arans is part of the sea now.\\n\\n"
                "There is nothing left to see here. Only the wind and the gulls and the endless water.\\n\\n"
                "(Type ONWARD to continue.)"
            )
        if state.has_flag("witnessed_death"):
            return None  # Use default description (still fresh)
        return None
'''

# Foster village description
describe_fns["foster_village"] = '''
    def _foster_describe(state):
        """Foster village after time has moved on."""
        if state.has_flag("childhood_seen") and state.has_flag("training_seen"):
            return (
                "The Foster Village — Memory",
                "The village is quiet now. The children who played here have grown. The goats that wandered the lanes "
                "are gone — eaten, or sold, or wandered off themselves.\\n\\n"
                "An old woman sits in the doorway of a stone hut, weaving. She looks up as you pass and her eyes "
                "widen. She remembers you. She remembers the child who stared at the sea.\\n\\n"
                '\"You went, then,\" she says. \"We all knew you would. The sea always calls its own.\"\\n\\n'
                "The village feels smaller than you remember. Or perhaps you are bigger."
            )
        if state.has_flag("childhood_seen"):
            return (
                "The Foster Village — Years Later",
                "The village is much the same, but you are not. The stones are the same stones. The goats are "
                "different goats. A new dog sleeps in the sun — the old one has passed.\\n\\n"
                "Your foster mother's hut stands empty. She is at the training field today, watching the young men "
                "practice.\\n\\n"
                "A familiar DRUID sits by a fire, stirring his eternal pot. He nods as you pass. "
                "He is patient. He knows you will come to him when you are ready."
            )
        return None
'''

# Training field description
describe_fns["training_field"] = '''
    def _training_describe(state):
        """Training field after companions are recruited or time passes."""
        has_conganchnes = state.has_flag("recruited_young_conganchnes")
        has_fergus = state.has_flag("recruited_young_fergus")
        has_diuran = state.has_flag("recruited_young_diuran")
        all_gone = has_conganchnes and has_fergus and has_diuran
        
        if state.has_flag("training_seen") and all_gone:
            return (
                "The Training Field — Empty",
                "The training field is quiet now. Wooden swords lie scattered on the grass, slowly rotting. "
                "The sea wind has scattered the practice dummies.\\n\\n"
                "Your companions are gone — sailed away with you on the great adventure. "
                "Only the ghosts of old training sessions remain. You can almost hear Conganchnes laughing "
                "as he knocks the sword from your hand one more time.\\n\\n"
                "Your foster mother no longer comes to watch. She has said her goodbyes.\\n\\n"
                "The field feels like a memory of a life you used to live."
            )
        if state.has_flag("training_seen") and has_conganchnes:
            return (
                "The Training Field — One Friend Gone",
                "The training field feels emptier without Conganchnes. His absence is a hole in the air — "
                "the space where his laughter used to be.\\n\\n"
                "Fergus sits on a rock, studying star charts. Diurán writes poetry under a tree. "
                "Your foster mother watches from the edge, her face unreadable.\\n\\n"
                "The sea glitters in the distance, waiting."
            )
        return None
'''

# Feast hall description
describe_fns["feast_hall"] = '''
    def _feast_describe(state):
        """Feast hall after the taunting and recruitment."""
        if state.has_flag("taunting_seen") and state.has_flag("learned_truth"):
            return (
                "The Feast Hall — After the Truth",
                "The hall is empty now. The fire has burned low, and the benches are cold. "
                "The laughter that filled this room seems like a distant echo.\\n\\n"
                "Lorcán is gone — slunk away to nurse his hangover and his wounded pride. "
                "Your companions are gathering their things, ready to follow you to the ends of the earth.\\n\\n"
                "The truth has been spoken. The air is different now. It smells of salt and destiny.\\n\\n"
                "The druid's sanctuary lies to the NORTH. Your future awaits."
            )
        if state.has_flag("taunting_seen"):
            return (
                "The Feast Hall — After the Taunt",
                "The hall is silent. Everyone is staring at you. Lorcán's words hang in the air like smoke.\\n\\n"
                "\"The bastard of Inishmore.\" The words echo in your skull. Your father was not a fisherman. "
                "He was Ailill Ochair Ága, the Wolf of the Arans, and he was murdered.\\n\\n"
                "Your friends are watching you, waiting to see what you will do.\\n\\n"
                "The druid's sanctuary is to the NORTH. He will have the full truth."
            )
        return None
'''

# Druid sanctuary description
describe_fns["druid_sanctuary"] = '''
    def _druid_describe(state):
        """Druid sanctuary changes after truth is learned."""
        if state.has_flag("learned_truth") and state.has_flag("set_sail"):
            return (
                "The Druid's Sanctuary — Return",
                "The grove is quiet. The fire has burned to embers. The druid's pot sits cold and untouched.\\n\\n"
                "The druid is gone — perhaps to the harbor to see you off, perhaps somewhere else entirely. "
                "Druids come and go like the wind.\\n\\n"
                "The magic thread is with you now, tied to your mast, pulling you toward your destiny.\\n\\n"
                "There is nothing left for you here. The sea is waiting."
            )
        if state.has_flag("learned_truth"):
            return None  # Original description already has the truth revealed
        return None
'''

# Harbor description
describe_fns["village_harbor"] = '''
    def _harbor_describe(state):
        """Harbor changes after sailing."""
        if state.has_flag("set_sail"):
            return (
                "The Harbor — After Departure",
                "The beach where your curragh lay is empty now. The tide has erased the marks where "
                "the hull rested. Footprints lead nowhere.\\n\\n"
                "Your foster mother stands alone on the sand, watching the horizon. She does not turn "
                "when you approach. She knew you would not stay.\\n\\n"
                '"The sea takes what it wants," she says, her voice carried away by the wind. '
                '"Be sure it gives you back."\\n\\n'
                "The harbor is a place of farewells. You have made yours."
            )
        return None
'''

# Now insert these functions and add describe= to each Location

# Strategy: For each location, find its Location( constructor call and the next )
# Insert the describe function BEFORE the constructor call
# Insert describe=_fn_name, inside the constructor

# Let's work backwards from the last location to avoid line number shifts

# For each location in reverse order:
# 1. Find the last ) that closes the Location constructor
# 2. Add the describe=_fn_name line before it

insertions = []  # (line_number, text_to_insert)

for loc_id, (start_line, end_line) in sorted(loc_blocks.items(), key=lambda x: -x[1][1]):
    if loc_id not in describe_fns:
        continue
    
    fn_code = describe_fns[loc_id]
    fn_name_match = re.search(r'def (\w+)\(state\)', fn_code)
    if not fn_name_match:
        continue
    fn_name = fn_name_match.group(1)
    
    # Find where to insert the function (before the Location constructor)
    insert_line = start_line  # Insert function before this line
    
    # Build the insert text: function + describe= param
    fn_text = fn_code.strip()
    describe_param = f"        describe={fn_name},"
    
    # Check if the last line before closing ) has an empty/whitespace line
    # Find the actual closing ) line
    close_line = end_line
    closing_line_text = lines[close_line]
    
    # The closing paren is the last line. Insert describe= before it.
    # Insert the function definition right before the l["loc_id"] = Location( line
    # and the describe= param right before the closing )
    
    insertions.append((insert_line, fn_text + "\n\n"))
    
    # Insert describe= before the closing )
    # Find indent of other params
    param_indent = "        "  # 8 spaces
    insertions.append((close_line, f"{param_indent}describe={fn_name},\n"))

# Apply insertions from bottom to top
for line_no, insert_text in sorted(insertions, key=lambda x: -x[0]):
    print(f"Inserting at line {line_no+1}: {insert_text[:60]}...")
    lines.insert(line_no, insert_text)

new_text = "\n".join(lines)
with open(FILE, "w") as f:
    f.write(new_text)

print(f"\nPatched {len(describe_fns)} locations with describe functions!")
print(f"Prologue locations: {', '.join(describe_fns.keys())}")
