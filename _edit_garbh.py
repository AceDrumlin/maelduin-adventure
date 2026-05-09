#!/usr/bin/env python3
"""Insert garbh greeting_if_forgave_garbh."""
path = "/home/ace/maelduin-adventure/game/levels/_shared.py"
with open(path, "r") as f:
    lines = f.readlines()

# Insert at line 1438 (0-indexed: 1437) - before the "father": ( line
idx = 1437  # 0-indexed - line 1438 in file (1-indexed)
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

with open(path, "w") as f:
    f.writelines(lines)

print("garbh: inserted successsfully")
