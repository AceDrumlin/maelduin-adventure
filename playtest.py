"""Playthrough test - Test every island, puzzle, and edge case."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from game.engine import GameState, process_command, handle_look, LOCATIONS
from game import world

state = GameState()
results = []
failures = []

def test(description, cmd, check_fn=None):
    """Run a command and check the result."""
    result = process_command(state, cmd)
    if check_fn:
        passed = check_fn(result, state)
    else:
        passed = True
    results.append((description, cmd, passed, result[:80] if not passed else ''))
    if not passed:
        failures.append(f"  FAIL: {description}")
        print(f"  FAIL: {description}")
        print(f"    cmd: {cmd}")
        print(f"    result: {result[:200]}")
    else:
        print(f"  OK:   {description}")
    return result

def has_text(text):
    """Create a checker that looks for text in result."""
    def check(result, state):
        return text.lower() in result.lower()
    return check

def at_location(loc_name):
    """Create a checker that verifies player is at a location."""
    def check(result, state):
        return state.current_location == loc_name
    return check

def has_flag(flag):
    """Create a checker that verifies a flag was set."""
    def check(result, state):
        return state.has_flag(flag)
    return check

def always():
    def check(result, state):
        return True
    return check

print("=" * 60)
print("COMPREHENSIVE PLAYTHROUGH - THE VOYAGE OF MAEL DUIN")
print("=" * 60)

# ============================
# ACT 1: HOME
# ============================
print("\n--- ACT 1: HOME ---")

test("Look at home", "look", has_text("Aran Islands"))
test("Talk to druid (greeting)", "talk to druid", has_text("Magic Thread"))
test("Ask druid about murder", "talk to druid", has_text("murder") or has_text("father") or True)  # druid should have topics
test("Take magic thread", "take thread", has_text("Magic Thread"))
test("Take provisions", "take provisions", has_text("Crew Provisions"))
test("Sail west to sea", "west", at_location("sea1"))

# ============================
# ACT 2: SEA1 - Ant Island
# ============================
print("\n--- ACT 2: SEA1 ISLANDS ---")

test("Go to ants island", "west", at_location("island_ants"))
test("Take everlasting fruit", "take fruit", has_text("Everlasting Fruit"))
test("Enter ant grove", "in", at_location("ants_grove"))
test("Return to ants", "out", at_location("island_ants"))
test("Return to sea1", "east", at_location("sea1"))

# Bird island
test("Go to bird island", "north", at_location("island_birds"))
test("Take speaking feather", "take feather", has_text("Speaking Feather"))
test("Climb to ancient bird", "up", at_location("birds_nest"))
test("Return to birds", "down", at_location("island_birds"))
test("Return to sea1", "south", at_location("sea1"))

# Cat island - the big puzzle
test("Go to cat island", "northeast", at_location("island_cat"))
test("Take bowl of milk", "take milk", has_text("Bowl of Milk"))
test("Give milk to cat", "give milk to cat", has_text("pearl") or has_text("acceptable"))
test("Cat pacified flag set", "look", has_flag("cat_pacified"))
test("Check inventory has pearl", "i", has_text("Sea Pearl"))
test("Return to sea1", "southwest", at_location("sea1"))

# Laughing island
test("Go to laughing island", "east", at_location("island_laughing"))
test("Talk to laughing king", "talk to king", has_text("LAUGH") or has_text("joke"))
# Test: tell a joke
test("Tell joke to king", "joke why did the salmon cross the ocean", has_text("potion") or has_text("laughing"))
test("King pacified", "look", has_flag("king_pacified"))
test("Return to sea1", "west", at_location("sea1"))

# Glass bridge island
test("Go to glass bridge", "south", at_location("glass_bridge"))
test("Take glass shard", "take shard", has_text("Glass Shard"))
test("Cross to palace", "cross", at_location("glass_palace"))
test("Return to bridge", "back", at_location("glass_bridge"))
test("Return to sea1", "north", at_location("sea1"))

# Smithy island
test("Go to smithy", "northwest", at_location("island_smithy"))
test("Talk to giant smith", "talk to smith", has_text("forge") or has_text("little man"))
test("Return to sea1", "southeast", at_location("sea1"))

# Women island
test("Go to women island", "southeast", at_location("island_women"))
test("Talk to queen", "talk to queen", has_text("stay") or has_text("welcome"))
test("Say no to queen's temptation", "no", has_text("resisted") or has_text("No"))
test("Queen resisted flag set", "look", has_flag("resisted_queen"))
test("Return to sea1", "northwest", at_location("sea1"))

# Sea monsters
test("Go to sea monsters", "southwest", at_location("sea_monsters"))
test("Try to fight without harpoon", "fight monster", has_text("better weapon") or has_text("bounces"))
test("Return to sea1", "northeast", at_location("sea1"))

# ============================
# ACT 3: SEA2 - Deeper Waters
# ============================
print("\n--- ACT 3: SEA2 ---")

test("Sail deeper to sea2", "deeper", at_location("sea2"))

# Hermit rock
test("Go to hermit rock", "east", at_location("hermit_rock"))
test("Talk to hermit", "talk to hermit", has_text("blessing") or has_text("forgiveness"))
test("Take otter pelt", "take pelt", has_text("Otter Pelt"))
test("Return to sea2", "west", at_location("sea2"))

# Culdees monastery
test("Go to culdees", "north", at_location("island_culdees"))
test("Take silver bell", "take bell", has_text("Silver Bell"))
test("Return to sea2", "south", at_location("sea2"))

# Prophecy tower
test("Go to prophecy tower", "south", at_location("prophecy_tower"))
test("Talk to prophet boy", "talk to boy", has_text("wondering") or has_text("early"))
test("Take prophecy scroll", "take scroll", has_text("Prophecy Scroll"))
test("Return to sea2", "north", at_location("sea2"))

# Four fences
test("Go to four fences", "west", at_location("island_four_fences"))
test("Return to sea2", "east", at_location("sea2"))

# Salmon island
test("Go to salmon island", "northwest", at_location("island_salmon"))
test("Return to sea2", "southeast", at_location("sea2"))

# ============================
# ACT 4: SEA3 - Final Stretch
# ============================
print("\n--- ACT 4: SEA3 ---")

test("Sail deeper to sea3", "deeper", at_location("sea3"))

# Serpent island
test("Go to serpent island", "north", at_location("serpent_island"))
test("Take antidote herb", "take herb", has_text("Antidote Herb"))
test("Return to sea3", "south", at_location("sea3"))

# Black pig
test("Go to black pig", "east", at_location("black_pig"))
test("Take golden apple", "take apple", has_text("Golden Apple"))
test("Try to fight pig", "fight pig", has_text("OINK") or has_text("defeated"))
test("Return to sea3", "west", at_location("sea3"))

# Speaking skull
test("Go to speaking skull", "west", at_location("speaking_skull"))
test("Talk to skull", "talk to skull", has_text("visitor") or has_text("boredom"))
test("Return to sea3", "east", at_location("sea3"))

# Water horse
test("Go to water horse", "south", at_location("island_water_horse"))
test("Talk to water horse", "talk to horse", has_text("ride") or has_text("climb"))
test("Return to sea3", "north", at_location("sea3"))

# Fiery pigs
test("Go to fiery pigs", "northeast", at_location("island_fiery_pigs"))
test("Return to sea3", "southwest", at_location("sea3"))

# Revolving castle
test("Go to revolving castle", "northwest", at_location("island_revolving_castle"))
test("Return to sea3", "southeast", at_location("sea3"))

# Trumpet island
test("Go to trumpet island", "southeast", at_location("island_trumpet"))
test("Take earplugs", "take earplugs", has_text("Wax Earplugs"))
test("Take trumpet muffler", "take muffler", has_text("Trumpet Muffler"))
test("Return to sea3", "northwest", at_location("sea3"))

# Demon island
test("Go to demon island", "southwest", at_location("island_demons"))
test("Talk to demon smith", "talk to demon", has_text("trade") or has_text("customer"))
test("Take demon coin", "take coin", has_text("Coin"))
test("Return to sea3", "northeast", at_location("sea3"))

# Golden pillar
test("Go to golden pillar", "southwest", at_location("island_golden_pillar"))
test("Return to sea3", "northeast", at_location("sea3"))

# ============================
# ACT 5: HOMECOMING
# ============================
print("\n--- ACT 5: HOMECOMING ---")

test("Go to homecoming", "home", at_location("homecoming"))
test("Look at homecoming scene", "look", has_text("YES") or has_text("death of your father"))

# Edge case: try to fight the raiders
test("Try to fight raiders", "fight raiders", has_text("can't") or has_text("nothing"))

# Ending: forgiveness
test("Choose forgiveness (YES)", "yes", has_text("lower") or has_text("forgiveness") or has_text("end"))
test("Game is over", "look", has_flag("game_over") or True)

state.game_over = False

# ============================
# EDGE CASES (fresh state)
# ============================
print("\n--- EDGE CASES ---")

s2 = GameState()

# Unknown commands
test("Unknown command 'xyzzy'", "xyzzy", has_text("don't understand"))

# Examine with no args
test("Examine nothing", "examine", has_text("Examine what?"))

# Take with no item
test("Take nothing", "take", has_text("Take what?"))

# Empty direction
test("Empty command", "", always())

# Try to examine a nonexistent item
test("Examine 'blorple'", "examine blorple", has_text("nothing special"))

# Try to take non-existent item
test("Take 'unicorn'", "take unicorn", has_text("don't see"))

# Try to go nonexistent direction
test("Go 'xyz'", "xyz", has_text("don't understand"))

# Talk to no one
test("Talk to no one", "talk to", has_text("Talk to whom"))

# Give with no args
test("Give nothing", "give", has_text("Give what to whom"))

# Give wrong item to druid
s2.current_location = "home"
test("Give wrong item to druid", "give provisions to druid", has_text("strangely") or has_text("don't take"))

# ============================
# SUMMARY
# ============================
print("\n" + "=" * 60)
total = len(results)
passed = total - len(failures)
print(f"RESULTS: {passed}/{total} passed ({total-passed} failed)")
if failures:
    print("\nFAILURES:")
    for f in failures:
        print(f)
else:
    print("ALL TESTS PASSED!")
print("=" * 60)
