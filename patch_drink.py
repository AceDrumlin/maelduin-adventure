import sys
sys.path.insert(0, '/home/ace/maelduin-adventure')

# Add handle_drink and VERBS entry
with open('/home/ace/maelduin-adventure/game/engine.py', 'r') as f:
    content = f.read()

# 1. Add "drink" to VERBS after "crew"
old_verbs = '    "crew": ("crew", handle_crew),\n    "score":'
new_verbs = '    "crew": ("crew", handle_crew),\n    "drink": ("drink", handle_drink),\n    "score":'
content = content.replace(old_verbs, new_verbs, 1)

# 2. Add handle_drink function before handle_wait
old_func = '\n\ndef handle_wait(state, args):'
new_func = '''
def handle_drink(state, args):
    """Handle DRINK command - primarily for the Freshwater Well."""
    loc = state.get_location()
    if loc and loc.id == "freshwater_well" and not state.has_flag("well_drunk"):
        state.set_flag("well_drunk")
        state.set_flag("well_visited")
        state.score += 2
        return (
            "You cup your hands and drink from the shimmering well.\\n\\n"
            "The water is cold and impossibly clear. As it passes your lips, "
            "the world shifts.\\n\\n"
            "For a moment, you see everything clearly: your father's face, "
            "the faces of your crew, the islands you have visited and those yet to come. "
            "You understand briefly, profoundly, that every island was a mirror, "
            "every monster a part of yourself, every storm a lesson you needed to learn.\\n\\n"
            "The vision fades. You are standing at the well, your hands wet, "
            "your heart strangely light.\\n\\n"
            "(+2 points. The Water of Seeing has shown you a glimpse of the truth.)"
        )
    elif loc and loc.id == "freshwater_well" and state.has_flag("well_drunk"):
        return "You have already drunk from the well. The water is still there, but the vision will not come twice."
    return "There is nothing to drink here."


def handle_wait(state, args):'''

content = content.replace(old_func, new_func, 1)

with open('/home/ace/maelduin-adventure/game/engine.py', 'w') as f:
    f.write(content)

import ast
with open('/home/ace/maelduin-adventure/game/engine.py', 'r') as f:
    ast.parse(f.read())
print('OK')
