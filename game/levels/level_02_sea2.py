"""Level: 02 Sea2 — The Deeper Waters"""

from ..engine import Location
from ._shared import items, npcs


def register(items, npcs):
    """Register this level's locations."""
    from ..engine import LOCATIONS
    l = {}

    # ═══════════════════════════════════════════
    # THE DEEPER SEA
    # ═══════════════════════════════════════════
    l["sea2"] = Location(
        "sea2", "The Deeper Sea",
        "The water has changed color — a deep, midnight blue. Strange lights flicker beneath the surface.",
        detailed_desc=(
            "You have sailed beyond the familiar waters into the deeper sea. "
            "The coastline of Ireland is long gone. The sky is a different shade of grey here — "
            "somehow older, more ancient, as if this sky was hung before humans learned to name things.\n\n"
            "The druid's Magic Thread pulls steadily westward. The wind has a different voice — "
            "it whispers names you don't recognize in a language that sounds almost like Irish but isn't.\n\n"
            "Fergus squints at the horizon. 'We're in uncharted waters now, Captain. "
            "The stars are different here. They have... stranger names. "
            "Also, I think that cloud just waved at me.'\n\n"
            "Bioluminescent creatures drift past the boat, trailing sparks of cold fire. "
            "The water glows where your oars dip in, leaving trails of light."
        ),
        exits={
            "north": "island_culdees", "south": "prophecy_tower",
            "east": "hermit_rock", "west": "island_four_fences",
            "northwest": "island_salmon", "deeper": "sea3",
            "far": "sea3", "back": "sea1",
        },
        ambient=lambda s: (
            "Bioluminescent creatures drift past the boat, trailing sparks of cold fire. "
            "The water glows where your oars dip in."
            if s.turns % 3 == 0 else
            "A deep, resonant sound echoes from below — like a whale singing, but older. "
            "Much older. Your bones vibrate with it."
            if s.turns % 3 == 1 else
            "A strange fog rolls in. In the mist, you see shapes that might be islands "
            "or might be something else. They don't hold still long enough to tell."
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE CULDEES (Monastery)
    # ═══════════════════════════════════════════
    l["island_culdees"] = Location(
        "island_culdees", "Island of the Culdees",
        "A peaceful island with a small monastery. A bell rings itself, calling the monks to prayer.",
        detailed_desc=(
            "A monastery of grey stone stands on this quiet island. The Culdees — anchorites devoted to God — "
            "tend a garden of herbs and vegetables with patient, weathered hands.\n\n"
            "A SILVER BELL hangs in a small tower. It rings of its own accord, at the exact hour of prayer. "
            "No one rings it. It simply decides it's time, and rings.\n\n"
            "The monks pay you no mind. They are busy praying, gardening, and ignoring the mortal world "
            "with a dedication that is almost impressive.\n\n"
            "One monk looks up from his weeding and nods once. 'The bell knows when it's needed,' he says. "
            "'Do you?' He goes back to weeding before you can answer.\n\n"
            "The silver bell is within reach. It would certainly fetch a price. "
            "But stealing from monks feels... wrong."
        ),
        items=[items["silver_bell"]],
        npcs=[],
        exits={"south": "sea2"},
        ambient=lambda s: (
            "The self-ringing bell tolls softly. A monk chants in Latin. "
            "It is... peaceful. You feel your blood pressure dropping."
            if not s.has_flag("took_bell") else
            "Without the bell, the island feels incomplete. The monks seem quieter now, "
            "glancing up at the empty tower. One of them sighs deeply."
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF PROPHECY (Crystal Tower)
    # ═══════════════════════════════════════════
    l["prophecy_tower"] = Location(
        "prophecy_tower", "Island of Prophecy",
        "An island with a single tower of crystal, rising from the sea like a prism.",
        detailed_desc=(
            "A tower of pure crystal rises from the sea, catching the light and scattering it into rainbows. "
            "The sight is so beautiful it makes Diurán weep. 'I'll never be able to describe this adequately,' "
            "he sobs, writing furiously.\n\n"
            "A door of silver stands open. Inside, stairs spiral upward. "
            "The steps are made of glass, and beneath them, you can see the sea. "
            "It's a long way down.\n\n"
            "At the top of the tower, a YOUNG BOY sits cross-legged on nothing — he's floating "
            "a few inches above the floor. He's reading a book that has no pages, "
            "yet he turns each invisible leaf with great concentration.\n\n"
            "He looks up and grins. 'Took you long enough! I've been waiting since page three.'"
        ),
        npcs=[npcs["prophet_boy"]],
        items=[items["prophecy_scroll"]],
        exits={"north": "sea2", "up": "prophecy_tower", "enter": "prophecy_tower"},
    )

    # ═══════════════════════════════════════════
    # THE HERMIT'S ROCK
    # ═══════════════════════════════════════════
    l["hermit_rock"] = Location(
        "hermit_rock", "The Hermit's Rock",
        "A bare rock in the middle of the ocean. A holy man stands upon it, one with the elements.",
        detailed_desc=(
            "You approach a solitary ROCK jutting from the sea. It is no larger than your curragh. "
            "The waves crash against it with furious regularity, yet the man standing on top "
            "does not so much as sway.\n\n"
            "Upon it stands a HERMIT, soaked by spray, lashed by wind, his eyes closed in prayer. "
            "His beard moves in the breeze like a living thing. His robes are patched in a dozen colors.\n\n"
            "At his feet, an OTTER sits, holding a fish in its mouth. The otter looks at you "
            "with an expression that clearly says 'This is my fish. Get your own.'\n\n"
            "The hermit opens his eyes and looks directly at you. "
            "His gaze is unsettling — it feels like he's looking through you, not at you.\n\n"
            '"I was wondering when you\'d get here," he says. "The otter caught a large one today — '
            "there's enough for everyone. Sit. Eat. Tell me why you're really here.\""
        ),
        npcs=[npcs["hermit"]],
        items=[items["otter_pelt"]],
        exits={"west": "sea2"},
        on_enter=lambda s: (
            "The hermit's blessing washes over you as you step onto the rock. "
            "For a moment, the weight of your quest lifts from your shoulders. "
            "The sea seems quieter. The wind gentler."
            if not s.has_flag("met_hermit") else None
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE FOUR FENCES
    # ═══════════════════════════════════════════
    l["island_four_fences"] = Location(
        "island_four_fences", "Island of the Four Fences",
        "An island divided by four fences — gold, silver, copper, and crystal. You must choose the right one.",
        detailed_desc=(
            "A flat, grey island stretches before you. It is divided into four sections by four different fences.\n\n"
            "The first fence is made of GOLD — gleaming, magnificent, clearly the most valuable. A gate stands open. "
            "A path beyond it leads invitingly toward a treasure chest.\n\n"
            "The second fence is made of SILVER — elegant, understated, with a latch that lifts easily. "
            "Beyond it, the path is slightly overgrown but still clear.\n\n"
            "The third fence is made of COPPER — humble, practical, with a simple rope holding the gate shut. "
            "Beyond it, the path is barely visible, winding through wild grass.\n\n"
            "The fourth fence is made of CRYSTAL — delicate, beautiful, but it looks like it would shatter at a touch. "
            "Beyond it, a magnificent palace gleams on the horizon.\n\n"
            "A faded sign reads: 'Beyond one fence lies a great treasure. Beyond the others, only regret. Choose wisely.'\n\n"
            "The answer seems obvious. But maybe that's the trap."
        ),
        items=[],
        npcs=[],
        exits={"east": "sea2",
               "gold": "four_fences_gold",
               "silver": "four_fences_silver",
               "copper": "four_fences_copper",
               "crystal": "four_fences_crystal"},
        ambient=lambda s: (
            "The fences hum with different energies. The gold one radiates greed — it makes your teeth ache. "
            "The copper one whispers humility — it smells like bread baking."
            if not s.has_flag("four_fences_solved") else
            "The copper fence has crumbled to dust. A treasure chest lies open at your feet. "
            "Inside: a bronze key that turns of its own accord."
        ),
        on_enter=lambda s: (
            "A faded sign offers a clue: 'The humble path is the true path. The proud path is the fool's path.'\n\n"
            "Four gates stand before you. Which do you open?\n"
            "Type GOLD, SILVER, COPPER, or CRYSTAL to choose."
            if not s.has_flag("four_fences_solved") else None
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE WISDOM SALMON
    # ═══════════════════════════════════════════
    l["island_salmon"] = Location(
        "island_salmon", "Island of the Wisdom Salmon",
        "An island with a single stream running through it, filled with silver salmon that leap against the current.",
        detailed_desc=(
            "A small, green island with a crystal-clear stream running from a spring in the center to the sea.\n\n"
            "The stream is FULL of salmon — fat, silver, magnificent fish that leap against the current "
            "with incredible determination. They move like thoughts — quick, purposeful, elusive.\n\n"
            "But these are no ordinary salmon. When you look into their eyes, you see... understanding. "
            "They look back at you with the patient wisdom of creatures who have seen civilizations rise and fall.\n\n"
            "A small sign on the bank reads: 'He who eats of the Salmon of Wisdom gains the knowledge of all things. "
            "But catching one requires cunning, for they are wiser than any fish has a right to be.'\n\n"
            "The salmon look at you smugly. They know you don't have a fishing rod. "
            "One of them flicks its tail and says — actually says, in a clear voice — "
            "'Nice try, land-walker.'"
        ),
        items=[],
        npcs=[],
        exits={"southeast": "sea2"},
        ambient=lambda s: (
            "A salmon leaps clear of the water, hangs in the air for a moment, "
            "and grins at you — a fish grinning — before splashing back down."
            if not s.has_flag("caught_salmon") else
            "The remaining salmon eye you warily. They've heard about what happened to their cousin. "
            "One of them mutters 'cannibal' under its breath."
        ),
    )


    # Sub-locations for Four Fences choices
    l["four_fences_gold"] = Location(
        "four_fences_gold", "The Golden Gate — Greed's Reward",
        "You chose the gold gate. It was a trap.",
        detailed_desc=(
            "The moment you step through the golden gate, it SLAMS shut behind you. "
            "The golden bars grow thorns. The path ahead dissolves into mist.\n\n"
            "From the mist, a voice: 'You chose what glitters. Now you must pay.'\n\n"
            "A golden spike shoots from the ground. You barely dodge it. "
            "Your crew scrambles to escape. In the chaos, one of your items falls into a crevice "
            "and is lost forever.\n\n"
            "You barely make it back to the gate, which has reopened. "
            "Your crew is shaken. One item is gone. The lesson: greed has a price."
        ),
        items=[], npcs=[], exits={"back": "island_four_fences", "east": "island_four_fences"},
        on_enter=lambda s: (
            setattr(s, "awaiting_choice", "fences_gold_penalty") or
            "The gold fence was a trap! You stumble back, lucky to be alive."
            if not s.has_flag("gold_fence_tried") else None
        ),
    )

    l["four_fences_silver"] = Location(
        "four_fences_silver", "The Silver Gate — Elegance Unrewarded",
        "You chose the silver gate. A dead end.",
        detailed_desc=(
            "The silver gate opens onto a path that winds through beautiful gardens. "
            "Flowers bloom in impossible colors. Fountains sing. It is lovely.\n\n"
            "It is also a circle. The path leads nowhere — it brings you back to the starting point.\n\n"
            "You have wasted time. The silver gate was beautiful but empty. "
            "The real treasure lies elsewhere."
        ),
        items=[], npcs=[], exits={"back": "island_four_fences", "east": "island_four_fences"},
    )

    l["four_fences_copper"] = Location(
        "four_fences_copper", "The Copper Gate — Humility Rewarded",
        "You chose the copper gate. The humble path. You chose wisely.",
        detailed_desc=(
            "The copper gate swings open with a sound like a contented sigh. "
            "The path beyond is simple — packed earth, wildflowers, the smell of rain.\n\n"
            "At the end of the path sits a small stone pedestal. On it rests a BRONZE KEY "
            "that turns in place of its own accord, as if it cannot stop moving.\n\n"
            "A voice on the wind: 'You chose humility over pride. The key to the turning world is yours.'\n\n"
            "The key is meant for the Revolving Castle. With it, you can choose the right door."
        ),
        items=[items["revolving_key"]], npcs=[], exits={"back": "island_four_fences", "east": "island_four_fences"},
        on_enter=lambda s: (
            (s.set_flag("four_fences_solved") or True) and
            "The copper fence crumbles to dust. The path is clear. "
            "The key hums in your hand, eager to be used."
            if not s.has_flag("four_fences_solved") else None
        ),
    )

    l["four_fences_crystal"] = Location(
        "four_fences_crystal", "The Crystal Gate — Fragile Beauty",
        "You chose the crystal gate. It shattered.",
        detailed_desc=(
            "The crystal gate is beautiful — delicate, rainbow-shot, perfect.\n\n"
            "It is also as fragile as it looks. The moment you touch it, the entire gate "
            "shatters into a million pieces. Shards fly everywhere.\n\n"
            "One of your crew members is cut badly. They will need time to recover. "
            "You cannot take them further into danger.\n\n"
            "You lose a crew member. The crystal gate had no answer — only pain."
        ),
        items=[], npcs=[], exits={"back": "island_four_fences", "east": "island_four_fences"},
        on_enter=lambda s: (
            (s.lose_crew("diuran") or True) and
            "Diurán is wounded by flying crystal! He cannot continue."
            if not s.has_flag("crystal_tried") else None
        ),
    )



    LOCATIONS.update(l)
