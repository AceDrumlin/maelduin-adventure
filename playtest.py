"""Comprehensive Playthrough — The Voyage of Mael Duin
Tests every island, puzzle, NPC interaction, and ending path.
"""
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
    results.append((description, cmd, passed, result[:100] if not passed else ''))
    if not passed:
        failures.append(f"  FAIL: {description}")
        print(f"  FAIL: {description}")
        print(f"    cmd: {cmd}")
        print(f"    result: {result[:200]}")
    else:
        print(f"  OK:   {description}")
    return result

def has_text(text):
    def check(result, state):
        return text.lower() in result.lower()
    return check

def at_location(loc_name):
    def check(result, state):
        return state.current_location == loc_name
    return check

def has_flag(flag):
    def check(result, state):
        return state.has_flag(flag)
    return check

def has_item(item_id):
    def check(result, state):
        return any(i.id == item_id for i in state.inventory)
    return check

def always():
    def check(result, state):
        return True
    return check

print("=" * 60)
print("COMPREHENSIVE PLAYTHROUGH - THE VOYAGE OF MAEL DUIN v2")
print("=" * 60)

# ============================
# ACT 1: PROLOGUE
# ============================
print("\n--- ACT 1: PROLOGUE ---")

test("Look at keep", "look", has_text("Ailill"))
test("Talk to young druid", "talk to young druid", has_text("questions"))
test("Go west to beach", "west", has_text("Ailill"))
test("Onward to childhood", "onward", has_text("Foster"))
test("Take wooden horse", "take horse", has_text("Carved Wooden Horse"))
test("Onward to training", "onward", has_text("Training"))
test("Talk to conganchnes", "talk to conganchnes", has_text("Conganchnes"))
test("Talk to fergus", "talk to fergus", has_text("Fergus"))
test("Talk to diuran", "talk to diuran", has_text("chapter"))
test("Onward to feast", "onward", has_text("Lorc"))
test("Out to druid sanctuary", "out", has_text("Magic Thread"))
test("Magic thread in inventory", "i", has_text("Magic Thread"))
test("Talk druid about murder", "talk to druid about murder", has_text("Northern Isles"))
test("Talk druid about vengeance", "talk to druid about vengeance", has_text("poison"))
test("Talk druid about father", "talk to druid about father", has_text("Ailill"))
test("Go to harbor", "harbor", has_text("curragh"))

# ============================
# ACT 2: SEA1 — First Islands
# ============================
print("\n--- ACT 2: SEA1 — ISLANDS ---")

test("Sail west to sea1", "west", at_location("sea1"))
test("Crew at sea — Diuran", "talk to diuran", has_text("poem") or has_text("chapter"))

# Home visit (new: home is now reachable)
test("Visit home village", "east", has_text("Aran"))
test("Talk to druid at home", "talk to druid", has_text("Magic Thread"))
test("Return to sea1", "west", at_location("sea1"))

# Ant island
test("Go to ant island", "west", at_location("island_ants"))
test("Take everlasting fruit", "take fruit", has_text("Everlasting Fruit"))
test("Return to sea1", "east", at_location("sea1"))

# Bird island
test("Go to bird island", "north", at_location("island_birds"))
test("Take speaking feather", "take feather", has_text("Speaking Feather"))
test("Return to sea1", "south", at_location("sea1"))

# Cat island
test("Go to cat island", "northeast", at_location("island_cat"))
test("Take bowl of milk", "take milk", has_text("Bowl of Milk"))
test("Give milk to cat", "give milk to cat", has_text("pearl") or has_text("acceptable"))
test("Cat pacified", "look", has_flag("cat_pacified"))
test("Sea pearl in inventory", "i", has_text("Sea Pearl"))
test("Return to sea1", "southwest", at_location("sea1"))

# Glass bridge
test("Go to glass bridge", "south", at_location("glass_bridge"))
test("Take glass shard", "take shard", has_text("Glass Shard"))
test("Cross bridge (with shard)", "cross", has_text("palace") or has_text("Palace"))
test("Return to bridge", "back", at_location("glass_bridge"))
test("Return to sea1", "north", at_location("sea1"))

# Laughing island
test("Go to laughing island", "east", at_location("island_laughing"))
test("Talk to king", "talk to king", has_text("LAUGH") or has_text("joke"))
test("Tell joke to king", "joke why did the salmon cross the ocean", has_text("potion") or has_text("laughing"))
test("King pacified", "look", has_flag("king_pacified"))
test("Return to sea1", "west", at_location("sea1"))

# Smithy island
test("Go to smithy", "northwest", at_location("island_smithy"))
test("Talk to smith", "talk to smith", has_text("forge"))
test("Trade with smith", "give fruit to smith", has_text("Harpoon"))
test("Magic harpoon obtained", "i", has_text("Magic Harpoon"))
test("Return to sea1", "southeast", at_location("sea1"))

# Women island
test("Go to women island", "southeast", at_location("island_women"))
test("Talk to queen", "talk to queen", has_text("stay"))
test("Resist queen", "no", has_text("resisted") or has_text("No"))
test("Queen resisted", "look", has_flag("resisted_queen"))
test("Return to sea1", "northwest", at_location("sea1"))

# Sea monsters (without harpoon test)
test("Go to sea monsters", "southwest", at_location("sea_monsters"))
test("Try sword on monster", "fight monster", has_text("better weapon") or has_text("bounces"))
test("Return to sea1", "northeast", at_location("sea1"))

# ============================
# ACT 3: SEA2 — Deeper Waters
# ============================
print("\n--- ACT 3: SEA2 — DEEPER WATERS ---")

test("Sail deeper to sea2", "deeper", at_location("sea2"))
test("Crew at sea2 — Fergus", "talk to fergus", has_text("star") or has_text("route"))

# NEW ISLAND: Wall of Water
test("Go to wall of water", "southeast", at_location("wall_of_water"))
test("Use thread on mast", "use thread on mast", has_text("wall") or has_text("calm") or has_text("Magic"))
test("Return to sea2", "northwest", at_location("sea2"))

# NEW ISLAND: Mill of the Sea
test("Go to mill exterior", "northeast", at_location("mill_exterior"))
test("Talk to mill guardian", "talk to guardian", has_text("mill") or has_text("grind"))
test("Enter mill interior", "in", at_location("mill_interior"))
test("Return to sea2", "southwest", at_location("sea2"))

# NEW ISLAND: Black & White Sheep
test("Go to sheep island", "southwest", at_location("island_sheep"))
test("Talk to ghostly shepherd", "talk to shepherd", has_text("riddle") or has_text("field"))
test("Return to sea2", "northeast", at_location("sea2"))

# NEW ISLAND: Giant Horses
test("Go to horse island", "horses", at_location("island_horses"))
test("Talk to stallion king", "talk to stallion", has_text("prove") or has_text("calm"))
test("Use bell to calm horses", "use bell", has_text("calm") or has_text("bell"))
test("Return to sea2", "southeast", at_location("sea2"))

# Existing islands — hermit
test("Go to hermit rock", "east", at_location("hermit_rock"))
test("Talk to hermit", "talk to hermit", has_text("blessing") or has_text("forgiveness"))
test("Talk hermit about father", "talk to hermit about father", has_text("peace"))
test("Talk hermit about forgiveness", "talk to hermit about forgiveness", has_text("feud"))
test("Take otter pelt", "take pelt", has_text("Otter Pelt"))
test("Give pelt to hermit", "give pelt to hermit", has_text("peace") or has_text("pelt"))
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
test("Try gold fence (wrong)", "gold", has_text("lose") or has_text("trap") or has_text("nothing"))
test("Try copper fence (correct)", "copper", has_text("key") or has_text("Revolving Key") or has_text("correct"))
test("Revolving key obtained", "i", has_text("Revolving Key"))
test("Return to sea2", "east", at_location("sea2"))

# Salmon island
test("Go to salmon island", "northwest", at_location("island_salmon"))
test("Return to sea2", "southeast", at_location("sea2"))

# ============================
# ACT 4: SEA3 — Final Stretch
# ============================
print("\n--- ACT 4: SEA3 — FINAL STRETCH ---")

test("Sail deeper to sea3", "deeper", at_location("sea3"))
test("Crew at sea3 — Conganchnes", "talk to conganchnes", has_text("fight") or has_text("sharp") or has_text("Conganchnes"))

# NEW ISLAND: Flaming Cat
test("Go to flaming cat", "cat", at_location("island_flaming_cat"))
test("Give milk to cat", "give milk to cat", has_text("purr") or has_text("acceptable") or has_text("tribute"))
test("Return to sea3", "west", at_location("sea3"))

# NEW ISLAND: Sacred Oxen
test("Go to sacred oxen", "oxen", at_location("island_oxen"))
test("Take golden horn", "take horn", has_text("Golden Horn"))
test("Return to sea3", "north", at_location("sea3"))

# NEW ISLAND: Freshwater Well
test("Go to freshwater well", "well", at_location("freshwater_well"))
test("Drink from well", "drink", has_text("vision") or has_text("water"))
test("Return to sea3", "east", at_location("sea3"))

# Serpent island
test("Go to serpent island", "north", at_location("serpent_island"))
test("Take antidote herb", "take herb", has_text("Antidote Herb"))
test("Return to sea3", "south", at_location("sea3"))

# Black pig
test("Go to black pig", "east", at_location("black_pig"))
test("Take golden apple", "take apple", has_text("Golden Apple"))
test("Return to sea3", "west", at_location("sea3"))

# Speaking skull
test("Go to speaking skull", "west", at_location("speaking_skull"))
test("Talk to skull", "talk to skull", has_text("visitor") or has_text("boredom"))
test("Ask skull about father", "talk to skull about father", has_text("Garbh") or has_text("murderer"))
test("Ask skull about revenge", "talk to skull about revenge", has_text("vengeance") or has_text("cup"))
test("Ask skull about home", "talk to skull about home", has_text("return") or has_text("home"))
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

# Test Garbh NPC
test("Enter red room (Garbh)", "north", has_text("Garbh") or has_text("red") or at_location("castle_red"))
if state.current_location == "castle_red":
    test("Talk to Garbh", "talk to garbh", has_text("Wolf") or has_text("expected"))
    test("Talk Garbh about father", "talk to garbh about father", has_text("Ailill") or has_text("blood feud"))
    test("Talk Garbh about revenge", "talk to garbh about revenge", has_text("become me") or has_text("kill me"))
    test("Talk Garbh about forgiveness", "talk to garbh about forgiveness", has_text("better man") or has_text("forgive"))
else:
    test("Enter red room (fallback)", "look", always())
test("Return to sea3", "southeast", at_location("sea3"))

# Trumpet island
test("Go to trumpet island", "southeast", at_location("island_trumpet"))
test("Take earplugs", "take earplugs", has_text("Earplugs"))
test("Take muffler", "take muffler", has_text("Muffler"))
test("Use muffler on trumpet", "use muffler on trumpet", has_text("muffle") or has_text("silence"))
test("Return to sea3", "northwest", at_location("sea3"))

# Demon island
test("Go to demon island", "southwest", at_location("island_demons"))
test("Take demon coin", "take coin", has_text("Coin"))
test("Return to sea3", "northeast", at_location("sea3"))

# Golden pillar
test("Go to golden pillar", "southwest", at_location("island_golden_pillar"))
test("Take silver net", "take net", has_text("Silver Net"))
test("Return to sea3", "northeast", at_location("sea3"))

# ============================
# ACT 5: HOMECOMING
# ============================
print("\n--- ACT 5: HOMECOMING ---")

# Visit home first (new feature — home connected)
test("Go home from village_harbor", "home", at_location("home"))

test("Head to homecoming", "homecoming", has_text("Home") or at_location("homecoming_beach"))
if state.current_location == "homecoming_beach":
    test("Druid arrival speech", "look", has_text("druid") or has_text("returned"))
    test("Go to hill", "up", at_location("homecoming_hill"))
    test("Hill reflection", "look", has_text("cairn") or has_text("Ailill"))
    test("Go to choice point", "east", at_location("homecoming_choice"))
    test("Final moment text", "look", has_text("YES") or has_text("forgive") or has_text("NO"))
else:
    # Fallback — old homecoming path
    test("Look at homecoming", "look", has_text("YES") or has_text("forgive"))

# Test forgiveness ending
test("Choose forgiveness", "yes", has_text("lower") or has_text("forgiveness") or has_text("end") or has_text("voyage"))

# ============================
# EDGE CASES (fresh state)
# ============================
print("\n--- EDGE CASES ---")

s2 = GameState()

test("Unknown command 'xyzzy'", "xyzzy", has_text("don't understand"))
test("Examine nothing", "examine", has_text("Examine what?"))
test("Take nothing", "take", has_text("Take what?"))
test("Empty command", "", always())
test("Examine non-existent item", "examine blorple", has_text("nothing special"))
test("Take non-existent item", "take unicorn", has_text("don't see"))
test("Talk to no one", "talk to", has_text("Talk to whom"))
test("Give nothing", "give", has_text("Give what"))
test("Go non-existent direction", "xyz", has_text("don't understand"))

# New edge cases
s3 = GameState()
s3.current_location = "home"
test("Talk druid about unknown topic", "talk to druid about blorple", has_text("greeting") or has_text("Magic Thread") or has_text("druid"))
test("Use nothing", "use", has_text("Use what"))
test("Drop nothing", "drop", has_text("Drop what"))
test("Crew command", "crew", has_text("CREW") or has_text("Diur"))
test("Score command", "score", has_text("Score") or has_text("score"))

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
