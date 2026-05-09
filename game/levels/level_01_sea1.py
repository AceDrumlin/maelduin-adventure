"""Level: 01 Sea1 — The Open Sea and its Islands"""

from ..engine import Location
from ._shared import items, npcs


def register(items, npcs):
    """Register this level's locations."""
    from ..engine import LOCATIONS
    l = {}

    # ═══════════════════════════════════════════
    # THE OPEN SEA — Hub for sea1 islands
    # ═══════════════════════════════════════════
    l["sea1"] = Location(
        "sea1", "The Open Sea",
        "Your curragh rises and falls on the grey Atlantic. The coast of Ireland is a fading line behind you.",
        detailed_desc=(
            "The wind fills your square-rigged sail. Your crew of 27 men man the oars, "
            "their faces set with determination — and a hint of seasickness.\n\n"
            "The druid's Magic Thread flutters from the mast, pulling gently to the west "
            "as if guided by an invisible hand.\n\n"
            "Ahead, the sea stretches endlessly. Diurán the poet is already writing about "
            "the experience. Conganchnes the invulnerable stands at the prow, scanning for enemies. "
            "Fergus mutters to himself, counting stars he can't yet see.\n\n"
            "Islands dot the horizon in every direction. Each one promises strangeness."
        ),
        exits={
            "west": "island_ants", "north": "island_birds",
            "northeast": "island_cat", "east": "island_laughing",
            "south": "glass_bridge", "northwest": "island_smithy",
            "southeast": "island_women", "southwest": "sea_monsters",
            "deeper": "sea2", "far": "sea2",
        },
        ambient=lambda s: (
            "The waves slap against the curragh's hide. A seabird cries overhead. "
            "Diurán is composing a limerick about a fisherman from Tralee."
            if s.turns % 3 == 0 else
            "A cold mist rolls across the water. Somewhere, a bell buoy tolls. "
            "Fergus says: 'That's not a bell buoy.' He doesn't elaborate."
            if s.turns % 3 == 1 else
            "The sun breaks through the clouds for a moment, turning the sea to silver. "
            "A whale breaches in the distance. The crew oohs and aahs."
        ),
        npcs=[npcs["young_diuran"]],
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE GIANT ANTS
    # ═══════════════════════════════════════════
    l["island_ants"] = Location(
        "island_ants", "Island of the Giant Ants",
        "An island covered in trees bearing golden fruit. The ground trembles with the marching of giant ants.",
        detailed_desc=(
            "You step onto a beach of white sand. Beyond it, a forest of strange trees rises — "
            "each one laden with golden, glowing fruit that never rots.\n\n"
            "But the trees are crawling with ANTS. Each ant is the size of a horse, "
            "with mandibles that could snap an oar in two.\n\n"
            "They seem to be... farming the trees. They tend the fruit with surprising care, "
            "almost like gardeners. One ant is gently polishing a golden fruit with its forelegs.\n\n"
            "One of them is watching you. It tilts its head. It seems more curious than hostile.\n\n"
            "A path leads INto the grove where the queen ant holds court."
        ),
        items=[items["everlasting_fruit"]],
        npcs=[],
        exits={"east": "sea1", "in": "ants_grove", "grove": "ants_grove"},
        blocked={"in": ("giant ants block the path — they seem to fear the speaking birds",
                        lambda s: s.get_item_from_inventory("speaking_feather") is None)},
        ambient=lambda s: (
            "The ants click their mandibles rhythmically, like tiny swords being sharpened. "
            "It sounds almost like a song."
            if not s.has_flag("ants_pacified") else
            "The ants now ignore you completely. One of them waves a feeler in your direction. "
            "It might be a greeting. It might be a warning. With ants, it's hard to tell."
        ),
    )

    l["ants_grove"] = Location(
        "ants_grove", "The Ant Grove",
        "The heart of the ant colony. A massive queen ant sits atop a mound of golden fruit.",
        detailed_desc=(
            "The grove opens into a clearing where the QUEEN ANT — the size of a house — "
            "sits regally upon a throne of woven branches and golden fruit.\n\n"
            "She regards you with compound eyes that reflect the world in a thousand fragments. "
            "Each fragment shows you from a different angle. You have never felt so thoroughly seen.\n\n"
            "The fruit here is piled high. A single branch hangs low, offering its golden bounty.\n\n"
            "The worker ants have stopped their labor. They watch you in complete silence. "
            "Even the wind holds its breath."
        ),
        items=[items["everlasting_fruit"]],
        npcs=[npcs["queen_ant"]],
        exits={"out": "island_ants", "east": "island_ants"},
        on_enter=lambda s: (
            "The queen ant clicks her mandibles three times. The sound echoes like a gong. "
            "A single ant approaches you, holding a golden fruit in its jaws. It offers it to you.\n\n"
            "It seems the ants are... friendly? Or they think you're a very ugly ant. "
            "Either way, free fruit."
            if not s.has_flag("ants_pacified") else None
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE SPEAKING BIRDS
    # ═══════════════════════════════════════════
    l["island_birds"] = Location(
        "island_birds", "Island of the Speaking Birds",
        "An island of sheer cliffs covered in birds of every color. They sing in human tongues.",
        detailed_desc=(
            "The cliffs rise like cathedral walls, every ledge occupied by a bird. "
            "They are not ordinary birds — they speak. Not just mimicry, but actual conversation.\n\n"
            '"Welcome, hairless ones!" cries a red-feathered creature.\n'
            '"Did you bring snacks?" asks another, hopping closer hopefully.\n'
            '"I saw a fish once that looked just like you!" adds a third.\n\n'
            "At the top of the cliff, an ENORMOUS OLD BIRD perches — ancient, half-blind, "
            "and clearly the elder of this feathered parliament. It hasn't spoken yet.\n\n"
            "A single, iridescent feather lies at the base of the cliff, humming faintly."
        ),
        items=[items["speaking_feather"]],
        npcs=[npcs["speaking_bird"]],
        exits={"south": "sea1", "up": "birds_nest", "climb": "birds_nest"},
        ambient=lambda s: (
            "The birds are arguing about the meaning of life. One of them makes an excellent point about salmon. "
            "Another is trying to organize a book club."
            if not s.has_flag("bird_talked") else
            "The birds now respectfully nod as you pass. One tips its wing in salute."
        ),
    )

    l["birds_nest"] = Location(
        "birds_nest", "The Ancient Bird's Perch",
        "The nest of the Ancient Bird, built from silver twigs and lined with gold.",
        detailed_desc=(
            "The Ancient Bird fixes you with one milky eye.\n\n"
            '"Mael Duin," it says. Its voice is like old parchment being folded. '
            '"I have been expecting you. Well, not you specifically. I\'ve been expecting someone. '
            "It's been a long time since anyone climbed up here. My legs don't work like they used to.\"\n\n"
            "It shifts on its nest, revealing a stash of shiny objects — coins, buttons, "
            "a thimble, a bronze brooch, and what looks like a dragon's tooth.\n\n"
            '"Take what you need," it says. "I\'m too old to guard treasure. '
            'I mostly just nap and complain about the weather."'
        ),
        items=[items["bronze_brooch"], items["dragon_tooth"]],
        npcs=[npcs["ancient_bird"]],
        exits={"down": "island_birds"},
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE CAT
    # ═══════════════════════════════════════════
    l["island_cat"] = Location(
        "island_cat", "Island of the Cat",
        "A small, tidy island with a single stone house. A massive black cat sits by the door.",
        detailed_desc=(
            "This island is immaculate. The grass is perfectly trimmed, the path is swept clean, "
            "and a stone house stands at the center with a neatly painted door. A welcome mat reads "
            '"WIPE YOUR PAWS."\n\n'
            "Before the door, on a golden throne, sits a CAT.\n\n"
            "It is the largest cat you have ever seen — the size of a bear. "
            "Its fur is black as ink, and its eyes are ancient green gold. "
            "It wears a small golden crown that looks surprisingly natural on its head.\n\n"
            "It licks a paw with careful dignity, then looks at you. "
            "It does not blink. Cats don't need to blink. They need you to know they don't need to blink.\n\n"
            "You get the distinct feeling you are being judged and found wanting."
        ),
        items=[items["talking_cat_tribute"]],
        npcs=[npcs["cat"]],
        exits={"southwest": "sea1"},
        ambient=lambda s: (
            "The cat's tail flicks once, twice. It is unimpressed with your existence. "
            "You hear it mutter something that sounds like 'amateurs.'"
            if not s.has_flag("cat_pacified") else
            "The cat purrs contentedly as you pass. You have been deemed acceptable. "
            "It's the greatest honor of your life."
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE LAUGHING PEOPLE
    # ═══════════════════════════════════════════
    l["island_laughing"] = Location(
        "island_laughing", "Island of the Laughing People",
        "An island where EVERYONE is laughing. Babies laugh. Dogs laugh. Even the trees seem to chuckle.",
        detailed_desc=(
            "As you step ashore, a wave of laughter hits you. Everyone — and everything — on this island is laughing.\n\n"
            "A farmer laughs as he plows. His horse laughs. The chickens laugh so hard they fall off their perches. "
            "A woman offers you a cup of water, laughing so hard she spills half of it.\n\n"
            "In the center of the village, a KING sits on a one-legged stool, laughing uproariously "
            "at absolutely nothing visible. He laughs until he cries, then laughs at his own tears.\n\n"
            "Your crew is starting to giggle. Conganchnes looks deeply uncomfortable. "
            "He has not laughed since 1142 and he is not about to start now."
        ),
        items=[],
        npcs=[npcs["laughing_king"]],
        exits={"west": "sea1"},
        ambient=lambda s: (
            "HA HA HA HA HA! The laughter never stops. It's infectious. "
            "You find yourself grinning despite yourself. "
            "Diurán is writing down the joke, but he's laughing too hard to hold the quill."
            if not s.has_flag("king_pacified") else
            "The island seems quieter now. People still chuckle, but it's a gentle mirth. "
            "The king is humming contentedly and trying to fix his stool."
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE GLASS BRIDGE
    # ═══════════════════════════════════════════
    l["glass_bridge"] = Location(
        "glass_bridge", "Island of the Glass Bridge",
        "A glittering island with a bridge made entirely of crystal, leading to a palace beyond.",
        detailed_desc=(
            "A palace of white marble gleams in the distance. But to reach it, you must cross "
            "a BRIDGE made entirely of transparent glass, suspended over a chasm of swirling mist.\n\n"
            "The glass is perfectly clear. You can see straight through it to the jagged rocks below. "
            "The bridge is about a hundred feet long and looks like it was made by someone who "
            "had never heard the phrase 'safety first.'\n\n"
            "A beautiful woman stands on the far side of the bridge, beckoning.\n\n"
            '"Cross, brave sailor. I will not let you fall."\n\n'
            "You notice two things that might help: a SHARD OF GLASS lies at the base of the bridge, "
            "broken off from the edge. And in your heart, you feel the HERMIT'S BLESSING could "
            "carry you across on faith alone.\n\n"
            "Without either, the bridge is certain death."
        ),
        items=[items["glass_shard"]],
        npcs=[],
        exits={"north": "sea1", "cross": "glass_palace", "bridge": "glass_palace"},
        blocked={"cross": ("the bridge is made of transparent glass over a bottomless chasm — you need the Glass Shard to test its strength or the Hermit's Blessing to cross on faith",
                          lambda s: s.get_item_from_inventory("glass_shard") is None
                          and s.get_item_from_inventory("hermit_blessing") is None)},
        on_enter=lambda s: (
            "The glass groans under your weight as you step onto the bridge...\n\n"
            + (("You hold up the Glass Shard. It glows and the bridge solidifies beneath you, "
                "turning from transparent to a milky white that you can walk on.\n\n"
                "You cross safely, the shard showing you the way.")
               if s.has_flag("bridge_tested") or s.get_item_from_inventory("glass_shard") else
               ("You clutch the Hermit's Blessing. A warm light surrounds you, "
                "and the bridge seems to become solid as faith itself.\n\n"
                "You walk across, guided not by sight but by trust. The chasm below does not claim you."))
            + "\n\nYour crew follows, awestruck."
            if not s.has_flag("crossed_bridge") else None
        ),
        ambient=lambda s: (
            "The glass bridge shimmers in the light. It's beautiful and absolutely terrifying. "
            "The wind whistles through the chasm below."
        ),
    )

    def _glass_palace_enter(state):
        if state.has_flag("left_palace"):
            return "The palace is empty now, but you feel lighter for having resisted."
        if not state.has_flag("entered_palace"):
            state.set_flag("entered_palace")
            state.awaiting_choice = "palace_stay"
            return (
                "The woman beckons. 'Stay with me. Forget the sea, the quest, the revenge.'\n\n"
                "Her voice is honey and razor wire. You feel your resolve weakening...\n\n"
                "Type YES to stay. Type NO to leave."
            )
        return None

    l["glass_palace"] = Location(
        "glass_palace", "The Glass Palace",
        "A palace of crystal and light. Music plays from nowhere, and the air smells of honey.",
        detailed_desc=(
            "You step into a palace that seems built from frozen light. "
            "Every surface reflects a thousand colors in a thousand different ways. "
            "Music \u2014 harps and flutes \u2014 plays without any musician.\n\n"
            "A beautiful woman offers you a seat on cushions of silk. "
            '"Stay," she whispers. "Rest. You have traveled so far."\n\n'
            "This place feels like a dream. It also feels like a trap. "
            "The floor is suspiciously transparent in places \u2014 you can see the chasm below. "
            "The palace isn't built on the ground; it's suspended over the void.\n\n"
            "The woman's smile never reaches her eyes.\n\n"
            "A voice in your head whispers: 'Stay and you will forget your quest. Leave and you will remember.'\n\n"
            "Type YES to stay (lose time, risk losing a crew member).\n"
            "Type NO to leave the palace behind."
        ),
        items=[],
        npcs=[],
        exits={"back": "glass_bridge", "east": "glass_bridge"},
        on_enter=_glass_palace_enter,
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE SMITHY
    # ═══════════════════════════════════════════
    l["island_smithy"] = Location(
        "island_smithy", "Island of the Smithy",
        "An island of volcanic rock, dominated by a massive forge that belches fire and smoke.",
        detailed_desc=(
            "The air shimmers with heat. A mountain of slag and cinder rises from the center of the island, "
            "topped by a FORGE the size of a hill.\n\n"
            "CLANG. CLANG. CLANG.\n\n"
            "Each hammer strike shakes the ground beneath your feet. "
            "The vibrations travel up through your legs and rattle your teeth.\n\n"
            "A GIANT works the bellows — each breath of the bellows sends a gale across the island. "
            "You realize the bellows are what create storms at sea. The giant sneezes, and a bolt of lightning "
            "cracks across the sky, followed by a thunderclap that rocks the boat.\n\n"
            "\"...Bless you,\" says a crew member quietly.\n\n"
            "The giant hasn't noticed you yet. He's too busy hammering a block of metal "
            "that's glowing like a small sun."
        ),
        npcs=[npcs["smith"]],
        exits={"southeast": "sea1"},
        items=[items["fiery_ash"]],
        ambient=lambda s: (
            "The forge roars. Embers drift like fireflies. The giant hums a tune "
            "that sounds suspiciously like 'Row, Row, Row Your Boat' but in a minor key. "
            "A sign above the forge reads: 'Payment accepted: shiny things only.'"
            if not s.has_flag("got_harpoon") else
            "The forge is quiet now. The giant waves cheerily as you pass. "
            "'Come back if you need anything else! I do good work!'"
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF WOMEN
    # ═══════════════════════════════════════════
    l["island_women"] = Location(
        "island_women", "Island of Women",
        "An island of perpetual sunset, where beautiful women feast, dance, and sing endlessly.",
        detailed_desc=(
            "You step onto an island that seems untouched by time. The sun is always just setting, "
            "painting everything in gold and rose. The air is warm and smells of honey and jasmine.\n\n"
            "Beautiful women in silken gowns approach, offering trays of roasted meats, fresh bread, "
            "and honeyed wine. Music — a harp and a flute — floats on the warm air.\n\n"
            "Your crew is already drooling. Diurán is composing poetry. "
            "Conganchnes is blushing. Fergus has forgotten how to navigate.\n\n"
            "At the center of the feast, a QUEEN sits on a throne of flowers. "
            "She smiles at you — a smile that promises everything and costs nothing."
        ),
        npcs=[npcs["queen"]],
        items=[items["truth_ring"]],
        exits={"northwest": "sea1"},
        ambient=lambda s: (
            "The music swells. A woman laughs somewhere. The food smells incredible. "
            "Time feels different here — slower, thicker, like honey."
            if not s.has_flag("left_women") else
            "The island is silent now. The palace stands empty, as if everyone left in a hurry. "
            "A single wilted flower lies on the throne."
        ),
    )

    # ═══════════════════════════════════════════
    # THE SEA OF MONSTERS
    # ═══════════════════════════════════════════
    l["sea_monsters"] = Location(
        "sea_monsters", "The Sea of Monsters",
        "Still, glassy water that feels wrong. Something moves beneath the surface.",
        detailed_desc=(
            "The sea is unnaturally calm — flat as glass. Not a breath of wind stirs. "
            "The water is dark green, almost black, and impossibly deep.\n\n"
            "Your crew rows nervously. Too quietly. Too watchfully. "
            "Oars dip into the water without a splash, as if the sea itself is holding its breath.\n\n"
            "Something HUGE passes beneath the boat. A shadow the size of your curragh glides in the depths. "
            "It circles once. Twice.\n\n"
            "Then — a giant hand erupts from the water, grabbing the side of your boat! "
            "Webbed fingers the size of hammers grip the gunwale. The boat lurches violently."
        ),
        npcs=[],
        items=[],
        exits={"east": "island_women", "northeast": "sea1", "north": "island_laughing"},
        on_enter=lambda s: (
            "A monstrous hand erupts from the water, clutching the gunwale of your curragh! "
            "The boat lurches violently. Crew members grab for their swords.\n\n"
            "You have a moment to act! FIGHT it with your sword, or use an item!"
            if not s.has_flag("sea_monster_defeated") else None
        ),
        ambient=lambda s: (
            "The water beneath you is impossibly deep and dark. Something is watching from below. "
            "Fergus is praying to every god he knows. Diurán is writing his will."
            if not s.has_flag("sea_monster_defeated") else
            "The sea is calm and safe now. Fergus has stopped praying. Diurán has torn up his will."
        ),
    )

    # Add crew dialogue that references prologue events
    # These dialogues get triggered when talking to crew members at sea
    
    # We add sea-specific dialogue by updating existing NPC dialogue
    # The NPC objects are shared, so we modify them after creation
    
    _add_sea_dialogue(npcs)

    LOCATIONS.update(l)


def _add_sea_dialogue(npcs):
    """Add sea-specific dialogue to crew NPCs that references prologue events."""
    if "young_diuran" in npcs:
        diuran = npcs["young_diuran"]
        diuran.dialogue["sea"] = (
            'Diur\u00e1n looks up from his parchment, quill still moving.\n\n'
            '"Captain! I\'m writing a poem about that last island. '
            'It\'s not going well. I keep rhyming \'sea\' with \'misery\' which is '
            'technically accurate but poetically lazy.\n\n'
            'Remember back in the training field, when I used to write epic poems '
            'about battles we hadn\'t fought yet? Well, now we\'ve fought them, '
            'and let me tell you: reality is much harder to rhyme than imagination."\n\n'
            'He sighs dramatically and dips his quill again.'
        )
        diuran.dialogue["islands"] = (
            'Diur\u00e1n flips through his increasingly thick sheaf of parchment.\n\n'
            '"I\'ve been keeping a log of every island. The giant ants? Excellent material. '
            'That cat? I wrote a haiku about it. '
            'The Laughing King? I filled three pages and couldn\'t stop laughing long enough '
            'to make them coherent.\n\n'
            'This voyage will be the greatest epic ever told. '
            'Assuming we survive to tell it."'
        )

    if "young_fergus" in npcs:
        fergus = npcs["young_fergus"]
        fergus.dialogue["sea"] = (
            'Fergus squints at the horizon, then at the sky, then back at the horizon.\n\n'
            '"The stars are different here, Captain. I don\'t recognise half of them. '
            'Back home, I could name every star in the sky. Here? '
            'I saw one that looked like a fish riding a horse. I don\'t know what that means.\n\n'
            'But the Magic Thread is pulling true. Whatever the druid wove into that thread, '
            'it knows where we\'re going better than any star chart."'
        )
        fergus.dialogue["navigation"] = (
            'Fergus taps his nose. "I navigate by instinct now. '
            'The old ways don\'t work in these waters. '
            'The stars moved. The currents changed. The wind has a different smell.\n\n'
            'But there\'s a rhythm to it. The sea has a heartbeat, '
            'and if you listen long enough, you can feel where it wants you to go."'
        )

    if "young_conganchnes" in npcs:
        conganchnes = npcs["young_conganchnes"]
        conganchnes.dialogue["sea"] = (
            'Conganchnes grins and flexes an arm the size of a mast timber.\n\n'
            '"Still can\'t be cut, Captain. I tested it on that glass bridge shard. '
            'The shard lost. I\'m starting to think I really am invulnerable.\n\n'
            'Remember when we trained together back in the village? '
            'You could barely lift a practice sword. Now look at you. '
            'Leading twenty-seven men across the edge of the world. '
            'Your father would be proud."\n\n'
            'He claps you on the shoulder hard enough to stagger you.'
        )
        conganchnes.dialogue["fight"] = (
            'Conganchnes draws his sword and inspects the edge.\n\n'
            '"I\'m ready whenever you need me, Captain. '
            'Monster, man, or god \u2014 I\'ll fight it. '
            'That\'s what I\'m here for. That\'s what I\'ve always been here for.\n\n'
            'The training field is a long way behind us now. '
            'This is the real thing. And I wouldn\'t miss it for anything."'
        )
