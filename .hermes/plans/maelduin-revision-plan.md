# The Voyage of Mael Duin — Full Story Revision Plan

> **Goal:** Revise the game to be a fully-fledged, faithful adaptation of the original 10th-century Irish immram "Immram Curaig Maíle Dúin"
>
> **Approach:** Phase-based, incremental. Each phase is self-contained so subagents can work in parallel where possible.

---

## Phase 0: Critical Infrastructure Fixes

These must be done first — everything else depends on them working.

### Task 0.1: Wire the Topic Dialogue System
- **Why:** Interactions.py has a 14-topic `get_talk_topic_response()` system that engine.py's `handle_talk()` never calls. Beautiful content sitting unused.
- **What:** Modify `handle_talk()` in engine.py to call `get_talk_topic_response()` when players ask NPCs about specific topics (e.g. "talk to druid about murder"). Keep greeting as default.
- **Pattern:** `talk to <npc>` → greeting. `talk to <npc> about <topic>` → topic response.
- **Files:** `game/engine.py` (handle_talk), `game/interactions.py` (already has the system)

### Task 0.2: Create Missing NPC Entities
- **Why:** `black_pig` and `serpent` are referenced in give/use combos but don't exist as NPC objects.
- **What:** Add NPC entries for `black_pig` (the giant black pig guarding the apples) and `serpent` (the great serpent guarding the herb). Give them dialogue, aliases, and personality groups.
- **Files:** `game/levels/_shared.py`

### Task 0.3: Fix Orphaned "home" Location
- **Options:** (A) Add an exit from village_harbor back to home. (B) Remove home entirely. (C) Make home the return destination after homecoming.
- **Best: Option A + home becomes post-voyage epilogue hub.**

### Task 0.4: Fix the Playtest
- Update `playtest.py` to start from `ailill_keep` prologue path instead of `home`.
- Or better: write a new comprehensive playtest.

---

## Phase 1: Add Missing Islands (New Level: level_05_missing_islands.py)

Add the most thematically important missing islands from the original tale.

### Island 1: The Mill of the Sea
- **Original story:** A giant mill that grinds everything — the crew throw a stone into it to stop it momentarily.
- **Puzzle:** The mill churns the sea, creating whirlpools. Find a millstone or heavy object to jam the mechanism. Use the Fiery Ash? Use the Golden Apple?
- **NPC:** The Mill Guardian (ancient, half-deaf)
- **Items:** Millstone fragment (puzzle item), ground grain (healing food?)
- **Location:** Connected from sea2 (northeast)

### Island 2: The Island of Black & White Sheep
- **Original story:** Sheep that change color as they cross between two fields (black ↔ white), symbolizing the passage of souls / good vs evil.
- **Puzzle:** A riddle of transformation. The crew must figure out the pattern to cross safely. Solve the color-changing riddle → gain a magical fleece.
- **NPC:** The Shepherd (ghostly, speaks in riddles)
- **Items:** Fleece of Change (magical item, used to disguise)

### Island 3: The Island of Giant Horses
- **Original story:** A giant horse attacks and kills a crewman.
- **Puzzle:** The horses are wild and dangerous. Use the Otter Pelt to gain their trust? Or the Silver Bell to calm them? Or the Speaking Feather to command them?
- **NPC:** The Stallion King (ghost horse spirit)
- **Items:** Horsehair Bridle (allows faster sea travel)

### Island 4: The Island of the Flaming Cat
- **Original story:** A small cat that grows into a giant flaming beast when provoked.
- **Puzzle:** The cat guards a treasure. If you steal, it grows huge and attacks. Use food to distract (Bowl of Milk? Everlasting Fruit?). If you resist temptation, it stays small and gives a reward.
- **NPC:** The Little Cat / Flaming Cat
- **Items:** Sunstone (illuminates dark places)

### Island 5: The Wall of Water
- **Original story:** The sea rises like a wall; the crew must sail through it.
- **Puzzle:** Navigation hazard. Use the Magic Thread + crew sailing command to navigate through. Wrong choice = damage to crew.
- **Items:** None (survival encounter)

### Island 6: The Island of the Sacred Oxen
- **Original story:** Sacred white oxen with golden horns.
- **Puzzle:** The oxen are sacred — killing them brings bad luck. The crew must take only what they need (milk/hide) without harming them.
- **Items:** Golden Horn (trumpet, calls for aid)

### Island 7: The Strand of the Freshwater Well
- **Original story:** The first strange landfall — a well of freshwater with a magical property.
- **Puzzle:** Drinking from the well grants visions... or a curse. Choose wisely.
- **Items:** Water of Vision (temporary clairvoyance)

---

## Phase 2: Complete Existing Islands

### Task 2.1: Wisdom Salmon — Add Fishing
- Add a USE interaction for Silver Net on the salmon pool at island_salmon
- Or add a `fish` command
- Eating the salmon grants a permanent buff (knowledge of a puzzle solution)

### Task 2.2: Glass Bridge — Real Puzzle
- Add a condition to cross: you must be carrying the Glass Shard OR have the Hermit's Blessing
- Wrong crossing → fall, lose crew member
- Right crossing → gain access to the palace treasure

### Task 2.3: Trumpet Island — Consequences
- After trumpet muffler + earplugs are used, allow safe passage
- If you don't use them, the trumpet blast deafens a crewman
- Add the trumpet blast as a timer puzzle

### Task 2.4: Speaking Skull Questions
- Wire the skull's question system: "ask skull about father", "ask skull about revenge", "ask skull about home"
- Each question reveals a clue about the endgame

### Task 2.5: Crew at Sea Locations
- Place crew NPCs at sea hub locations (Diurán at sea1, Conganchnes at sea2, Fergus at sea3)
- Each gives voyage-relevant advice/dialogue

### Task 2.6: Four Fences — Clarify Puzzle
- Currently has a simple "copper is correct" answer
- Add stronger theming and poetic clues from the druid

### Task 2.7: Revolving Castle — The Murderer Confrontation
- Expand the castle interior: add the murderer (named NPC: Garbh)
- Add dialogue: the murderer explains the blood feud
- Add the forgiveness choice (already exists in homecoming)
- Add a proper puzzle to stop the castle's rotation

### Task 2.8: Sea Monsters — Proper Encounter
- Add multiple sea monster types
- Different strategies to defeat/each: Magic Harpoon, Silver Bell (calm), Golden Horn (call for aid)

---

## Phase 3: Enhance the Emotional Arc

### Task 3.1: Expand Homecoming
- Add multiple endings: (1) Forgiveness (good), (2) Vengeance (bad), (3) Wisdom (neutral — you understand but still don't forgive)
- Add NPC reactions to your choice
- Add a final druid epilogue scene

### Task 3.2: The Hermit's Full Lesson
- The hermit at hermit_rock should have a multi-part dialogue tree
- Topics: forgiveness, fate, the meaning of the islands, the nature of your quest
- Visiting the hermit BEFORE the homecoming changes the ending options

### Task 3.3: The Prophetic Boy's Full Role
- The boy should foretell the number of islands visited
- Give the player a hint about the revolving castle puzzle
- Add a prophecy flag that tracks your truth-seeking

### Task 3.4: Druid NPC Journey
- The druid should appear at key moments (seen in visions? or as a recurring character?)
- Give progressive revelations as the voyage deepens

---

## Phase 4: Integration & Polish

### Task 4.1: New Comprehensive Playtest
- Full path through prologue → all islands → homecoming
- Edge cases for new islands
- Test all give/use combos

### Task 4.2: Score Balancing
- Ensure all puzzles award appropriate points
- Add a maximum possible score

### Task 4.3: Narrative Coherence Pass
- Ensure the story flows naturally from island to island
- Add transition text when sailing between sea zones
- Add ambient text changes as the voyage progresses (days tracking)

---

## File Structure Changes

```
game/
  engine.py              ← MODIFY: wire topic dialogue, add fish/sail commands
  interactions.py        ← MODIFY: add new give/use combos
  levels/
    __init__.py          ← MODIFY: add level_05_missing_islands
    _shared.py           ← MODIFY: add black_pig, serpent, mill_guardian, etc.
    level_prologue.py    ← already good
    level_00_home.py     ← MODIFY: add return path from homecoming
    level_01_sea1.py     ← MODIFY: add crew NPCs, fix puzzles
    level_02_sea2.py     ← MODIFY: add Wisdom Salmon fishing
    level_03_sea3.py     ← MODIFY: add serpent NPC, revolving castle murderer
    level_04_homecoming.py ← MODIFY: expand endings
    level_05_missing_islands.py ← CREATE: The Mill, Horses, Sheep, Flaming Cat, etc.
console.py               ← no changes needed
playtest.py              ← REWRITE: comprehensive playthrough
```

---

## Implementation Order

1. **Phase 0** — Critical fixes (parallelizable: dialogue wire + NPC creation)
2. **Phase 1** — Missing islands (one subagent per island)
3. **Phase 2** — Existing island completion (parallel: fishing, glass bridge, trumpet, skull, crew, fences, castle, monsters)
4. **Phase 3** — Emotional arc (homecoming, hermit, boy, druid)
5. **Phase 4** — Integration (playtest, score, coherence)
