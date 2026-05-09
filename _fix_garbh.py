#!/usr/bin/env python3
"""Fix garbh missing greeting closing bracket."""
path = "/home/ace/maelduin-adventure/game/levels/_shared.py"
with open(path, "r") as f:
    content = f.read()

# Find and fix: line 1437 ends greeting text, line 1438 starts greeting_if_forgave_garbh
# Missing the ), closing for greeting
old = "                '\\\"I knew you would come, sooner or later. The sea always brings what it owes.\\\"'\n            \"greeting_if_forgave_garbh\": ("
new = "                '\\\"I knew you would come, sooner or later. The sea always brings what it owes.\\\"'\n            ),\n            \"greeting_if_forgave_garbh\": ("

if old in content:
    content = content.replace(old, new)
    print("Fixed garbh structure")
else:
    print("Could not find garbh pattern")

with open(path, "w") as f:
    f.write(content)
