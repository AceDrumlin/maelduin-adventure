"""Level: 05 Missing Islands — 7 new islands from the original immram."""

from ..engine import LOCATIONS, Location


def register(items, npcs):
    """Register this level's locations and add exits to sea hubs."""
    l = {}
    from .. import engine as _eng

    # ===================================================
    # Helper: register new direction aliases so players
    # can type single-word navigation commands
    # ===================================================
    _eng.VERBS["horses"] = ("go", lambda s, a: _eng.handle_go(s, "horses"))
    _eng.VERBS["cat"] = ("go", lambda s, a: _eng.handle_go(s, "cat"))
    _eng.VERBS["oxen"] = ("go", lambda s, a: _eng.handle_go(s, "oxen"))
    _eng.VERBS["well"] = ("go", lambda s, a: _eng.handle_go(s, "well"))

    # ===================================================
    # ISLAND 1: THE MILL OF THE SEA
    # (connects from sea2, direction: northeast)
    # ===================================================

    l["mill_exterior"] = Location(
        "mill_exterior", "The Mill of the Sea — Exterior",
        "A towering mill of black stone stands on a cliff, its great wheel dipping into the sea and churning the water into foam.",
        detailed_desc=(
            "A massive MILL of black stone dominates this island. It stands on a cliff at the edge of the sea, "
            "and its great wheel — as wide as your entire curragh — dips into the water, churning the sea into white foam. "
            "The grinding noise is immense — a deep, rhythmic GRIND-GRIND-GRIND that you feel in your teeth.\n\n"
            "The sea around the island is violent — whirlpools form and dissolve where the wheel churns. "
            "The water looks milk-white from the constant grinding.\n\n"
            "An old man shuffles near the entrance to the mill, muttering to himself. "
            "He does not seem to have noticed you yet.\n\n"
            "A stone archway leads INTO the mill proper. The grinding is louder from inside."
        ),
        items=[],
        npcs=[npcs["mill_guardian"]],
        exits={"in": "mill_interior", "enter": "mill_interior", "southwest": "sea2", "back": "sea2"},
        ambient=lambda s: (
            "GRIND... GRIND... GRIND... The mill never stops. The sea never stops. "
            "The old man shuffles in endless circles."
            if not s.has_flag("mill_stopped") else
            "It is quiet now. The silence is so profound it feels like a physical presence. "
            "The old man sits on a stone, weeping silently with joy."
        ),
        on_enter=lambda s: (
            "The grinding of the mill is deafening. Your crew covers their ears.\n\n"
            "'We cannot sail past this island,' Fergus shouts over the noise. "
            "'The whirlpools will tear us apart! We must stop that mill somehow!'\n\n"
            "You can enter the mill through the archway."
            if not s.has_flag("mill_stopped") else None
        ),
    )

    l["mill_interior"] = Location(
        "mill_interior", "The Mill of the Sea — Grinding Chamber",
        "Inside the mill. Great bronze gears the size of houses turn slowly, meshing with crushing force. The floor vibrates.",
        detailed_desc=(
            "You step inside the mill, and the noise doubles. Great GEARS of bronze and iron turn in the dim light — "
            "each one the size of a house, meshing with a force that could crush stone to powder.\n\n"
            "In the center of the chamber, a massive MILLSTONE — a wheel of black granite taller than three men — "
            "grinds against a stone base. Between them, seawater pours in and emerges as... nothing. "
            "It simply disappears, ground into the fabric of reality.\n\n"
            "A fragment of the millstone lies on the floor — broken off, perhaps by a previous visitor who tried and failed "
            "to stop the mill. It is HEAVY.\n\n"
            "The gears turn with terrible purpose. If you could jam something into them — something heavy and strong — "
            "you might stop the wheel. The old guardian said you can only 'feed' the mill. "
            "Perhaps that is the answer: give it something heavy enough to choke on."
        ),
        items=[items["millstone_fragment"]],
        npcs=[],
        exits={"out": "mill_exterior", "back": "mill_exterior"},
        ambient=lambda s: (
            "The gears groan. The stone grinds. The sea boils outside. "
            "You feel like you are standing inside the heartbeat of a dying world."
            if not s.has_flag("mill_stopped") else
            "The silence is beautiful. You can hear your own thoughts for the first time in hours."
        ),
    )

    # ===================================================
    # ISLAND 2: ISLAND OF BLACK & WHITE SHEEP
    # (connects from sea2, direction: southwest)
    # ===================================================

    l["island_sheep"] = Location(
        "island_sheep", "Island of Black & White Sheep",
        "An island split down the middle — a field of black grass on one side, white grass on the other. Sheep cross between them and change color as they walk.",
        detailed_desc=(
            "This island is divided into two perfect halves.\n\n"
            "To the left, a field of BLACK grass, so dark it seems to drink the light. "
            "White sheep graze there, but as you watch, one crosses the invisible boundary — "
            "and the moment it steps onto the black grass, its fleece turns BLACK. "
            "It continues grazing, apparently unconcerned by its transformation.\n\n"
            "To the right, a field of WHITE grass, so pale it glows faintly. "
            "Black sheep graze there, turning white the moment they cross over.\n\n"
            "A narrow path runs between the two fields, bordered by neither black nor white grass — "
            "a grey ribbon of packed earth. At the far end stands a figure in a tattered cloak, watching you.\n\n"
            "Across both fields, a GHOSTLY SHEPHERD walks slowly, his crook trailing through the grass. "
            "He leaves no footprints."
        ),
        items=[],
        npcs=[npcs["ghostly_shepherd"]],
        exits={"northeast": "sea2", "back": "sea2"},
        blocked={
            "northeast": (
                "The sheep have blocked the path! "
                "A wall of black and white wool surges across the trail. "
                "The shepherd's riddle echoes in your mind: "
                "'Neither black nor white, yet containing both.'",
                lambda s: not s.has_flag("sheep_riddle_solved")
            ),
        },
        ambient=lambda s: (
            "A sheep crosses the boundary and bleats in surprise as its color changes. "
            "Another follows, and another. They seem to do this for entertainment."
            if not s.has_flag("sheep_riddle_solved") else
            "The sheep have parted, forming a corridor of grey down the center path. "
            "They watch you pass with knowing, ancient eyes. One winks at you."
        ),
        on_enter=lambda s: (
            "The Ghostly Shepherd approaches, his form flickering between solid and mist.\n\n"
            "'Welcome, traveler. You have come to the fields of change.'\n\n"
            "He raises his crook, and the sheep fall silent. 'I have a riddle for you. "
            "Answer it, and you may pass through the fields unchanged. Fail, and my sheep will show you "
            "what it means to be transformed against your will.'\n\n"
            "'I am neither black nor white, yet I contain both. Walk with me, and you shall pass. What am I?'"
            if not s.has_flag("sheep_riddle_solved") else None
        ),
    )

    l["sheep_pasture"] = Location(
        "sheep_pasture", "The Shepherd's Pasture",
        "A quiet pasture at the far end of the grey path, where a single fleece hangs on a wooden post.",
        detailed_desc=(
            "The grey path opens into a small, peaceful pasture. The shepherd's crook stands planted in the ground, "
            "and hanging from it is a FLEECE — shimmering, shifting between black and white as you look at it.\n\n"
            "The ghostly shepherd sits on a grey stone, watching you with twilight eyes.\n\n"
            "'You answered the riddle,' he says softly. 'The fleece is yours. It is neither black nor white — "
            "it is both. It is the space between. Wear it well, traveler, and remember: "
            "the truest path is never one thing or the other, but the grey road between extremes.'\n\n"
            "The sheep have parted to let you pass. The way back to the sea is clear."
        ),
        items=[items["fleece_of_change"]],
        npcs=[npcs["ghostly_shepherd"]],
        exits={"back": "island_sheep", "northeast": "sea2"},
        on_enter=lambda s: (
            s.set_flag("sheep_riddle_solved") or
            "The sheep part before you, forming a living corridor of black and white. "
            "You walk between them, feeling their wool brush against your legs — "
            "warm one moment, cool the next, as if you are passing through alternating currents.\n\n"
            "At the end of the path: a pasture, a shepherd, and a fleece that holds the twilight."
            if not s.has_flag("sheep_riddle_solved") else None
        ),
    )

    # ===================================================
    # ISLAND 3: ISLAND OF GIANT HORSES
    # (connects from sea2, custom direction "horses")
    # ===================================================

    l["island_horses"] = Location(
        "island_horses", "Island of Giant Horses",
        "A wide, grassy island where horses the size of war elephants gallop across the plains, their hooves shaking the earth.",
        detailed_desc=(
            "This is an island of grass and thunder.\n\n"
            "HERDS of GIANT HORSES gallop across the plains — each one the size of a small house, "
            "their manes streaming like banners, their hooves striking the earth with the force of falling trees. "
            "The ground trembles constantly.\n\n"
            "At the center of the herd stands the STALLION KING — a magnificent white horse larger than all the others, "
            "his mane flowing like sea-foam, his eyes burning with wild intelligence. He watches you with the "
            "unmistakable expression of a king who does not suffer fools.\n\n"
            "The herd mills around him, snorting and stamping. They do not attack — yet. "
            "But they make it clear: you are not welcome here unless you prove yourself."
        ),
        items=[items["horsehair_bridle"]],
        npcs=[npcs["stallion_king"]],
        exits={"southeast": "sea2", "back": "sea2"},
        blocked={
            "southeast": (
                "The herd encircles you! The Stallion King snorts a warning. "
                "You must calm the horses or fight them before you can leave.",
                lambda s: not s.has_flag("horses_pacified") and not s.has_flag("horses_fought")
            ),
        },
        ambient=lambda s: (
            "The ground shakes as the giant horses gallop past. Their breath forms clouds in the air. "
            "One of them rears up, silhouetted against the grey sky, and whinnies a challenge to the heavens."
            if not s.has_flag("horses_pacified") and not s.has_flag("horses_fought") else
            "The horses have calmed. They graze peacefully, occasionally glancing at you with something like respect. "
            "The Stallion King nods once — a gesture of acknowledgment."
        ),
        on_enter=lambda s: (
            "The giant horses rear and snort as you approach. The ground shakes with their stamping.\n\n"
            "The Stallion King fixes you with his burning eyes. He does not speak — "
            "but his challenge is clear: Prove yourself, little one. Calm me, or fight me.\n\n"
            "If you have the Silver Bell, you could ring it to calm them.\n"
            "If you have the Otter Pelt, its scent might earn their trust.\n"
            "Or you could fight the Stallion King himself."
            if not s.has_flag("horses_pacified") and not s.has_flag("horses_fought") else None
        ),
    )

    # ===================================================
    # ISLAND 4: ISLAND OF THE FLAMING CAT
    # (connects from sea3, custom direction "cat")
    # ===================================================

    l["island_flaming_cat"] = Location(
        "island_flaming_cat", "Island of the Flaming Cat",
        "A small, warm island dominated by a single pedestal of black stone. A golden crystal rests atop it, pulsing with inner light.",
        detailed_desc=(
            "This island is small — barely more than a large rock jutting from the sea. But it is unnaturally warm, "
            "as if heated from below. The air shimmers with heat haze.\n\n"
            "At the center stands a PEDESTAL of black obsidian, carved with images of cats in various stages of "
            "growth — from tiny kittens to enormous, flame-wreathed beasts.\n\n"
            "On top of the pedestal rests a SUNSTONE — a golden crystal that pulses with captured sunlight, "
            "casting warm, dancing beams across the island.\n\n"
            "A LITTLE CAT sits at the base of the pedestal — a tiny, rust-colored kitten with emerald eyes. "
            "It purrs and rubs against the stone, gazing up at the crystal with obvious adoration.\n\n"
            "When you approach, it looks up at you and mews. It seems to be saying: "
            "'This is mine. But maybe — just maybe — we can come to an arrangement.'"
        ),
        items=[items["sunstone"]],
        npcs=[npcs["little_cat"]],
        exits={"west": "sea3", "back": "sea3"},
        ambient=lambda s: (
            "The little cat purrs contentedly. The air shimmers with warmth. "
            "The sunstone pulses like a slow, golden heartbeat."
            if not s.has_flag("flaming_cat_pacified") else
            "The cat, still small, bats gently at your ankle. It seems pleased with your offering. "
            "The sunstone glows calmly, no longer a temptation — a gift freely given."
        ),
        on_enter=lambda s: (
            "The little cat stretches, yawns, and trots over to you. It circles your feet, purring loudly.\n\n"
            "But as you reach for the sunstone, its demeanor changes. Its fur stands on end. "
            "A low growl rumbles from its tiny chest — and then it BEGINS TO GROW.\n\n"
            "Its body swells, fur turning to flame, eyes blazing with ancient fire. "
            "In seconds, it is the size of a bear — a beast of living flame, blocking your path to the sunstone.\n\n"
            "Its voice crackles like a bonfire: 'You would take what is mine, little thief? "
            "Give me tribute, or feel my flame!'\n\n"
            "If you have the Bowl of Milk or the Everlasting Fruit, you could offer it as tribute."
            if not s.has_flag("flaming_cat_pacified") else None
        ),
    )

    # ===================================================
    # ISLAND 5: THE WALL OF WATER
    # (connects from sea2, direction: southeast — transitional)
    # ===================================================

    l["wall_of_water"] = Location(
        "wall_of_water", "The Wall of Water",
        "A towering wall of water rises before your ship, impossibly high, stretching from the seafloor to the clouds.",
        detailed_desc=(
            "A WALL OF WATER rises before you — a vertical ocean, stretching from the depths below to the heavens above. "
            "It is translucent, greenish, moving with a slow, powerful current that defies all nature.\n\n"
            "The wall hums — a deep, resonant sound like a mountain singing. "
            "Your curragh rocks in the turbulence at its base. Spray drenches you.\n\n"
            "Fergus stares, his face pale. 'Captain... I have never seen anything like this. "
            "It is a boundary. The sea itself has become a wall. We cannot sail through — "
            "it would crush us. But we cannot sail around it either. It stretches as far as I can see.'\n\n"
            "There must be a way to calm the waters. The Magic Thread on your mast... "
            "the Silver Bell... something that can speak to the sea's anger."
        ),
        items=[],
        npcs=[],
        exits={"northwest": "sea2", "back": "sea2", "through": "sea3"},
        blocked={
            "northwest": (
                "The wall of water thunders before you. You cannot leave until you find a way through.",
                lambda s: not s.has_flag("wall_crossed")
            ),
            "through": (
                "A towering wall of water blocks your path. You must calm the waters before you can pass through.",
                lambda s: not s.has_flag("wall_crossed")
            ),
        },
        ambient=lambda s: (
            "The wall hums. Spray flies. The sea churns at its base. It is beautiful and terrifying."
            if not s.has_flag("wall_crossed") else
            "The wall has collapsed. The sea is calm once more. Ahead, the way is clear."
        ),
        on_enter=lambda s: (
            "The Wall of Water rises before you, impossibly tall.\n\n"
            "'We must find a way through,' you say.\n\n"
            "You have the Magic Thread tied to your mast — the druid said it would guide you safely. "
            "Perhaps it can calm these waters too.\n"
            "Or the Silver Bell — its ring can calm storms. It might calm the wall as well.\n\n"
            "Type: USE THREAD ON MAST or USE BELL to try."
            if not s.has_flag("wall_crossed") else None
        ),
    )

    # ===================================================
    # ISLAND 6: ISLAND OF THE SACRED OXEN
    # (connects from sea3, custom direction "oxen")
    # ===================================================

    l["island_oxen"] = Location(
        "island_oxen", "Island of the Sacred Oxen",
        "A green, misty island where two massive white oxen with golden horns stand motionless, watching the sea.",
        detailed_desc=(
            "A green island, covered in mist that glows with a pale, golden light. The grass is thick and soft — "
            "it feels like walking on clouds.\n\n"
            "Two SACRED OXEN stand in the center of the island — magnificent white beasts with horns of pure gold. "
            "They are as still as statues, their breath forming clouds in the cool air. "
            "Their eyes are deep, dark pools — ancient, patient, knowing.\n\n"
            "They do not move as you approach. But they WATCH you.\n\n"
            "One of them lowers its massive head, presenting its golden horn as if offering it. "
            "Or perhaps it is a challenge. The meaning is unclear.\n\n"
            "The smaller ox lows softly — a sound like a distant thunder, mournful and beautiful."
        ),
        items=[],
        npcs=[npcs["sacred_oxen"]],
        exits={"north": "sea3", "back": "sea3"},
        ambient=lambda s: (
            "The oxen stand motionless. Their golden horns gleam in the mist. "
            "The larger one exhales, and its breath forms a perfect ring of cloud that drifts out to sea."
            if not s.has_flag("oxen_peaceful") and not s.has_flag("oxen_slaughtered") else
            "The remaining ox stands alone, its head bowed. "
            "The golden horn you took feels heavier than it should. "
            if s.has_flag("oxen_slaughtered") else
            "The sacred oxen graze peacefully. The larger one nods as you pass — "
            "a gesture of respect between ancient souls."
        ),
        on_enter=lambda s: (
            "The sacred oxen regard you with ancient patience.\n\n"
            "The larger one lowers its head, offering its golden horn.\n\n"
            "If you have the Speaking Feather, you could TALK to them and ask for the horn.\n"
            "You could try to FIGHT them — but killing a sacred beast would surely bring a curse.\n"
            "Or you could simply take the horn if offered willingly."
            if not s.has_flag("oxen_peaceful") and not s.has_flag("oxen_slaughtered") else None
        ),
    )

    l["oxen_glade"] = Location(
        "oxen_glade", "The Oxen's Glade",
        "A peaceful glade where the sacred oxen have made their home for centuries. The grass here glows faintly with a golden light.",
        detailed_desc=(
            "You step into the sacred glade, and the mist parts around you like a curtain.\n\n"
            "The oxen stand at the center, their golden horns casting warm light in all directions. "
            "The grass beneath your feet glows faintly, as if infused with gold dust.\n\n"
            "The larger ox lowers its head and gently places its golden horn at your feet. "
            "It steps back and lows softly — a sound of peace, of offering.\n\n"
            "'Take it,' a voice seems to say — not in words, but in understanding. "
            "'Take what you need, and go in peace. We have guarded this island long enough. "
            "Perhaps it is time for the horn to see the world beyond the mist.'\n\n"
            "The smaller ox nuzzles your hand. Its breath is warm and smells of hay and ancient sunlight."
        ),
        items=[items["golden_horn"]],
        npcs=[npcs["sacred_oxen"]],
        exits={"out": "island_oxen", "back": "island_oxen"},
        on_enter=lambda s: (
            s.set_flag("oxen_peaceful") or
            "The oxen part to let you enter the glade. The larger one bows its head, "
            "and the golden horn slides free as if it were never attached — a gift, willingly given.\n\n"
            "You take the horn. It is warm and heavy, pulsing with ancient power."
            if not s.has_flag("oxen_peaceful") else None
        ),
    )

    # ===================================================
    # ISLAND 7: THE STRAND OF THE FRESHWATER WELL
    # (connects from sea3, custom direction "well")
    # ===================================================

    l["freshwater_well"] = Location(
        "freshwater_well", "The Strand of the Freshwater Well",
        "A sandy beach on the edge of a dark sea. A single well of white stone stands at the high-tide mark, shimmering with otherworldly light.",
        detailed_desc=(
            "A strand of pale sand curves along the edge of a dark sea. The waves here are gentle — "
            "they lap at the shore like a tired animal, making soft, hushing sounds.\n\n"
            "At the high-tide mark, a WELL of white stone rises from the sand. It is ancient — "
            "the stone is worn smooth by centuries of wind and salt.\n\n"
            "Inside the well, WATER shimmers — not reflecting the grey sky above, but glowing with its own "
            "silvery light. It is the clearest water you have ever seen, and looking into it, "
            "you see not your reflection, but... something else. A path. A door. A truth you have not yet faced.\n\n"
            "A small cup of horn hangs from a peg on the well's rim, as if waiting for visitors.\n\n"
            "An inscription is carved around the well's rim:\n\n"
            "'Drink and see what is hidden. Take and carry the light. "
            "But know this: the water shows only truth, and truth is not always kind.'"
        ),
        items=[items["water_of_vision"]],
        npcs=[],
        exits={"east": "sea3", "back": "sea3"},
        ambient=lambda s: (
            "The water in the well glows softly, pulsing like a slow heartbeat. "
            "The sea whispers secrets in a language older than speech."
        ),
        on_enter=lambda s: (
            "The Freshwater Well glows before you, its water shimmering with inner light.\n\n"
            "You can DRINK from the well to gain a vision.\n"
            "You can TAKE the water — fill the cup and carry it with you.\n"
            "If you have the Truth Ring, you could use it with the water to see deeper truths."
            if not s.has_flag("well_visited") else
            s.set_flag("well_visited") or None
        ),
    )

    # ---------------------------------------------------
    # Register all new locations
    # ---------------------------------------------------
    LOCATIONS.update(l)

    # ---------------------------------------------------
    # Connect islands to sea hubs
    # ---------------------------------------------------

    # sea2 gets new exits
    try:
        sea2 = LOCATIONS["sea2"]
        sea2.exits["northeast"] = "mill_exterior"
        sea2.exits["southwest"] = "island_sheep"
        sea2.exits["horses"] = "island_horses"
        sea2.exits["southeast"] = "wall_of_water"
    except KeyError:
        pass  # sea2 may not exist in some contexts

    # sea3 gets new exits
    try:
        sea3 = LOCATIONS["sea3"]
        sea3.exits["cat"] = "island_flaming_cat"
        sea3.exits["oxen"] = "island_oxen"
        sea3.exits["well"] = "freshwater_well"
    except KeyError:
        pass  # sea3 may not exist in some contexts
