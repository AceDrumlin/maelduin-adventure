#!/usr/bin/env python3
"""Export all game data to JSON for the static JS frontend.
Run this to regenerate docs/game_data.json after changing game content.
"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from game.engine import LOCATIONS
from game import world

def serialize_item(item):
    return {
        "id": item.id,
        "name": item.name,
        "description": item.description,
        "examine": item.examine_text,
        "takeable": item.takeable,
        "aliases": item.aliases,
        "usable_with": item.usable_with,
        "use_text": item.use_text if isinstance(item.use_text, str) else None,
    }

# Known visibility conditions for key NPCs (matching the Python visible_if lambdas)
# These are derived from the _shared.py definitions and engine added_later patches
KNOWN_VISIBLE_IF = {
    "ailill": {"not_flag": "witnessed_death"},
    "mother": {"not_flag": "witnessed_death"},
    "beach_mother": {"flag": "witnessed_death"},
    "young_conganchnes": {"not_flag": "recruited_young_conganchnes"},
    "young_fergus": {"not_flag": "recruited_young_fergus"},
    "young_diuran": {"not_flag": "recruited_young_diuran"},
    "giant": {"not_any": ["giant_defeated", "giant_mollified"]},
    "treasure_serpent": {"not_flag": "serpent_passed"},
    "great_hound": {"not_flag": "dog_pacified"},
    "mountain_lion": {"not_any": ["lion_fought", "lion_pacified"]},
    "black_pig": {"not_flag": "pig_pacified"},
    "serpent": {"not_flag": "serpent_calmed"},
}

def serialize_npc(npc):
    dialogue = {}
    for key, val in npc.dialogue.items():
        if key == "on_take":
            if isinstance(val, dict):
                dialogue[key] = {k: True for k in val.keys()}
        elif isinstance(val, str):
            dialogue[key] = val
        elif isinstance(val, tuple):
            dialogue[key] = val[0] if val else val
    return {
        "id": npc.id,
        "name": npc.name,
        "description": npc.description,
        "aliases": npc.aliases,
        "dialogue": dialogue,
        "state": npc.state,
        "visible_if": KNOWN_VISIBLE_IF.get(npc.id),
    }

def serialize_location(loc_id, loc):
    data = {
        "id": loc.id,
        "name": loc.name,
        "description": loc.description,
        "detailed_desc": loc.detailed_desc,
        "items": [i.id for i in loc.items],
        "npcs": [n.id for n in loc.npcs],
        "exits": dict(loc.exits),
        "blocked": {d: msg for d, (msg, _) in loc.blocked.items()},
    }
    return data

def export_all():
    # Collect all data
    items_data = {}
    npcs_data = {}
    locations_data = {}

    # Load the game to populate LOCATIONS
    from game.engine import LOCATIONS
    from game.levels._shared import items, npcs

    for iid, item in items.items():
        items_data[iid] = serialize_item(item)

    for nid, npc in npcs.items():
        npcs_data[nid] = serialize_npc(npc)

    for lid, loc in LOCATIONS.items():
        locations_data[lid] = serialize_location(lid, loc)

    # Crew data
    from game.engine import GameState
    temp_state = GameState()
    crew_data = []
    for c in temp_state.crew:
        crew_data.append({
            "id": c.id,
            "name": c.name,
            "description": c.description,
            "role": c.role,
        })

    # Build the full game data bundle
    game_data = {
        "version": "1.0",
        "items": items_data,
        "npcs": npcs_data,
        "locations": locations_data,
        "crew": crew_data,
    }

    return game_data

if __name__ == "__main__":
    data = export_all()
    out_path = os.path.join(os.path.dirname(__file__), "..", "docs", "game_data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(data['items'])} items, {len(data['npcs'])} NPCs, {len(data['locations'])} locations")
    print(f"Written to: {out_path}")
    print(f"File size: {os.path.getsize(out_path):,} bytes")
