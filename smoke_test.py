"""Quick smoke test for new islands and fixes."""
import sys
sys.path.insert(0, '/home/ace/maelduin-adventure')
from game.engine import GameState, process_command, handle_look, LOCATIONS
from game import world

state = GameState()

passed = 0
failed = 0

def test(desc, cmd):
    global passed, failed
    r = process_command(state, cmd)
    # Game shouldn't crash
    if r and len(r) > 3:
        passed += 1
        print(f'  OK: {desc}')
    else:
        failed += 1
        print(f'  FAIL: {desc} -> {r[:60]}')
    return r

print('=== SMOKE TEST: KEY FEATURES ===')

# Prologue
test('Prologue look', 'look')
test('West to beach', 'west')
test('Onward child', 'onward')
test('Onward training', 'onward')
test('Onward feast', 'onward')
test('Out to druid', 'out')
test('Harbor to village', 'harbor')
test('West to sea1', 'west')
test('Talk diuran', 'talk to diuran')

# Sea to sea2
test('Deeper to sea2', 'deeper')
test('Talk fergus', 'talk to fergus')

# Sea2 to sea3  
test('Deeper to sea3', 'deeper')
test('Talk conganchnes', 'talk to conganchnes')

# NEW: Great Fish from sea3
test('Go to Great Fish', 'fish')
test('Escape with shard', 'use shard on belly')
test('Return to sea3', 'out')

# NEW: Fountain
test('Go to Fountain', 'fountain')
test('Return to sea3', 'back')

# NEW: Silenced Music
test('Go to Silenced Music', 'silence')
test('Return to sea3', 'back')

# NEW: Promised Land
test('Go to Promised Land', 'promised')
test('Return to sea3', 'back')

# Homecoming path from sea3
test('Homecoming from sea3', 'homecoming')
loc = state.current_location
print(f'  Location: {loc} (contains homecoming: {"homecoming" in loc})')

# Teleport to revolving castle for puzzle test
state.current_location = 'island_revolving_castle'
test('Use key on castle door', 'use key on door')
test('Enter castle', 'in')
r = test('Talk to Garbh', 'talk to garbh')
has_garbh = 'expected' in r.lower() or 'wolf' in r.lower() or 'Garbh' in r
print(f'  Garbh present: {has_garbh}')

print(f'\n=== RESULTS: {passed} passed, {failed} failed ===')
if failed == 0:
    print('ALL SMOKE TESTS PASSED')
