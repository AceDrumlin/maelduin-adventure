"""Core game engine for The Voyage of Mael Duin."""

import random
import re
import textwrap
import json
import os
import pathlib
import datetime
from .drink_handler import handle_drink


class Item:
    def __init__(self, id, name, description, examine_text=None,
                 takeable=True, aliases=None, usable_with=None,
                 use_text=None):
        self.id = id
        self.name = name
        self.description = description
        self.examine_text = examine_text or description
        self.takeable = takeable
        self.aliases = aliases or []
        self.usable_with = usable_with or []  # list of item ids this can be used with
        self.use_text = use_text

    def match(self, text):
        text = text.lower().strip()
        if text == self.id or text == self.name.lower():
            return True
        for a in self.aliases:
            if text == a.lower():
                return True
        return False


class NPC:
    def __init__(self, id, name, description, dialogue=None,
                 aliases=None, state=None):
        self.id = id
        self.name = name
        self.description = description
        self.dialogue = dialogue or {}  # topic -> response or {"condition": ..., "text": ...}
        self.aliases = aliases or []
        self.state = state or {}

    def match(self, text):
        text = text.lower().strip()
        if text == self.id or text == self.name.lower():
            return True
        for a in self.aliases:
            if text == a.lower():
                return True
        return False


class Location:
    def __init__(self, id, name, description, detailed_desc=None,
                 items=None, npcs=None, exits=None, blocked=None,
                 on_enter=None, on_look=None, ambient=None):
        self.id = id
        self.name = name
        self.description = description
        self.detailed_desc = detailed_desc or description
        self.items = items or []
        self.npcs = npcs or []
        self.exits = exits or {}
        self.blocked = blocked or {}  # dir -> ("blocked message", condition_fn)
        self.on_enter = on_enter  # fn(state) -> str (event text)
        self.on_look = on_look  # fn(state) -> str (additional look text)
        self.ambient = ambient  # fn(state) -> str (ambient description)

    def get_exits_text(self, state):
        available = []
        for d, loc_id in self.exits.items():
            if d in self.blocked:
                cond_fn = self.blocked[d][1]
                if cond_fn and cond_fn(state):
                    available.append(f"{d} ({self.blocked[d][0]})")
                    continue
            available.append(d)
        if not available:
            return ""
        return "Exits: " + ", ".join(available)


class CrewMember:
    def __init__(self, id, name, description, role, alive=True):
        self.id = id
        self.name = name
        self.description = description
        self.role = role
        self.alive = alive


CREW_TEMPLATES = {
    "diuran": {"id": "diuran", "name": "Diurán", "description": "The poet and scribe, always ready with a verse.", "role": "poet"},
    "conganchnes": {"id": "conganchnes", "name": "Conganchnes", "description": "A warrior whose skin cannot be wounded. Terrifying in battle.", "role": "champion"},
    "fergus": {"id": "fergus", "name": "Fergus", "description": "The navigator, who can read the stars and the waves.", "role": "navigator"},
}

# Map prologue NPC IDs to crew template IDs for recruitment
CREW_NPC_MAP = {
    "young_conganchnes": "conganchnes",
    "young_fergus": "fergus",
    "young_diuran": "diuran",
}


class GameState:
    def __init__(self):
        self.current_location = "ailill_keep"
        self.inventory = []
        self.flags = {}
        self.score = 0
        self.turns = 0
        self.days = 0  # in-game days passed
        self.game_over = False
        self.won = False
        self.message_log = []
        self.crew = []  # Start empty — recruit companions through the prologue
        self.dead_crew = []
        self.known_islands = []
        self.awaiting_choice = None  # For choice-based interactions
        self.choice_data = None

    def add_message(self, msg):
        self.message_log.append(msg)

    def get_location(self):
        return LOCATIONS.get(self.current_location)

    def get_item_from_inventory(self, name):
        for item in self.inventory:
            if item.match(name):
                return item
        return None

    def get_npc_at_location(self, name):
        loc = self.get_location()
        if not loc:
            return None
        for npc in loc.npcs:
            if npc.match(name):
                return npc
        return None

    def get_item_at_location(self, name):
        loc = self.get_location()
        if not loc:
            return None
        for item in loc.items:
            if item.match(name):
                return item
        return None

    def find_item(self, name):
        """Find item in inventory or current location."""
        item = self.get_item_from_inventory(name)
        if item:
            return item, "inventory"
        item = self.get_item_at_location(name)
        if item:
            return item, "location"
        return None, None

    def has_flag(self, flag):
        return self.flags.get(flag, False)

    def set_flag(self, flag, value=True):
        self.flags[flag] = value

    def add_crew(self, member_id):
        """Add a crew member by ID if not already in crew."""
        if any(c.id == member_id for c in self.crew):
            return False
        if member_id not in CREW_TEMPLATES:
            return False
        tpl = CREW_TEMPLATES[member_id]
        self.crew.append(CrewMember(**tpl))
        return True

    def total_crew_alive(self):
        return sum(1 for c in self.crew if c.alive)

    def lose_crew(self, member_id=None):
        """Lose a random or specific crew member."""
        alive = [c for c in self.crew if c.alive]
        if member_id:
            member = next((c for c in alive if c.id == member_id), None)
        else:
            member = random.choice(alive) if alive else None
        if member:
            member.alive = False
            self.dead_crew.append(member)
            return member
        return None

    def to_save_dict(self):
        """Serialize to a JSON-safe dict."""
        return {
            "location": self.current_location,
            "inventory_ids": [item.id for item in self.inventory],
            "flags": dict(self.flags),
            "score": self.score,
            "turns": self.turns,
            "days": self.days,
            "game_over": self.game_over,
            "won": self.won,
            "crew": [{"id": c.id, "alive": c.alive} for c in self.crew],
            "awaiting_choice": self.awaiting_choice,
            "visited": dict(getattr(self, 'visited', {})),
        }

    @classmethod
    def from_save_dict(cls, data):
        """Restore state from a save dict."""
        from . import world  # noqa: F401 — populates engine.LOCATIONS and engine.ITEMS
        state = cls()
        state.current_location = data.get("location", "ailill_keep")
        state.score = data.get("score", 0)
        state.turns = data.get("turns", 0)
        state.days = data.get("days", 0)
        state.game_over = data.get("game_over", False)
        state.won = data.get("won", False)
        state.awaiting_choice = data.get("awaiting_choice", None)
        state.flags = dict(data.get("flags", {}))
        state.visited = dict(data.get("visited", {}))
        # Restore visited flags for backward compat
        for loc_id in state.visited:
            state.set_flag(f"{loc_id}_visited", True)
        # Restore inventory from IDs (ITEMS dict populated by world.py)
        for item_id in data.get("inventory_ids", []):
            if item_id in ITEMS:
                state.inventory.append(ITEMS[item_id])
        # Restore crew alive status
        for cdata in data.get("crew", []):
            cid = cdata.get("id")
            existing = next((c for c in state.crew if c.id == cid), None)
            if existing:
                existing.alive = cdata.get("alive", True)
            elif cid in CREW_TEMPLATES:
                # Crew was saved with members; restore them from templates
                tpl = dict(CREW_TEMPLATES[cid])
                tpl["alive"] = cdata.get("alive", True)
                state.crew.append(CrewMember(**tpl))
        return state


# ----- Save/Load Helpers -----

def _get_save_dir():
    """Get the save directory, creating it if needed."""
    save_dir = os.path.expanduser("~/.maelduin/saves")
    os.makedirs(save_dir, exist_ok=True)
    return save_dir

def _sanitize_save_name(name):
    """Sanitize a save name for use as a filename."""
    safe = re.sub(r'[^a-zA-Z0-9_\- ]', '', name).strip()
    return safe if safe else "unnamed"

def _save_path(name):
    return os.path.join(_get_save_dir(), _sanitize_save_name(name) + ".json")

def list_saves():
    """Return list of {name, timestamp} dicts."""
    save_dir = _get_save_dir()
    saves = []
    if os.path.isdir(save_dir):
        for f in sorted(os.listdir(save_dir)):
            if f.endswith(".json"):
                path = os.path.join(save_dir, f)
                name = f[:-5]
                mtime = os.path.getmtime(path)
                ts = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
                saves.append({"name": name, "timestamp": ts, "path": path})
    return saves


# ----- Action Handler -----

def handle_unknown(state, cmd):
    return f"I don't understand \"{cmd}\". Type HELP for a list of commands."


def handle_help(state, args):
    return (
        "=== THE VOYAGE OF MAEL DUIN ===\n\n"
        "Commands:\n"
        "  LOOK / L               - Describe your surroundings\n"
        "  GO [dir] / [dir]       - Move (north/south/east/west/sea)\n"
        "  TAKE [item]            - Pick up an item\n"
        "  DROP [item]            - Drop an item\n"
        "  INVENTORY / I          - Check what you're carrying\n"
        "  EXAMINE / X [item]     - Look closely at something\n"
        "  TALK TO [npc]          - Speak with someone\n"
        "  GIVE [item] TO [npc]   - Offer something\n"
        "  USE [item] [with item] - Use an item\n"
        "  SAIL                   - Set sail on the open sea\n"
        "  FIGHT [target]         - Engage in combat\n"
        "  JOKE TO [npc]          - Tell someone a joke\n"
        "  SING [song]            - Belt out a tune\n"
        "  YES / NO               - Respond to a choice\n"
        "  WAIT / Z               - Pass time\n"
        "  CREW                   - Check on your crew\n"
        "  SCORE                  - See your progress\n"
        "  QUIT / Q               - End the voyage\n"
        "  RESTART                - Start over\n"
        "  SAVE [name]            - Save your game\n"
        "  LOAD [name]            - Load a saved game\n"
        "  SAVES                  - List all saved games\n"
        "  DELETE SAVE [name]     - Delete a saved game\n"
        "  HELP                   - Show this message\n\n"
        "Tip: Try EXAMINE things and TALK TO people!"
    )


def handle_look(state, args):
    loc = state.get_location()
    if not loc:
        return "The void stares back. You are nowhere."
    text = f"\n=== {loc.name} ===\n\n"
    if state.has_flag(f"{loc.id}_visited"):
        text += loc.description + "\n"
    else:
        text += loc.detailed_desc + "\n"
        state.set_flag(f"{loc.id}_visited")

    if loc.items:
        items_desc = ", ".join(i.name for i in loc.items if i.takeable or True)
        if items_desc:
            text += f"\nYou see: {items_desc}\n"
    if loc.npcs:
        for npc in loc.npcs:
            text += f"\n{npc.name} is here.\n"
    if loc.ambient:
        ambient_text = loc.ambient(state)
        if ambient_text:
            text += f"\n{ambient_text}\n"

    crew_str = ", ".join(f"{c.name} ({c.description})" for c in loc.npcs if hasattr(c, 'name') and c in getattr(loc, 'npcs', []))
    text += "\n" + loc.get_exits_text(state)

    if loc.on_look:
        extra = loc.on_look(state)
        if extra:
            text += "\n\n" + extra

    return text


def handle_go(state, direction):
    loc = state.get_location()
    if not loc:
        return "You are lost."

    direction = direction.lower().strip()
    # Map common aliases
    dir_map = {
        "n": "north", "north": "north",
        "s": "south", "south": "south",
        "e": "east", "east": "east",
        "w": "west", "west": "west",
        "ne": "northeast", "northeast": "northeast",
        "nw": "northwest", "northwest": "northwest",
        "se": "southeast", "southeast": "southeast",
        "sw": "southwest", "southwest": "southwest",
        "sea": "sea", "sail": "sea", "out": "sea",
        "in": "in", "inside": "in",
        "u": "up", "up": "up",
        "d": "down", "down": "down",
        "deeper": "deeper", "deep": "deeper",
        "back": "back", "return": "back", "shallows": "shallows",
        "home": "home",
        "homecoming": "homecoming",
        "in": "in", "inside": "in", "enter": "in",
        "cross": "cross", "bridge": "cross",
        "ride": "ride", "mount": "ride",
        "out": "out", "exit": "out", "leave": "out",
        "door": "out",
        "through": "through",
        "climb": "climb",
        "gold": "gold",
        "silver": "silver",
        "copper": "copper",
        "crystal": "crystal",
        "red": "red", "blue": "blue", "green": "green", "black": "black",
        "onward": "onward", "forward": "onward", "time": "onward", "grow": "onward",
    }

    direction = dir_map.get(direction, direction)

    if direction in loc.blocked:
        msg, cond = loc.blocked[direction]
        if cond and cond(state):
            state.add_message(msg)
            return msg

    if direction in loc.exits:
        new_loc_id = loc.exits[direction]
        new_loc = LOCATIONS.get(new_loc_id)
        if new_loc:
            state.current_location = new_loc_id
            state.turns += 1
            result = ""
            if new_loc.on_enter:
                event_text = new_loc.on_enter(state)
                if event_text:
                    result += event_text + "\n\n"
            result += handle_look(state, [])
            return result
        else:
            return f"You try to go {direction} but find nothing there."
    else:
        return f"You cannot go {direction} from here."


def handle_take(state, item_name):
    if not item_name:
        return "Take what?"
    loc = state.get_location()
    if not loc:
        return "There's nothing here."

    item = state.get_item_at_location(item_name)
    if not item:
        return f"You don't see any \"{item_name}\" here."

    if not item.takeable:
        return f"You can't take the {item.name}. {item.description}"

    if len(state.inventory) >= 10:
        return "Your hands are full. Drop something first."
    loc.items.remove(item)
    state.inventory.append(item)
    state.add_message(f"Taken: {item.name}")
    return f"You take the {item.name}."


def handle_drop(state, item_name):
    if not item_name:
        return "Drop what?"
    item = state.get_item_from_inventory(item_name)
    if not item:
        return f"You don't have \"{item_name}\"."

    state.inventory.remove(item)
    loc = state.get_location()
    if loc:
        loc.items.append(item)
    return f"You drop the {item.name}."


def handle_inventory(state, args):
    if not state.inventory:
        return "You are carrying nothing."
    items = "\n".join(f"  - {i.name}: {i.description}" for i in state.inventory)
    return f"You are carrying:\n{items}"


def handle_examine(state, target):
    if not target:
        return "Examine what?"

    # Check inventory
    item = state.get_item_from_inventory(target)
    if item:
        return item.examine_text

    # Check location
    loc = state.get_location()
    if loc:
        item = state.get_item_at_location(target)
        if item:
            return item.examine_text
        npc = state.get_npc_at_location(target)
        if npc:
            return npc.description

    # --- Location-specific examines ---
    if loc and loc.id == "island_revolving_castle":
        wall_targets = {"walls", "wall", "carvings", "stone", "masonry", "obsidian", "foundation"}
        if target.lower().strip() in wall_targets:
            if state.has_flag("castle_unlocked"):
                return "The walls are smooth black obsidian. The entrance has already been opened."
            state.set_flag("castle_unlocked")
            return (
                "You examine the outer walls of the Revolving Castle carefully. "
                "The black obsidian is smooth, almost glassy, but near the base "
                "you find a section where the stone has crumbled away.\n\n"
                "Behind the broken stone, a narrow gap leads into the castle's foundations. "
                "You squeeze through, emerging inside a dark entrance hall.\n\n"
                "The secret entrance is revealed!"
            )

    return f"You see nothing special about \"{target}\"."


def handle_talk(state, npc_name, topic=None):
    if not npc_name:
        return "Talk to whom?"

    # Support "talk to <npc> about <topic>" via inline parsing
    if topic is None and " about " in npc_name.lower():
        parts = npc_name.lower().split(" about ", 1)
        npc_name = parts[0].strip()
        topic = parts[1].strip()

    npc = state.get_npc_at_location(npc_name)
    if not npc:
        return f"There's no one named \"{npc_name}\" here to talk to."

    # If topic was provided, try to get topic-specific dialogue
    if topic:
        try:
            from .interactions import get_talk_topic_response
            topic_result = get_talk_topic_response(state, npc, topic)
            if topic_result is not None:
                return topic_result
            # Topic not found — fall through to greeting
        except (ImportError, Exception):
            pass  # Fall through to greeting

    if "greeting" in npc.dialogue:
        result = npc.dialogue["greeting"]

        # Check if this NPC can be recruited (young companions in prologue)
        if "recruit" in npc.dialogue and not state.has_flag(f"recruited_{npc.id}"):
            if not any(c.id == npc.id for c in state.crew):
                result += "\n\n" + npc.dialogue["recruit"]
                state.awaiting_choice = f"recruit_{npc.id}"
                state.choice_data = {"npc_id": npc.id}

        # Special: Ailill at the keep is gone after his death
        if npc.id == "ailill" and state.has_flag("witnessed_death"):
            return (
                "The hall feels empty now. Ailill Ochair Ága is gone — "
                "cut down on the strand by raiders from the Northern Isles. "
                "The Wolf's Fang leans against his throne, untouched. "
                "His drinking horn sits half-full on the table. "
                "But the Wolf himself will never laugh again.\n\n"
                "You are a ghost in this hall, and the ghost of your father "
                "walks beside you in silence."
            )

        # Special: queen's greeting sets up the stay/leave choice
        if npc.id == "queen" and not state.has_flag("queen_choice_offered"):
            state.set_flag("queen_choice_offered")
            state.awaiting_choice = "queen_stay"
            result += "\n\n(Type YES to stay. Type NO to resist and leave.)"
        # Don't re-offer the choice if already decided
        elif npc.id == "queen" and state.has_flag("queen_choice_offered"):
            pass  # Return the normal greeting without the choice prompt

        return result
    return f"{npc.name} looks at you but says nothing."


def handle_give(state, args):
    # args like "fish to cat" or just "fish" "to" "cat"
    text = args
    parts = re.split(r'\s+to\s+', text, maxsplit=1)
    if len(parts) < 2:
        return "Give what to whom? Usage: GIVE [item] TO [npc]"

    item_name = parts[0].strip()
    npc_name = parts[1].strip()

    item = state.get_item_from_inventory(item_name)
    if not item:
        return f"You don't have \"{item_name}\"."

    npc = state.get_npc_at_location(npc_name)
    if not npc:
        return f"There's no \"{npc_name}\" here."

    # Check if NPC has a take_item handler in dialogue
    if "on_take" in npc.dialogue:
        handler = npc.dialogue["on_take"]
        if isinstance(handler, dict):
            # Check for specific item match first
            if item.id in handler:
                result = handler[item.id](state, item)
                if result:
                    state.inventory.remove(item)
                    return result
            # Check for wildcard (any item)
            if "__any__" in handler:
                result = handler["__any__"](state, item)
                if result:
                    state.inventory.remove(item)
                    return result

    # Fallback: interactions module for contextual responses
    try:
        from .interactions import get_give_response
        return get_give_response(state, item, npc)
    except ImportError:
        pass

    # Default: NPC may not want it
    return f"You offer the {item.name} to {npc.name}. They look at you strangely and don't take it."


def handle_use(state, args):
    if not args or not args.strip():
        return "Use what? Usage: USE [item] [with target]"
    parts = re.split(r'\s+(?:with|on|at|in)\s+', args, maxsplit=1)
    item_name = parts[0].strip()
    target_name = parts[1].strip() if len(parts) > 1 else None

    item, source = state.find_item(item_name)
    if not item:
        return f"You don't have \"{item_name}\"."

    # Find target
    target = None
    if target_name:
        target, _ = state.find_item(target_name)
        if not target:
            target = state.get_npc_at_location(target_name)
        if not target:
            # Before giving up, try registered USE combos from interactions.py
            try:
                from .interactions import get_use_response
                result = get_use_response(state, item, target_name)
                if result:
                    return result
            except (ImportError, Exception):
                pass
            return f"You don't see \"{target_name}\" here."

    if item.usable_with and target:
        if target.id not in item.usable_with and target_name not in item.usable_with:
            return f"You can't use the {item.name} with the {target.name}."

    if item.use_text:
        result = item.use_text
        if callable(item.use_text):
            result = item.use_text(state, target)
        return result

    # Fallback: interactions module
    try:
        from .interactions import get_use_response
        return get_use_response(state, item, target)
    except ImportError:
        pass

    return f"You use the {item.name}. Nothing happens."


def handle_wait(state, args):
    state.turns += 1
    loc = state.get_location()

    # --- Revolving Castle puzzle: wait for the right moment ---
    if loc and loc.id == "island_revolving_castle" and not state.has_flag("castle_unlocked"):
        waits = state.flags.get("castle_waits", 0) + 1
        state.flags["castle_waits"] = waits
        if waits >= 3:
            state.set_flag("castle_unlocked")
            return (
                "You wait. The castle continues its slow, grinding rotation...\n\n"
                "On the third pause, you notice the Red Door lingers at the platform just a little longer than the others. "
                "Long enough for a quick-witted visitor to slip through.\n\n"
                "You seize the moment and dart inside!"
            )
        door_names = ["Red", "Blue", "Green", "Black"]
        return (
            f"You wait. The great castle turns. The {door_names[(waits-1) % 4]} Door "
            "aligns with the platform, pauses, then continues its eternal rotation.\n\n"
            "You'll need to learn the rhythm if you want to get in."
        )

    # --- Generic location on_wait hook if available ---
    if loc and hasattr(loc, 'on_wait') and loc.on_wait:
        result = loc.on_wait(state)
        if result:
            return result

    return "Time passes..."


def handle_crew(state, args):
    if not state.crew:
        return 'You have no crew yet. Find companions to join your voyage by talking to people.'
    alive = [c for c in state.crew if c.alive]
    dead = state.dead_crew
    lines = ["=== YOUR CREW ==="]
    for c in alive:
        lines.append(f"  {c.name} ({c.role}) - {c.description}")
    if dead:
        lines.append("\n--- Lost ---")
        for c in dead:
            lines.append(f"  {c.name} - {c.role}")
    lines.append(f"\n{len(alive)} alive, {len(dead)} lost")
    return "\n".join(lines)


def handle_score(state, args):
    visited = sum(1 for k in state.flags if k.endswith("_visited"))
    items = len(state.inventory)
    crew_alive = state.total_crew_alive()
    return (
        f"=== SCORE ===\n"
        f"Turns: {state.turns}\n"
        f"Score: {state.score}\n"
        f"Islands visited: {visited}\n"
        f"Items carried: {items}\n"
        f"Crew alive: {crew_alive}/{len(state.crew)}\n"
        f"Game over: {state.game_over}"
    )


def handle_quit(state, args):
    state.game_over = True
    return "Your voyage ends here. Farewell, Mael Duin."


def handle_restart(state, args):
    return "__RESTART__"


def handle_save(state, args):
    name = args.strip() if args else None
    if not name:
        return "Usage: SAVE [name] — give your save a name."
    safe = _sanitize_save_name(name)
    path = _save_path(safe)
    blob = {
        "version": 1,
        "save_name": safe,
        "timestamp": datetime.datetime.now().isoformat(),
        "state": state.to_save_dict(),
    }
    with open(path, "w") as f:
        json.dump(blob, f, indent=2)
    return f'Game saved as "{safe}".'


def handle_load(state, args):
    name = args.strip() if args else None
    if not name:
        return "Usage: LOAD [name] — load a previously saved game."
    safe = _sanitize_save_name(name)
    path = _save_path(safe)
    if not os.path.exists(path):
        existing = list_saves()
        if not existing:
            return f'No save named "{safe}" found. No saves exist.'
        names = ", ".join(s["name"] for s in existing)
        return f'No save named "{safe}" found. Available saves: {names}'
    with open(path) as f:
        blob = json.load(f)
    new_state = GameState.from_save_dict(blob["state"])
    # Replace the caller's state in-place
    for attr in ["current_location", "inventory", "flags", "score", "turns", "days",
                 "game_over", "won", "crew", "awaiting_choice", "visited"]:
        setattr(state, attr, getattr(new_state, attr))
    state.message_log = []
    return f'Save "{safe}" loaded. ({blob.get("timestamp", "unknown")})\n\n' + handle_look(state, [])


def handle_list_saves(state, args):
    saves = list_saves()
    if not saves:
        return "No saved games found."
    lines = ["=== SAVED GAMES ==="]
    for s in saves:
        lines.append(f"  {s['name']:20s}  {s['timestamp']}")
    return "\n".join(lines)


def handle_delete_save(state, args):
    name = args.strip() if args else None
    if not name:
        return "Usage: DELETE SAVE [name]"
    safe = _sanitize_save_name(name)
    path = _save_path(safe)
    if os.path.exists(path):
        os.remove(path)
        return f'Save "{safe}" deleted.'
    return f'No save named "{safe}" found.'


def handle_sail(state, args):
    """Special handler for sailing between islands."""
    loc = state.get_location()
    if not loc:
        return "You are lost. You cannot sail from here."

    # Already at sea — sailing is just looking around
    if loc.id in ("sea1", "sea2", "sea3"):
        return "You are already at sea. Try a direction (north/south/east/west) to reach an island."

    # Try to find any exit that leads back to sea
    for direction, target in loc.exits.items():
        if target.startswith("sea"):
            return handle_go(state, direction)

    return "There's nowhere to sail from here. Try a direction (north/south/east/west) to find the sea."


def handle_fight(state, target):
    """Simple combat system."""
    if not target:
        return "Fight what? Use: FIGHT [target]"

    loc = state.get_location()
    if not loc:
        return "There's nothing to fight here."

    # Check for fightable NPCs/creatures via location-specific logic
    if loc.id == "island_giant":
        return _fight_giant(state)
    if loc.id == "treasure_cave":
        return _fight_treasure_serpent(state)
    if loc.id == "island_dog":
        return _fight_hound(state)
    if loc.id == "island_lion":
        return _fight_mountain_lion(state)
    # This is handled by hooks in the world module
    if loc.id == "sea_monsters" and not state.has_flag("sea_monster_defeated"):
        if state.has_flag("got_harpoon"):
            state.set_flag("sea_monster_defeated")
            state.score += 5
            return (
                "You hurl the magic harpoon at the monstrous hand! It strikes true, and "
                "with a roar that shakes the sea, the creature releases the boat and sinks "
                "back into the depths. The water is still once more.\n\n"
                "Your crew cheers. Conganchnes claps you on the back. 'Good throw, Captain!'"
            )
        elif not state.has_flag("monster_attacked_without_harpoon"):
            # Conganchnes can fight it
            conganchnes = next((c for c in state.crew if c.id == "conganchnes"), None)
            if conganchnes and conganchnes.alive:
                state.set_flag("sea_monster_defeated")
                state.score += 3
                return (
                    "Conganchnes leaps onto the monster's hand, his legendary skin "
                    "turning aside its claws! He drives his sword deep into the creature's wrist, "
                    "and with a howl of pain, it releases the boat and sinks beneath the waves.\n\n"
                    "Conganchnes lands back on deck, dripping with ichor. 'Next time, you fight the sea monster.'"
                )
        return (
            "You draw your sword and strike at the monstrous hand! The blade bounces off "
            "its leathery skin. It barely seems to notice. You need a better weapon, or a stronger warrior."
        )

    if loc.id == "black_pig" and not state.has_flag("apple_taken"):
        return (
            "The black pig snorts and charges! Its tusks are the size of daggers. "
            "Before you can react, it bowls you over and stands triumphantly on your chest.\n\n"
            '"OINK," it says, with evident satisfaction. It then wanders back to the tree and goes to sleep.\n\n'
            "You are unharmed, but your pride is in tatters. You were defeated by a pig."
        )

    return "There's nothing to fight here."


def _fight_giant(state):
    if state.has_flag("giant_defeated"):
        return "The giant is already dead. His body lies at the base of the cliff."
    if state.has_flag("giant_mollified"):
        return "The giant is peacefully chewing his food. He ignores you."
    if state.has_flag("giant_encountered") and not state.has_flag("giant_defeated") and not state.has_flag("giant_mollified"):
        if state.get_item_from_inventory("magic_harpoon"):
            state.set_flag("giant_defeated")
            state.score += 3
            from .levels._shared import items as shared_items
            club = shared_items.get("giants_club")
            loc = state.get_location()
            if club and loc:
                loc.items.append(club)
            return (
                "You hurl the Magic Harpoon at the giant. It strikes him square in the chest — "
                "a blow that would kill any mortal man. The giant bellows in pain, tearing at the harpoon, "
                "but the enchanted weapon returns to your hand before he can pull it free.\n\n"
                "He stumbles backward, clutching his wound, and topples from the cliff. The ground shakes "
                "as his body crashes onto the rocks below. The waves wash over him, and he is still.\n\n"
                "At the base of the cliff, his GIANT'S CLUB lies among the rocks.\n\n"
                "(+3 points.)"
            )
        return (
            "You draw your sword and charge, but the giant hurls a stone that smashes into the ground "
            "at your feet. You dive aside, barely avoiding being crushed. You need the Magic Harpoon "
            "to bring this giant down."
        )
    return "There's nothing to fight here."


def _fight_treasure_serpent(state):
    if state.has_flag("serpent_passed"):
        return "The serpent has already been dealt with. The cave is open."
    if state.has_flag("serpent_encountered") and not state.has_flag("serpent_passed"):
        state.set_flag("serpent_passed")
        state.score += 3
        from .levels._shared import items as shared_items
        gold = shared_items.get("treasure_gold")
        loc = state.get_location()
        if gold and loc:
            loc.items.append(gold)
        return (
            "You steel yourself and rush at the serpent with your weapon drawn! It strikes with blinding speed — "
            "but Conganchnes shoves you aside, taking the blow on his invulnerable skin.\n\n"
            "The serpent recoils, hissing in confusion. In that moment, you land a blow on its neck. "
            "It thrashes wildly and retreats deeper into the cave.\n\n"
            "Beyond the entrance, you see the gleam of ANCIENT GOLD. The treasure is yours.\n\n"
            "(+3 points. Ancient Gold lies in the cave.)"
        )
    return "There's nothing to fight here."


def _fight_hound(state):
    if state.has_flag("dog_pacified"):
        return "The great hound is peacefully dozing. It has finally earned its rest."
    if state.has_flag("dog_encountered") or True:
        state.set_flag("dog_pacified")
        state.score += 3
        return (
            "You raise your weapon and face the Great Hound. It does not back down — "
            "it springs at you with jaws wide, but at the last moment, you sidestep and "
            "strike its flank. The hound yelps and retreats, tail between its legs.\n\n"
            "It watches you from a distance as you take the Silver Torc from the pedestal. "
            "It does not interfere.\n\n"
            "(+3 points.)"
        )


def _fight_mountain_lion(state):
    if state.has_flag("lion_pacified") or state.has_flag("lion_fought"):
        return "The mountain lion is gone — driven off or healed."
    state.set_flag("lion_fought")
    state.score += 3
    from .levels._shared import items as shared_items
    claw = shared_items.get("lions_claw")
    loc = state.get_location()
    if claw and loc:
        loc.items.append(claw)
    return (
        "You raise your weapon against the wounded lion. It snarls and lunges — "
        "but its injury slows it. You strike true, and the beast collapses.\n\n"
        "When it falls, one of its claws breaks off. You pick it up — it is razor-sharp "
        "and still warm. The Lion's Claw could serve as a dagger.\n\n"
        "(+3 points. Gained: Lion's Claw)"
    )

    return "There's nothing to fight here."


def handle_joke(state, args):
    """Tell a joke. Used for the Laughing King puzzle."""
    # Auto-target the laughing king if present and no target specified
    if not args or args == "to":
        npc = state.get_npc_at_location("king")
        if npc:
            args = "a joke"
        else:
            return "Tell a joke to whom? Use: JOKE TO [npc] or JOKE [text]"

    # Check if laughing king is here
    npc = state.get_npc_at_location("king")
    if not npc:
        return "There's no one here who wants to hear a joke."

    if state.has_flag("king_pacified"):
        return 'The Laughing King wipes a tear from his eye. "You already told me the best one! I can\'t take another!"'

    # Accept any joke told
    state.set_flag("king_pacified")
    state.score += 2
    # Add laughing potion to location
    from .world import items
    loc = state.get_location()
    if loc and items.get("laughing_potion") and items["laughing_potion"] not in loc.items:
        loc.items.append(items["laughing_potion"])

    return (
        f'You tell a joke: "{args}"\n\n'
        "The Laughing King freezes. His eyes go wide. For a moment, there is silence.\n\n"
        'Then he ERUPTS — laughing so hard he falls off his stool, rolls on the ground, '
        "and pounds the earth with his fists. His subjects are laughing too, but at him, not with him.\n\n"
        '"THAT\'S the one! THAT\'S the BEST joke I\'ve ever heard!" He gasps between gales of laughter. '
        '"Here, take this! It\'s the Laughing Potion — one sip and you\'ll be as happy as me!"\n\n'
        "He tosses you a bubbling vial.\n\n"
        "(+2 points. The island is now quiet — well, quieter.)"
    )


def handle_sing(state, args):
    """Sing a song. Used for various occasions."""
    if not args:
        return "Sing what? Use: SING [song]"

    # Check if Diuran is here or at sea
    loc = state.get_location()
    if loc and loc.id in ("sea1", "sea2", "sea3"):
        return (
            f'You belt out a shanty: "{args}"\n\n'
            "Your crew joins in, their rough voices carrying across the waves. "
            "Diurán quickly scribbles down the lyrics, muttering about copyright."
        )

    return (
        f'You sing: "{args}"\n\n'
        "Your voice cracks slightly on the high notes, but you give it your all. "
        "A nearby seal applauds by slapping its flippers together."
    )


def handle_yes(state, args):
    """Handle YES response to a choice."""
    if state.awaiting_choice and state.awaiting_choice.startswith('recruit_'):
        npc_id = state.awaiting_choice.replace('recruit_', '')
        crew_id = CREW_NPC_MAP.get(npc_id, npc_id)
        name = CREW_TEMPLATES.get(crew_id, {}).get("name", npc_id.capitalize())
        if state.add_crew(crew_id):
            state.set_flag(f"recruited_{npc_id}")
            state.awaiting_choice = None
            return f'"{name} joins your crew!"'
        else:
            state.awaiting_choice = None
            return f"{name} is already in your crew."
    elif state.awaiting_choice == "queen_stay":
        return _queen_stay_choice(state)
    elif state.awaiting_choice == "ending" or state.awaiting_choice == "ending_forgiven":
        if state.awaiting_choice == "ending_forgiven":
            state.set_flag("ending_decided")
        return _ending_forgive_choice(state)
    elif state.awaiting_choice == "ending_vengeance":
        state.set_flag("ending_decided")
        return _ending_vengeance_choice(state)
    elif state.awaiting_choice == "homecoming_leave":
        state.set_flag("left_women")
        state.current_location = "sea1"
        return handle_look(state, [])
    elif state.awaiting_choice == "palace_stay":
        state.set_flag("stayed_in_palace")
        state.days += 14
        state.score += 1
        return (
            'You stay. "Yes," you whisper. "I will stay."\n\n'
            "The woman's smile widens. The days blur into weeks. The enchantment wraps around you like silk...\n\n"
            "But you were born of the sea, and the sea calls to you. You wake one morning, pack your things, "
            "and leave before the woman wakes. Your crew follows, bleary-eyed but loyal.\n\n"
            "You have lost time, but not your purpose. The voyage continues."
        )
    elif state.awaiting_choice == "promised_land":
        state.set_flag("stayed_in_promised_land")
        state.game_over = True
        state.won = True
        state.awaiting_choice = None
        islands_visited = sum(1 for k in state.flags if k.endswith("_visited") and not k.startswith("ailill") and not k.startswith("foster") and not k.startswith("training") and not k.startswith("feast") and not k.startswith("druid") and not k.startswith("village") and not k.startswith("fathers"))
        state.score += islands_visited * 3
        return (
            'You say YES.\n\n'
            "The Guardian of Peace smiles — a smile that contains the warmth of a thousand suns.\n\n"
            "'You have chosen well, Mael Duin. You have crossed the edges of the world, "
            "braved wonders and horrors, and now you have come home to the place that was always waiting for you.'\n\n"
            "Your crew steps forward, one by one, and the shimmering land enfolds them.\n\n"
            "There is no pain here. No hunger. No death. The rivers run with wine and honey.\n\n"
            "You stay. Forever.\n\n"
            "=== THE END ===\n"
            "Thank you for playing The Voyage of Mael Duin.\n"
            f"Final score: {state.score} | "
            f"Islands visited: {islands_visited}\n\n"
            '"The Promised Land is not a place. It is a decision."'
        )
    return "Yes to what? There's no pending choice."


def handle_no(state, args):
    """Handle NO response to a choice."""
    if state.awaiting_choice and state.awaiting_choice.startswith('recruit_'):
        state.awaiting_choice = None
        return 'Very well. Perhaps another time. You can talk to them again if you change your mind.'
    elif state.awaiting_choice == "queen_stay":
        state.set_flag("resisted_queen")
        state.score += 5
        state.awaiting_choice = None
        return (
            '"No," you say firmly. "We must continue our voyage."\n\n'
            "The Queen's smile flickers. For a moment, you see something ancient and cold in her eyes. "
            "Then she laughs — a sound like breaking glass.\n\n"
            '"As you wish, Mael Duin. But remember: not all who stay are prisoners, '
            "and not all who leave are free.\"\n\n"
            "She waves her hand, and you find yourself back on your curragh, "
            "bobbing on the open sea. Days — or weeks? — have passed. "
            "Your crew looks older, wearier. They remember everything.\n\n"
            "You have resisted the ultimate temptation."
        )
    elif state.awaiting_choice == "ending":
        return _ending_vengeance_choice(state)
    elif state.awaiting_choice == "ending_forgiven":
        # Already chose forgiveness at the castle — can't undo that now
        return "You have already made your choice. The path of forgiveness cannot be undone."
    elif state.awaiting_choice == "ending_vengeance":
        return "You have already made your choice. The path of vengeance cannot be undone."
    elif state.awaiting_choice == "palace_stay":
        state.set_flag("left_palace")
        state.score += 3
        state.awaiting_choice = None
        return (
            '"No," you say firmly. "I must continue my quest."\n\n'
            "The woman's smile does not waver. 'As you wish, Mael Duin. "
            "The palace will remember you.'\n\n"
            "You turn and walk back across the glass bridge. "
            "The wind is cold, but it is real. You are free."
        )
    elif state.awaiting_choice == "promised_land":
        state.awaiting_choice = None
        state.set_flag("refused_promised_land")
        state.score += 5
        from .levels._shared import items as items_mod
        wind = items_mod.get("wind_of_return")
        if wind and wind not in state.inventory:
            state.inventory.append(wind)
        return (
            'You shake your head. "No," you say firmly. "I cannot stay. There is a life waiting for me — '
            "a home, a people, a story that is not yet finished.'\n\n"
            "The Guardian of Peace nods slowly, its expression unchanged — still warm, still kind.\n\n"
            "'I understand. The world beyond calls to you. Your story is not yet finished. "
            "Take this — the Wind of Return. When you are ready, use it to sail home. "
            "It will carry you across the sea with unerring certainty.'\n\n"
            "The Guardian places a sealed glass bottle in your hands. Inside, a tiny whirlwind spins endlessly.\n\n"
            "'Go with my blessing, Mael Duin. And remember: you carry home with you now.'\n\n"
            "(+5 points. Gained: Wind of Return)"
        )
    return "No to what? There's no pending choice."


def handle_number_choice(state, num_str):
    """Handle numeric choice response."""
    try:
        num = int(num_str)
    except ValueError:
        return None  # Not a number choice

    if state.awaiting_choice == "smith_trade":
        items_list = state.choice_data or []
        if 1 <= num <= len(items_list):
            chosen = items_list[num - 1]
            state.inventory.remove(chosen)
            state.score += 3
            state.awaiting_choice = None

            # Give the harpoon
            from .world import items
            if items.get("magic_harpoon") and items["magic_harpoon"] not in state.inventory:
                state.inventory.append(items["magic_harpoon"])

            return (
                f'You hand over {chosen.name}. The giant smith examines it, grunts, and tosses it into the forge.\n\n'
                '"Fair trade, little man. Fair trade."\n\n'
                "He works the bellows, and the ground shakes. Sparks fly like fireworks. "
                "After an hour of ear-splitting hammering, he presents you with a MAGIC HARPOON — "
                "dark iron etched with spirals, humming with power.\n\n"
                '"This harpoon always returns to its thrower. Don\'t lose it. Well, you CAN lose it, but it\'ll come back. '
                "You know what I mean.\"\n\n"
                "(+3 points. Gained: Magic Harpoon)"
            )
        else:
            return f"Choose a number between 1 and {len(items_list)}."

    return None


# ----- Choice helpers -----

def _queen_stay_choice(state):
    """The player chose to stay with the Queen."""
    state.set_flag("stayed_with_queen")
    state.days += 30  # A month passes
    state.score += 1

    # Random crew loss
    alive = [c for c in state.crew if c.alive]
    if alive:
        lost = random.choice(alive)
        lost.alive = False
        state.dead_crew.append(lost)

    state.current_location = "sea1"
    state.current_location = "sea1"
    state.awaiting_choice = None
    return (
        "You stay. Days turn to weeks. Weeks to months.\n\n"
        "The feasts are glorious. The wine flows like rivers. The Queen's laughter is music, "
        "and her touch is fire. Your crew forgets the voyage. You almost forget your father.\n\n"
        "But one morning, you wake to find one of your crew has vanished. Then another. "
        "The beautiful women grow pale and thin. The food tastes like ash.\n\n"
        "You gather what remains of your crew and flee to the curragh. "
        "As you push off from shore, the Queen watches from the palace steps, smiling her cold smile.\n\n"
        "Months have passed in the real world. Your crew is smaller. Your quest feels more urgent than ever.\n\n"
        f"(You lost {lost.name if 'lost' in dir() else 'a crew member'} to the Queen's enchantment. "
        "30 days have passed.)"
    )


def _ending_forgive_choice(state):
    """The player chose forgiveness in the ending."""
    state.awaiting_choice = None
    state.game_over = True
    state.won = True

    # Calculate final score
    islands_visited = sum(1 for k in state.flags if k.endswith("_visited") and not k.startswith("ailill") and not k.startswith("foster") and not k.startswith("training") and not k.startswith("feast") and not k.startswith("druid") and not k.startswith("village") and not k.startswith("fathers"))
    state.score += islands_visited * 2

    return (
        'You lower your sword.\n\n'
        '"Go," you say. "I did not sail across the edge of the world, visit thirty islands, '
        'fight giant ants and talking cats and laughing kings, to become the same kind of man who killed my father."\n\n'
        "The raiders stare at you. The eldest — grey-bearded, one-eyed — nods slowly.\n\n"
        '"Your father was a good man," he says. "He died well. I have carried his death '
        "like a stone in my chest ever since. Thank you, Mael Duin, for lifting it.\"\n\n"
        "They leave their weapons on the sand and walk away into the mist.\n\n"
        "Your crew gathers around you. Diurán is weeping. Conganchnes sheathes his sword. "
        "Fergus puts a hand on your shoulder.\n\n"
        '"Well," says the poet, "that\'s a better ending than I\'d written."\n\n'
        "You return to your village a different man. The druid is waiting for you by the fire. "
        "He smiles — the first time you've ever seen him smile.\n\n"
        '"I see the sea has taught you what I could not," he says.\n\n'
        "=== THE END ===\n"
        "Thank you for playing The Voyage of Mael Duin.\n"
        f"Final score: {state.score} | "
        f"Islands visited: {islands_visited} | "
        f"Days at sea: {state.days} | "
        f"Crew survived: {state.total_crew_alive()}/{len(state.crew)}\n\n"
        '"Forgiveness is a cup that fills the drinker."'
    )


def _ending_vengeance_choice(state):
    """The player chose vengeance in the ending."""
    state.awaiting_choice = None
    state.game_over = True
    state.won = True

    # Calculate final score
    islands_visited = sum(1 for k in state.flags if k.endswith("_visited") and not k.startswith("ailill") and not k.startswith("foster") and not k.startswith("training") and not k.startswith("feast") and not k.startswith("druid") and not k.startswith("village") and not k.startswith("fathers"))
    state.score += islands_visited

    return (
        'You raise your sword.\n\n'
        '"For my father!" you cry, and your crew charges with you.\n\n'
        "The battle is short and brutal. Conganchnes cuts through three men before they can draw breath. "
        "The grey-bearded raider falls to his knees before you, and you drive your blade home.\n\n"
        "It is done. Your father is avenged.\n\n"
        "But as you stand over the body, you feel... empty. The prophecy scroll hangs heavy in your pack. "
        "Diurán has stopped writing. He has nothing to say.\n\n"
        "You return to your village a victor. The druid is waiting. He looks at you with sad eyes.\n\n"
        '"You have your revenge, Mael Duin. I hope it keeps you warm at night."\n\n'
        "It doesn't.\n\n"
        "=== THE END ===\n"
        "Thank you for playing The Voyage of Mael Duin.\n"
        f"Final score: {state.score} | "
        f"Islands visited: {islands_visited} | "
        f"Days at sea: {state.days} | "
        f"Crew survived: {state.total_crew_alive()}/{len(state.crew)}\n\n"
        '"Vengeance is a cup that empties the drinker."'
    )


# ----- Parser -----

VERBS = {
    "look": ("look", handle_look),
    "l": ("look", handle_look),
    "go": ("go", handle_go),
    "north": ("go", lambda s, a: handle_go(s, "north")),
    "n": ("go", lambda s, a: handle_go(s, "north")),
    "south": ("go", lambda s, a: handle_go(s, "south")),
    "s": ("go", lambda s, a: handle_go(s, "south")),
    "east": ("go", lambda s, a: handle_go(s, "east")),
    "e": ("go", lambda s, a: handle_go(s, "east")),
    "west": ("go", lambda s, a: handle_go(s, "west")),
    "w": ("go", lambda s, a: handle_go(s, "west")),
    "northeast": ("go", lambda s, a: handle_go(s, "northeast")),
    "ne": ("go", lambda s, a: handle_go(s, "northeast")),
    "northwest": ("go", lambda s, a: handle_go(s, "northwest")),
    "nw": ("go", lambda s, a: handle_go(s, "northwest")),
    "southeast": ("go", lambda s, a: handle_go(s, "southeast")),
    "se": ("go", lambda s, a: handle_go(s, "southeast")),
    "southwest": ("go", lambda s, a: handle_go(s, "southwest")),
    "sw": ("go", lambda s, a: handle_go(s, "southwest")),
    "up": ("go", lambda s, a: handle_go(s, "up")),
    "u": ("go", lambda s, a: handle_go(s, "up")),
    "down": ("go", lambda s, a: handle_go(s, "down")),
    "d": ("go", lambda s, a: handle_go(s, "down")),
    "take": ("take", handle_take),
    "get": ("take", handle_take),
    "pick": ("take", handle_take),
    "drop": ("drop", handle_drop),
    "discard": ("drop", handle_drop),
    "inventory": ("inventory", handle_inventory),
    "i": ("inventory", handle_inventory),
    "examine": ("examine", handle_examine),
    "x": ("examine", handle_examine),
    "talk": ("talk", handle_talk),
    "speak": ("talk", handle_talk),
    "give": ("give", handle_give),
    "use": ("use", handle_use),
    "wait": ("wait", handle_wait),
    "z": ("wait", handle_wait),
    "drink": ("drink", handle_drink),
    "crew": ("crew", handle_crew),
    "score": ("score", handle_score),
    "quit": ("quit", handle_quit),
    "q": ("quit", handle_quit),
    "restart": ("restart", handle_restart),
    "sail": ("sail", handle_sail),
    "fight": ("fight", handle_fight),
    "attack": ("fight", handle_fight),
    "joke": ("joke", handle_joke),
    "sing": ("sing", handle_sing),
    "yes": ("yes", handle_yes),
    "y": ("yes", handle_yes),
    "no": ("no", handle_no),
    "nope": ("no", handle_no),
    "help": ("help", handle_help),
    "?": ("help", handle_help),
    "h": ("help", handle_help),
    "save": ("save", handle_save),
    "load": ("load", handle_load),
    "saves": ("saves", handle_list_saves),
    "delete": ("delete", handle_delete_save),
}


def parse_command(text):
    """Parse a command string into (handler, args) tuple.
    Returns (handler_function, args_string) or (None, text) if unknown."""

    text = text.strip()
    if not text:
        return None, ""

    text = re.sub(r'\s+', ' ', text)

    # Check direct verb matches first
    lower = text.lower()
    words = lower.split()

    # Handle multi-word commands like "talk to npc" or "look at item"
    look_patterns = [
        r'^look at\s+(.+)$', r'^look\s+(.+)$', r'^l\s+(.+)$',
        r'^examine\s+(.+)$', r'^x\s+(.+)$',
    ]
    for pat in look_patterns:
        m = re.match(pat, lower)
        if m:
            return (handle_examine, m.group(1).strip())

    talk_patterns = [
        r'^talk to\s+(.+)$', r'^talk with\s+(.+)$',
        r'^speak to\s+(.+)$', r'^speak with\s+(.+)$',
    ]
    # Also check for bare "talk to" with no target
    if lower in ('talk to', 'speak to', 'talk with', 'speak with'):
        return lambda s, a: 'Talk to whom?', ""
    for pat in talk_patterns:
        m = re.match(pat, lower)
        if m:
            return (handle_talk, m.group(1).strip())

    give_pattern = r'^give\s+(.+)$'
    m = re.match(give_pattern, lower)
    if m:
        return (handle_give, m.group(1).strip())

    use_pattern = r'^use\s+(.+)$'
    m = re.match(use_pattern, lower)
    if m:
        return (handle_use, m.group(1).strip())

    take_patterns = [
        r'^take\s+(.+)$', r'^get\s+(.+)$', r'^pick up\s+(.+)$',
    ]
    for pat in take_patterns:
        m = re.match(pat, lower)
        if m:
            return (handle_take, m.group(1).strip())

    drop_patterns = [
        r'^drop\s+(.+)$', r'^discard\s+(.+)$',
    ]
    for pat in drop_patterns:
        m = re.match(pat, lower)
        if m:
            return (handle_drop, m.group(1).strip())

    # Joke pattern: "joke to [npc]" or "joke [text]"
    joke_pattern = r'^joke to\s+(.+)$'
    m = re.match(joke_pattern, lower)
    if m:
        return (handle_joke, m.group(1).strip())
    joke_pattern2 = r'^joke\s+(.+)$'
    m = re.match(joke_pattern2, lower)
    if m:
        return (handle_joke, m.group(1).strip())

    # Fight pattern: "fight [target]"
    fight_pattern = r'^fight\s+(.+)$'
    m = re.match(fight_pattern, lower)
    if m:
        return (handle_fight, m.group(1).strip())
    attack_pattern = r'^attack\s+(.+)$'
    m = re.match(attack_pattern, lower)
    if m:
        return (handle_fight, m.group(1).strip())

    # Sing pattern: "sing [song]"
    sing_pattern = r'^sing\s+(.+)$'
    m = re.match(sing_pattern, lower)
    if m:
        return (handle_sing, m.group(1).strip())

    # Delete save pattern: "delete save [name]"
    delete_save_pattern = r'^delete save\s+(.+)$'
    m = re.match(delete_save_pattern, lower)
    if m:
        return (handle_delete_save, m.group(1).strip())

    # Single word commands
    first_word = words[0]
    if first_word in VERBS:
        _, handler = VERBS[first_word]
        rest = " ".join(words[1:])
        return (handler, rest)

    # Check if it's a direction alias
    dir_aliases = {
        "n": "north", "s": "south", "e": "east", "w": "west",
        "ne": "northeast", "nw": "northwest",
        "se": "southeast", "sw": "southwest",
        "u": "up", "d": "down",
        "deeper": "deeper", "deep": "deeper",
        "back": "back", "return": "back", "shallows": "shallows",
        "home": "home",
        "homecoming": "homecoming",
        "in": "in", "inside": "in", "enter": "in",
        "cross": "cross", "bridge": "cross",
        "ride": "ride", "mount": "ride",
        "out": "out", "exit": "out", "leave": "out",
        "door": "out",
        "through": "through",
        "climb": "climb", "up": "up",
        "gold": "gold",
        "silver": "silver",
        "copper": "copper",
        "crystal": "crystal",
        "red": "red", "blue": "blue", "green": "green", "black": "black",
        "onward": "onward", "forward": "onward", "time": "onward", "grow": "onward",
        # New island navigation (from original immram)
        "harbor": "harbor", "village": "harbor",
        "horses": "horses", "cat": "cat", "oxen": "oxen", "well": "well",
        "mill": "mill", "sheep": "sheep", "wall": "wall",
        "beach": "beach", "strand": "beach",
        "hill": "hill",
        # Final islands (level 07)
        "giant": "giant", "treasure": "treasure", "dog": "dog",
        "lion": "lion", "anchorite": "anchorite",
    }
    if first_word in dir_aliases:
        return (lambda s, a: handle_go(s, dir_aliases[first_word]), "")

    return None, text


def process_command(state, text):
    """Process a command and return response text."""
    if not text or not text.strip():
        return "Type HELP for a list of commands, or just start exploring!"

    handler, args = parse_command(text)
    if handler is None:
        return handle_unknown(state, args)

    return handler(state, args)


# LOCATIONS will be imported/defined elsewhere
# This is the forward declaration for the module
LOCATIONS = {}
ITEMS = {}  # Populated by world.py
