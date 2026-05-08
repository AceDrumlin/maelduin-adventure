"""Core game engine for The Voyage of Mael Duin."""

import random
import re
import textwrap


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


class GameState:
    def __init__(self):
        self.current_location = "home"
        self.inventory = []
        self.flags = {}
        self.score = 0
        self.turns = 0
        self.game_over = False
        self.won = False
        self.message_log = []
        self.crew = [
            CrewMember("diuran", "Diurán", "The poet and scribe, always ready with a verse.", "poet"),
            CrewMember("conganchnes", "Conganchnes", "A warrior whose skin cannot be wounded. Terrifying in battle.", "champion"),
            CrewMember("fergus", "Fergus", "The navigator, who can read the stars and the waves.", "navigator"),
        ]
        self.dead_crew = []
        self.known_islands = []

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
        "  WAIT / Z               - Pass time\n"
        "  CREW                   - Check on your crew\n"
        "  SCORE                  - See your progress\n"
        "  QUIT / Q               - End the voyage\n"
        "  RESTART                - Start over\n"
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

    return f"You see nothing special about \"{target}\"."


def handle_talk(state, npc_name):
    if not npc_name:
        return "Talk to whom?"
    npc = state.get_npc_at_location(npc_name)
    if not npc:
        return f"There's no one named \"{npc_name}\" here to talk to."

    if "greeting" in npc.dialogue:
        return npc.dialogue["greeting"]
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
        if isinstance(handler, dict) and item.id in handler:
            result = handler[item.id](state, item)
            if result:
                state.inventory.remove(item)
                return result

    # Default: NPC may not want it
    return f"You offer the {item.name} to {npc.name}. They look at you strangely and don't take it."


def handle_use(state, args):
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
            return f"You don't see \"{target_name}\" here."

    if item.usable_with and target:
        if target.id not in item.usable_with and target_name not in item.usable_with:
            return f"You can't use the {item.name} with the {target.name}."

    if item.use_text:
        result = item.use_text
        if callable(item.use_text):
            result = item.use_text(state, target)
        return result

    return f"You use the {item.name}. Nothing happens."


def handle_wait(state, args):
    state.turns += 1
    return "Time passes..."


def handle_crew(state, args):
    alive = [c for c in state.crew if c.alive]
    dead = state.dead_crew
    lines = ["=== YOUR CREW ==="]
    for c in alive:
        lines.append(f"  {c.name} ({c.role}) - {c.description}")
    if dead:
        lines.append("\n--- Lost ---")
        for c in dead:
            lines.append(f"  {c.name} - {c.role}")
    lines.append(f"\n{alive} alive, {len(dead)} lost")
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


def handle_sail(state, args):
    """Special handler for sailing between islands."""
    loc = state.get_location()
    if not loc or loc.id == "home":
        return "You are on land. You need to be at sea or on the shore to sail."
    if "sea" in loc.exits or "sea" in state.flags:
        return handle_go(state, "sea")
    return "There's nowhere to sail from here."


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
    "crew": ("crew", handle_crew),
    "score": ("score", handle_score),
    "quit": ("quit", handle_quit),
    "q": ("quit", handle_quit),
    "restart": ("restart", handle_restart),
    "sail": ("sail", handle_sail),
    "help": ("help", handle_help),
    "?": ("help", handle_help),
    "h": ("help", handle_help),
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
    }
    if first_word in dir_aliases:
        return (lambda s, a: handle_go(s, dir_aliases[first_word]), "")

    return None, text


def process_command(state, text):
    """Process a command and return response text."""
    handler, args = parse_command(text)
    if handler is None:
        return handle_unknown(state, args)

    return handler(state, args)


# LOCATIONS will be imported/defined elsewhere
# This is the forward declaration for the module
LOCATIONS = {}
