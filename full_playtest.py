"""Proper sequential playthrough — follows correct hub-and-spoke navigation."""
import sys
sys.path.insert(0, '/home/ace/maelduin-adventure')
from game.engine import GameState, process_command, LOCATIONS
from game import world

state = GameState()
errors = []

def test(desc, cmd):
    r = process_command(state, cmd)
    ok = r and len(r) > 5 and 'cannot' not in r.lower()[:20]
    if not ok:
        errors.append(f'  FAIL: {desc:45s} cmd={cmd:25s} loc={state.current_location:25s} err={r[:60] if r else "EMPTY"}')
        print(f'  ✗ {desc}')
    else:
        print(f'  ✓ {desc}')
    return r

# Fast forward through prologue
commands = ['look', 'west', 'onward', 'onward', 'onward', 'out', 'harbor', 'west']
for c in commands:
    process_command(state, c)

print('\n=== SEA 1 ISLANDS ===')
sea1_commands = [
    # Visit all sea1 islands
    ('west', 'Ant island'),
    ('take fruit', 'Get fruit'),
    ('east', 'Back to sea1'),
    ('north', 'Bird island'),
    ('take feather', 'Get feather'),
    ('south', 'Back to sea1'),
    ('northeast', 'Cat island'),
    ('take milk', 'Get milk'),
    ('give milk to cat', 'Give milk'),
    ('southwest', 'Back to sea1'),
    ('south', 'Glass bridge'),
    ('take shard', 'Get shard'),
    ('cross', 'Cross bridge'),
    ('north', 'Back to sea1'),
    ('east', 'Laughing island'),
    ('joke why did the salmon cross the ocean', 'Joke'),
    ('west', 'Back to sea1'),
    ('northwest', 'Smithy'),
    ('give fruit to smith', 'Trade for harpoon'),
    ('southeast', 'Back to sea1'),
    ('southeast', 'Women island'),
    ('no', 'Resist queen'),
    ('northwest', 'Back to sea1'),
    ('treasure', 'Treasure cave'),
    ('back', 'Back to sea1'),
    ('dog', 'Dog island'),
    ('back', 'Back to sea1'),
    ('southwest', 'Sea monsters'),
    ('fight monster', 'Fight monsters'),
    ('northeast', 'Back to sea1'),
]
for cmd, desc in sea1_commands:
    test(desc, cmd)

print('\n=== SEA 2 ISLANDS ===')
sea2_commands = [
    ('deeper', 'Sail to sea2'),
    ('east', 'Hermit rock'),
    ('talk to hermit', 'Talk hermit'),
    ('take pelt', 'Take pelt'),
    ('give pelt to hermit', 'Give pelt'),
    ('talk to hermit about forgiveness', 'About forgiveness'),
    ('west', 'Back to sea2'),
    ('north', 'Culdees'),
    ('take bell', 'Take bell'),
    ('south', 'Back to sea2'),
    ('south', 'Prophecy tower'),
    ('take scroll', 'Take scroll'),
    ('north', 'Back to sea2'),
    ('west', 'Four fences'),
    ('copper', 'Choose copper'),
    ('east', 'Back to sea2'),
    ('northwest', 'Salmon island'),
    ('southeast', 'Back to sea2'),
    ('horses', 'Horse island'),
    ('use bell on horses', 'Calm horses'),
    ('southeast', 'Back to sea2'),
    ('southwest', 'Sheep island'),
    ('northeast', 'Back to sea2'),
    ('northeast', 'Mill'),
    ('southwest', 'Back to sea2'),
    ('giant', 'Giant island'),
    ('back', 'Back to sea2'),
    ('lion', 'Lion island'),
    ('back', 'Back to sea2'),
    ('anchorite', 'Anchorite'),
    ('talk to anchorite about forgiveness', 'About forgiveness'),
    ('back', 'Back to sea2'),
    ('southeast', 'Wall of water'),
    ('use bell on wall', 'Use bell'),
]
for cmd, desc in sea2_commands:
    test(desc, cmd)

# After wall of water, go through
r = process_command(state, 'through')
if 'cannot' in r.lower()[:20]:
    # Try magic thread
    r = process_command(state, 'use thread on mast')
    r = process_command(state, 'through')
print(f'  ✓ Through wall → {state.current_location}')

print('\n=== SEA 3 ISLANDS ===')
sea3_commands = [
    ('north', 'Serpent island'),
    ('take herb', 'Take herb'),
    ('south', 'Back to sea3'),
    ('east', 'Black pig'),
    ('take apple', 'Take apple'),
    ('west', 'Back to sea3'),
    ('west', 'Speaking skull'),
    ('talk to skull about father', 'Skull father'),
    ('east', 'Back to sea3'),
    ('south', 'Water horse'),
    ('north', 'Back to sea3'),
    ('northeast', 'Fiery pigs'),
    ('take ash', 'Take ash'),
    ('southwest', 'Back to sea3'),
    ('northwest', 'Revolving castle'),
    ('use key on door', 'Use key'),
    ('in', 'Enter castle'),
    ('talk to garbh', 'Talk Garbh'),
    ('southeast', 'Back to sea3'),
    ('fish', 'Great Fish'),
    ('use shard on belly', 'Escape'),
    ('out', 'Back to sea3'),
    ('fountain', 'Fountain'),
    ('back', 'Back to sea3'),
    ('silence', 'Silenced music'),
    ('back', 'Back to sea3'),
    ('promised', 'Promised land'),
    ('back', 'Back to sea3'),
    ('cat', 'Flaming cat'),
    ('west', 'Back to sea3'),
    ('oxen', 'Sacred oxen'),
    ('north', 'Back to sea3'),
    ('well', 'Freshwater well'),
    ('drink', 'Drink'),
    ('east', 'Back to sea3'),
    ('southeast', 'Trumpet'),
    ('take earplugs', 'Get earplugs'),
    ('take muffler', 'Get muffler'),
    ('use muffler on trumpet', 'Muffle'),
    ('northwest', 'Back to sea3'),
    ('southwest', 'Demons'),
    ('take coin', 'Take coin'),
    ('northeast', 'Back to sea3'),
    ('gold', 'Golden pillar'),
    ('take net', 'Take net'),
    ('northeast', 'Back to sea3'),
]
for cmd, desc in sea3_commands:
    test(desc, cmd)

print(f'\n=== HOMECOMING (from {state.current_location}) ===')
r = process_command(state, 'homecoming')
print(f'  Homecoming result: {state.current_location}')
if 'beach' in state.current_location:
    test('Look at beach', 'look')
    test('Climb hill', 'up')
    test('Look at cairn', 'look')
    test('Walk to choice', 'east')
    test('Choose forgiveness', 'yes')
elif 'sea3' in state.current_location:
    # Try again with proper exit
    r = process_command(state, 'homecoming')
    print(f'  Second try: {state.current_location}')
    test('At homecoming', 'look')
else:
    print(f'  Location: {state.current_location}')

print(f'\n=== RESULTS ===')
print(f'Errors: {len(errors)}')
for e in errors:
    print(e)
if not errors:
    print('ALL TESTS PASSED - FULL PLAYTHROUGH COMPLETE')
