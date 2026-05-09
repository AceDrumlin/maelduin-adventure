"""Add conditional dialogue variants to ALL shared NPCs in a single pass."""
import re

FILE = "game/levels/_shared.py"

with open(FILE) as f:
    content = f.read()

# Conditional dialogue variants to inject
# Format: (npc_id, key_to_add_after, new_entry_key, new_entry_text)
INJECTIONS = [
    # --- DRUID (greeting -> add greeting_if_learned_truth) ---
    ("druid", "greeting", "greeting_if_learned_truth", (
        'The druid nods slowly, a hint of a smile on his ancient face.\\n\\n'
        '"So. You know. The truth sits heavy in your chest, doesn\'t it? '
        'Good. That means you are ready.\\n\\n'
        'The magic thread will guide you. The sea will test you. '
        'And when you return, you will not be the man who left.\\n\\n'
        'Now go. The tide waits for no man, not even one with vengeance in his heart."'
    )),

    # --- SMITH (greeting -> add greeting_if_got_harpoon) ---
    ("smith", "greeting", "greeting_if_got_harpoon", (
        'The smith looks up from his work and grins, his face lit by the glow of the forge.\\n\\n'
        '"Back again, little man? I hope you\'re not looking for another harpoon — '
        'one masterpiece per customer is my rule.\\n\\n'
        'But if you\'ve got something shiny to trade, I\'m always listening. '
        'A smith\'s work is never done."'
    )),

    # --- LAUGHING KING (greeting -> add greeting_if_king_pacified) ---
    ("laughing_king", "greeting", "greeting_if_king_pacified", (
        'The Laughing King wipes a tear from his eye and lets out a long, contented sigh.\\n\\n'
        '"Ahhh. That was a good laugh. The BEST laugh. I don\'t think I\'ve laughed that hard since '
        'I accidentally sat on a hedgehog.\\n\\n'
        'He smiles — a genuine, peaceful smile. '
        '"You know, I\'d forgotten what silence sounds like. It\'s... nice. '
        'Still funny, though. Everything is still funny. Just... quieter."\\n\\n'
        'He hums contentedly, tapping his fingers on his one-legged stool.'
    )),

    # --- CAT (greeting -> add greeting_if_cat_pacified) ---
    ("cat", "greeting", "greeting_if_cat_pacified", (
        'The enormous cat is sprawled across its golden throne, purring like a dozen bees in a barrel. '
        'It opens one eye as you approach.\\n\\n'
        '"Ah. The milk-bringer. You may approach.\\n\\n'
        'It yawns, showing teeth the size of your fingers, then closes its eye again.\\n\\n'
        '"I have deemed you... acceptable. You may pass through my island whenever you wish. '
        'Consider yourself one of the few humans I don\'t actively despise.\\n\\n'
        'Don\'t let it go to your head."'
    )),

    # --- QUEEN (greeting -> add greeting_if_resisted_queen) ---
    ("queen", "greeting", "greeting_if_resisted_queen", (
        'The Queen watches you from her throne, her smile cold and precise.\\n\\n'
        '"You\'re back. I didn\'t think you would be. Most men who leave do not return — '
        'they cannot bear to see what they have refused.\\n\\n'
        'But you are not most men, are you, Mael Duin? You have the Wolf\'s blood in you. '
        'Stubborn. Foolish. Brave.\\n\\n'
        'She leans forward, her eyes glittering. '
        '"I respect you for it. But do not mistake respect for warmth. '
        'My island is no longer open to you. Leave before I change my mind."'
    )),

    # --- HERMIT (greeting -> add greeting_if_otter_pelt_returned) ---
    ("hermit", "greeting", "greeting_if_otter_pelt_returned", (
        'The hermit is sitting on his rock, the otter pelt wrapped around his shoulders. '
        'He looks warmer now. More at peace.\\n\\n'
        '"Mael Duin. You returned my companion\'s pelt. I cannot thank you enough.\\n\\n'
        'He pats the pelt gently. "It\'s funny — I thought the otter was gone forever. '
        'But he never really left. He was just... waiting to come home in a different form.\\n\\n'
        'He looks at you with clear, kind eyes. '
        '"You carry the same burden I carried — the weight of a father lost. '
        'But you carry it differently. You carry it forward. That takes strength."'
    )),

    # --- PROPHET BOY (greeting -> add greeting_if_fn) ---
    ("prophet_boy", "greeting", "greeting_if_fn", 
     'lambda s: _prophet_greeting(s)'),
]

# We'll also add the helper function for prophet_boy
PROPHET_FN = """
def _prophet_greeting(state):
    \"\"\"Prophet boy's greeting changes based on islands visited.\"\"\"
    # Count island flags that don't start with prologue locations
    island_count = sum(1 for k in state.flags if k.endswith('_visited')
                      and not k.startswith('ailill') and not k.startswith('foster')
                      and not k.startswith('training') and not k.startswith('feast')
                      and not k.startswith('druid') and not k.startswith('village')
                      and not k.startswith('fathers') and not k.startswith('home')
                      and not k.startswith('ants_grove') and not k.startswith('birds_nest')
                      and not k.startswith('castle_entry'))
    
    if island_count >= 10:
        return (
            'The boy closes his book and claps his hands.\\n\\n'
            f'"You have visited {island_count} islands! You are more than halfway through your journey. '
            'I can see it in your eyes — the distance you have traveled, the wonders you have seen.\\n\\n'
            'You are not the same man who left Ireland. Your father would be proud.\\n\\n'
            'The skull was right, you know. You will find what you are looking for in the Revolving Castle. '
            'But by the time you do, you may find you are looking for something else entirely."'
        )
    if island_count >= 5:
        return (
            'The boy giggles as you enter.\\n\\n'
            f'"{island_count} islands so far! You are making good progress. '
            'I can see the pattern forming — each island teaches you something you did not know you needed to learn.\\n\\n'
            'The giant ants taught you patience. The speaking birds taught you to listen. '
            'What will the next island teach you?"'
        )
    if island_count >= 2:
        return (
            'The boy looks up from his book and grins.\\n\\n'
            f'"You have visited {island_count} islands already! '
            'I told you this would be an adventure worth writing about.\\n\\n'
            'The druid\'s thread is pulling true. Follow it. Trust it. '
            'It will take you where you need to go — though not necessarily where you want to go."'
        )
    return (
        'The boy closes his book and giggles.\\n\\n'
        '"You\'re early! I didn\'t expect you for another three chapters. '
        'But since you\'re here — ask me anything. I already know the answer, '
        'but you don\'t, so it\'s more fun if you ask."'
    )

"""

# For each NPC, find their dialogue dict and inject the new entry
# Strategy: find the NPC's opening and then the specific dialogue entry to inject after

def find_npc_area(content, npc_id):
    """Find the line range for a given NPC definition."""
    pattern = rf'\n\s+n\["{npc_id}"\]\s*=\s*NPC\('
    m = re.search(pattern, content)
    if not m:
        return None
    
    start = m.start()
    # Find the matching closing paren
    depth = 0
    in_string = False
    string_char = None
    i = start
    while i < len(content):
        c = content[i]
        if not in_string:
            if c in '"\'':
                in_string = True
                string_char = c
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth <= 0:
                    return (start, i + 1)
        else:
            if c == '\\':
                i += 1  # skip escaped char
            elif c == string_char:
                in_string = False
        i += 1
    return None

def find_dialogue_entry(content, npc_start, entry_key):
    """Find a dialogue entry inside an NPC definition."""
    # Look for "entry_key": ( after the NPC start
    search_from = npc_start
    pattern = rf'"\b{re.escape(entry_key)}\b"\s*:\s*\('
    m = re.search(pattern, content[search_from:])
    if not m:
        return None
    abs_pos = search_from + m.start()
    
    # Find the matching closing paren of this tuple
    depth = 0
    in_string = False
    string_char = None
    i = abs_pos
    while i < len(content):
        c = content[i]
        if not in_string:
            if c in '"\'':
                in_string = True
                string_char = c
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth <= 0:
                    return (abs_pos, i + 1)
        else:
            if c == '\\':
                i += 1
            elif c == string_char:
                in_string = False
        i += 1
    return None

# First, insert the _prophet_greeting function before the _make_npcs call
# Find where _make_npcs is defined
make_npcs_pos = content.find('def _make_npcs():')
if make_npcs_pos > 0 and PROPHET_FN not in content:
    # Insert before _make_npcs
    content = content[:make_npcs_pos] + PROPHET_FN + "\n\n" + content[make_npcs_pos:]

# Now process each injection
for npc_id, after_key, new_key, new_text in INJECTIONS:
    npc_range = find_npc_area(content, npc_id)
    if not npc_range:
        print(f"WARNING: Could not find NPC '{npc_id}'")
        continue
    
    npc_start, npc_end = npc_range
    
    # Find the "after_key" entry
    entry_range = find_dialogue_entry(content, npc_start, after_key)
    if not entry_range:
        print(f"WARNING: Could not find '{after_key}' in NPC '{npc_id}'")
        continue
    
    entry_end = entry_range[1]
    
    # Build the injection text
    if new_key.endswith("_fn"):
        # Function reference
        inject_text = f'        "{new_key}": {new_text},\n\n'
    else:
        # Text string
        inject_text = f'        "{new_key}": (\n            {new_text}\n        ),\n\n'
    
    # Insert after the closing of the "after_key" entry
    # Find the ) and , that close the parenthesized entry
    content = content[:entry_end] + "\n" + inject_text + content[entry_end:]
    
    print(f"✓ Added '{new_key}' to NPC '{npc_id}'")

with open(FILE, "w") as f:
    f.write(content)

print("\nDone! All conditional dialogue variants added.")
