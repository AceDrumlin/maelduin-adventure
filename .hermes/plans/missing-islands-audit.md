# Missing Islands Audit — The Voyage of Mael Duin

Comparing current game (~26 islands) against the original ~33 islands from Immram Curaig Maíle Dúin (Kuno Meyer translation):

## Still Missing from Original:

1. **Island of the Giant Killer** — a giant kills a crew member with a stone. Need: giant NPC, crew-loss consequence, possible trick to avoid
2. **Island of the Fountain** — a magical fountain whose water turns to milk. Need: fountain puzzle, choice (drink/avoid)
3. **The Great Fish / Fish Monster** — a giant fish swallows the boat; crew escapes by cutting its belly. Need: unique survival encounter
4. **Island of the Treasure (Serpent-guarded)** — golden treasure guarded by serpent. Need: treasure room, serpent guardian
5. **The Promised Land / Edenic Island** — river of wine, golden trees, supernatural peace. Need: final peaceful island before homecoming
6. **Island of Silenced Music** — music is forbidden, eerie silence. Need: atmosphere puzzle
7. **Island of the Dog** — a dog guarding a treasure. Need: small encounter
8. **Island of the Lion** — a lion that kills. Need: fight-or-flight encounter

## Underdeveloped Existing Content:

9. **Revolving Castle** — has interior rooms and Garbh but NO real puzzle. Original: castle spins so gate is never facing visitors. Need: timing/trick puzzle to enter
10. **Wall of Water** — needs a proper "use thread on mast" or "use bell" to pass through to sea3
11. **Homecoming path** — no clear way to go from sea → homecoming. Need exit added to sea3

## Architecture Context

Items/NPCs defined in: `game/levels/_shared.py`
New level likely: `game/levels/level_06_missing_islands_2.py` (registered in __init__.py)
Or add to existing levels if they fit a sea hub
