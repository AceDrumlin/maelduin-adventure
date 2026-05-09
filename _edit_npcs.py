#!/usr/bin/env python3
"""Line-based insertion into _shared.py for remaining 3 NPCs."""
path = "/home/ace/maelduin-adventure/game/levels/_shared.py"
with open(path, "r") as f:
    lines = f.readlines()

# --- garbh ---
# Find the line containing '            "father": (' that belongs to garbh
# by searching backward for 'garbh' text
target_key = '            "father": (\n'
idx = -1
for i, line in enumerate(lines):
    if line == target_key:
        # Check context before this line to ensure it's garbh's section
        # Look backward a few lines for 'Garbh' text
        context = ''.join(lines[max(0,i-5):i])
        if 'Garbh' in context and 'garbh' in context:
            idx = i
            break

if idx >= 0:
    insert_lines = [
        '            "greeting_if_forgave_garbh": (\n',
        '                \'Garbh looks up as you enter. His one eye softens.\\n\\n\'\n',
        '                \'\\"You came back. After everything... you came back.\\"\\n\\n\'\n',
        '                \'He sets down his drinking horn and stands. For a long moment he says nothing.\\n\\n\'\n',
        '                \'\\"I don\\\'t know what to call a man who forgives his father\\\'s killer. \'\n',
        '                \'A fool, maybe. Or a saint. But I know this much: the wolf can rest now. \'\n',
        '                \'And so can I.\\"\\n\\n\'\n',
        '                \'He extends his hand. This time, it is not a challenge. It is a greeting.\'\n',
        '            ),\n',
    ]
    for j, il in enumerate(insert_lines):
        lines.insert(idx + j, il)
    print(f"garbh: inserted greeting_if_forgave_garbh at line {idx}")
else:
    print("garbh: could NOT find garbh's 'father' key")

# --- silence_guardian ---
target_key = '            "anger": (\n'
idx = -1
for i, line in enumerate(lines):
    if line == target_key:
        context = ''.join(lines[max(0,i-5):i])
        if 'silence' in context.lower() or 'guardian' in context.lower() or 'pale figure' in context:
            idx = i
            break

if idx >= 0:
    insert_lines = [
        '            "greeting_if_got_silent_bell": (\n',
        '                \'The Guardian of Silence turns its blank face toward you. The air hums with quiet recognition.\\n\\n\'\n',
        '                \'\\"You carry the Silent Bell. The valley knows you. The silence knows you.\\"\\n\\n\'\n',
        '                \'It inclines its head \\u2014 the first gesture of warmth it has shown.\\n\\n\'\n',
        '                \'\\"You are welcome here always. Speak if you must. Laugh if you can. \'\n',
        '                \'You have earned the right to break silence, for you have proven you understand its value.\\"\'\n',
        '            ),\n',
    ]
    for j, il in enumerate(insert_lines):
        lines.insert(idx + j, il)
    print(f"silence_guardian: inserted greeting_if_got_silent_bell at line {idx}")
else:
    print("silence_guardian: could NOT find 'anger' key")

# --- guardian_of_peace ---
target_key = '            "stay": (\n'
idx = -1
for i, line in enumerate(lines):
    if line == target_key:
        context = ''.join(lines[max(0,i-5):i])
        if 'guardian_of_peace' in context or 'Promised Land' in context or 'Land of Promise' in context or 'guardian of peace' in context.lower():
            idx = i
            break

if idx >= 0:
    insert_lines = [
        '            "greeting_if_stayed_in_promised_land": (\n',
        '                \'The Guardian of Peace glides toward you, radiant as before.\\n\\n\'\n',
        '                \'\\"You chose to stay. And the Promised Land welcomes you as one of its own. \'\n',
        '                \'Every day the fruit tastes sweeter. Every night the stars shine brighter. \'\n',
        '                \'This is your home now, Mael Duin. You have crossed the sea of the world \'\n',
        '                \'and arrived at the shore of forever.\\"\\n\\n\'\n',
        '                \'Its warmth envelops you completely. There is no pain here. No longing. \'\n',
        '                \'Only peace.\'\n',
        '            ),\n',
    ]
    for j, il in enumerate(insert_lines):
        lines.insert(idx + j, il)
    print(f"guardian_of_peace: inserted greeting_if_stayed_in_promised_land at line {idx}")
else:
    print("guardian_of_peace: could NOT find the right 'stay' key")

with open(path, "w") as f:
    f.writelines(lines)

print("All edits complete.")
