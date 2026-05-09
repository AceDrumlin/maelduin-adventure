"""Level: 06 Missing Islands (Part 2) — 4 new islands from the original immram."""

from ..engine import LOCATIONS, Location


def register(items, npcs):
    """Register this level's locations and add exits to sea hubs."""
    l = {}
    from .. import engine as _eng

    # ===================================================
    # Helper: register new direction aliases so players
    # can type single-word navigation commands
    # ===================================================
    _eng.VERBS["fish"] = ("go", lambda s, a: _eng.handle_go(s, "fish"))
    _eng.VERBS["fountain"] = ("go", lambda s, a: _eng.handle_go(s, "fountain"))
    _eng.VERBS["silence"] = ("go", lambda s, a: _eng.handle_go(s, "silence"))
    _eng.VERBS["promised"] = ("go", lambda s, a: _eng.handle_go(s, "promised"))

    # ===================================================
    # ISLAND 1: THE GREAT FISH
    # (connects from sea3, direction: fish)
    # ===================================================

    l["great_fish_belly"] = Location(
        "great_fish_belly", "The Great Fish — Belly of the Beast",
        "You are inside the belly of a fish the size of a cathedral. The walls pulse wetly. It is dark, hot, and the air smells of brine and bile.",
        detailed_desc=(
            "Darkness. Warmth. A wet, rhythmic pulse all around you.\\\n\\\n"
            "You are INSIDE something. Something alive.\\\n\\\n"
            "The walls are slick and pink, flexing with each slow contraction. "
            "The floor — if it can be called a floor — is spongy and uneven, "
            "slick with half-digested seawater. The air is thick and warm, "
            "and you taste salt and iron on your tongue.\\\n\\\n"
            "Your curragh is intact — the fish swallowed your boat whole, "
            "and now you drift in this fleshy chamber, surrounded by the "
            "slow, terrible digestion of the deep.\\\n\\\n"
            "There are no exits. No doors. No light.\\\n\\\n"
            "But the walls... they are thin in places. Thin enough to cut through. "
            "Thin enough to BURN through. If you have something sharp, "
            "or something that burns, you might be able to cut your way out."
        ),
        items=[],
        npcs=[],
        exits={},
        blocked={},
        ambient=lambda s: (
            "GLOOP... The walls pulse. The air is thick. You feel the pressure "
            "of the deep around you — tons of water and fish-flesh pressing in."
            if not s.has_flag("escaped_fish") else
            "A gaping wound in the fish's side lets in pale blue light. "
            "The sea waits outside."
        ),
        on_enter=lambda s: (
            "The world turns upside down.\\\n\\\n"
            "One moment you are sailing the dark sea, the next — a shadow from below, "
            "impossibly vast, rising like an island of teeth and hunger.\\\n\\\n"
            "Your crew shouts. The curragh shudders. And then the world goes dark "
            "and wet as the GREAT FISH swallows you whole.\\\n\\\n"
            "You are in its belly. It is warm. It is dark. It STINKS.\\\n\\\n"
            "Fergus's voice echoes in the darkness: 'Captain... we're inside something. "
            "Something BIG. We need to get out BEFORE WE GET DIGESTED.'\\\n\\\n"
            "You feel the walls. They are thick but yielding. With something SHARP "
            "or something that BURNS, you could cut your way free.\\\n\\\n"
            "But you don't have much time. The crew is gasping. The air is running out."
            if not s.has_flag("escaped_fish") else None
        ),
    )

    # Post-escape location (the fish's carcass outside)
    l["great_fish_carcass"] = Location(
        "great_fish_carcass", "The Great Fish — Carcass",
        "The fish floats lifeless on the surface, a gaping wound in its side. Your boat drifts nearby.",
        detailed_desc=(
            "The Great Fish floats belly-up on the dark water. It is enormous — "
            "the size of a small island. Its scales are the color of storm clouds, "
            "and its dead eye stares at nothing.\\\n\\\n"
            "You clamber out through the wound you made, gasping for clean air. "
            "Your crew follows, coughing and cheering.\\\n\\\n"
            "Fergus kneels on the fish's belly. 'I'm never eating fish again. "
            "Never. Not even on Fridays.'\\\n\\\n"
            "Between the fish's gaping jaws, you spot something gleaming — "
            "a single massive tooth, broken off during the swallowing. "
            "It is serrated, curved, and as long as your forearm. "
            "It could be a weapon. A reminder. Both.\\\n\\\n"
            "Take the FISH TOOTH before you go."
        ),
        items=[items["fish_tooth"]],
        npcs=[],
        exits={"out": "sea3", "back": "sea3"},
        on_enter=lambda s: (
            s.set_flag("escaped_fish") or
            "You stagger out of the fish's belly and collapse onto its slick, scaly back. "
            "The open sky has never looked so beautiful.\\\n\\\n"
            "Your crew emerges one by one, gasping, laughing, weeping. "
            "Diurán is already composing a verse: 'The belly of the beast we rode, "
            "and lived to tell the tale — though barely, and our clothes still smell.\\\n\\\n"
            "The Great Fish is dead. Your boat is safe. And between its jaws, "
            "a single massive FISH TOOTH gleams in the grey light.\\\n\\\n"
            "(+3 points. Take the Fish Tooth before you return to sea.)" or None
        ),
    )

    # ===================================================
    # ISLAND 2: ISLAND OF THE FOUNTAIN
    # (connects from sea3, direction: fountain)
    # ===================================================

    l["island_fountain"] = Location(
        "island_fountain", "Island of the Fountain",
        "A small, green island with a single white stone fountain at its center. The water glows with a pale, milky luminescence.",
        detailed_desc=(
            "This island is a perfect circle of green grass, no larger than a village green. "
            "At its center stands a FOUNTAIN of white stone, ancient and weather-worn, "
            "carved with spirals and knotwork that seem to shift when you look at them sideways.\\\n\\\n"
            "Water flows from the fountain — not clear, but MILK-WHITE, "
            "shimmering with an inner light. It pools in a basin below "
            "and overflows into a channel that feeds the grass.\\\n\\\n"
            "An inscription circles the basin, worn but legible:\\\n\\\n"
            "    'Drink and you shall dream.\\\n"
            "     Take and you shall carry.\\\n"
            "     Give and you shall heal.'\\\n\\\n"
            "The water smells faintly of honey and fresh cream. "
            "It looks drinkable. It looks like it might do something."
        ),
        items=[items["fountain_water"]],
        npcs=[],
        exits={"back": "sea3", "east": "sea3"},
        ambient=lambda s: (
            "The fountain burbles softly. The water glows with a gentle, milky luminescence. "
            "It seems to be waiting."
        ),
        on_enter=lambda s: (
            "The fountain glows softly before you, its milk-white water shimmering with inner light.\\\n\\\n"
            "You can DRINK from the fountain — but the inscription warns: 'Drink and you shall dream.'\\\n"
            "You can TAKE the water — fill a container with the glowing liquid.\\\n"
            "If you have an empty container, you could fill it with the healing water.\\\n\\\n"
            "What do you do?"
            if not s.has_flag("fountain_visited") else
            s.set_flag("fountain_visited") or None
        ),
    )

    # ===================================================
    # ISLAND 3: ISLAND OF SILENCED MUSIC
    # (connects from sea3, direction: silence)
    # ===================================================

    l["island_silence"] = Location(
        "island_silence", "Island of Silenced Music",
        "A beautiful valley where everything is muted. The birds open their beaks but no sound comes out. The wind blows but does not rustle the leaves.",
        detailed_desc=(
            "This valley should be full of sound — birds singing, wind rustling through the leaves, "
            "a stream chattering over stones. But there is NOTHING.\\\n\\\n"
            "The silence is so complete you can hear your own blood moving through your veins. "
            "You can hear your eyelids blinking. The absence of noise is a physical weight.\\\n\\\n"
            "The valley is beautiful — green grass, flowering trees, a crystal stream — "
            "but it is a beauty that has been frozen, mummified, preserved in silence.\\\n\\\n"
            "At the far end of the valley, on a throne of grey stone, sits a figure "
            "draped in flowing grey robes. It does not move. It does not breathe. "
            "But you know it is waiting.\\\n\\\n"
            "An iron bell hangs from a branch of a dead tree nearby. "
            "When you look at it, you feel an overwhelming urge to ring it — "
            "but also a deep, primal fear of what might happen if you do.\\\n\\\n"
            "The silence here is not natural. It is enforced. By something. "
            "Or someone."
        ),
        items=[],
        npcs=[],
        exits={"back": "sea3", "west": "sea3", "grove": "silence_grove", "deeper": "silence_grove", "in": "silence_grove"},
        ambient=lambda s: (
            "The silence presses in. You can hear your own heartbeat. Your own breath. "
            "The sound of your own thoughts is unbearably loud."
        ),
        on_enter=lambda s: (
            "The silence is suffocating.\\\n\\\n"
            "Your crew shuffles nervously — even Conganchnes looks uneasy. "
            "The poet Diurán is trying to hum but no sound comes out. "
            "He looks terrified.\\\n\\\n"
            "You feel the weight of the silence on your shoulders. It is not peaceful. "
            "It is a command. An edict.\\\n\\\n"
            "The grey figure on the throne waits. It has not moved. "
            "But its head is turned toward you.\\\n\\\n"
            "You could SING or JOKE — break the silence and see what happens.\\\n"
            "Or you could explore the valley quietly — the SILENT BELL hangs from a tree.\\\n\\\n"
            "Choose wisely. The silence is a living thing here."
            if not s.has_flag("silence_visited") else
            s.set_flag("silence_visited") or None
        ),
    )

    # The silent grove beyond — where the bell is found
    l["silence_grove"] = Location(
        "silence_grove", "The Silent Grove",
        "A small grove of silver-leaved trees surrounding a white clearing. The Silent Bell hangs on a branch, utterly still.",
        detailed_desc=(
            "Beyond the valley, hidden behind a curtain of silver-leaved willows, "
            "you find a small clearing. The grass here is soft and white, like moonlit snow.\\\n\\\n"
            "At the center of the clearing, a single dead tree stands. "
            "Hanging from its lowest branch is an iron BELL — cold, black, and silent. "
            "It does not move, even though there is no wind.\\\n\\\n"
            "The grey figure does not follow you here. For now, you are alone with the bell.\\\n\\\n"
            "You can TAKE the Silent Bell. It makes no sound when you touch it."
        ),
        items=[items["silent_bell"]],
        npcs=[],
        exits={"back": "island_silence", "out": "island_silence"},
        on_enter=lambda s: (
            "You push through the silver willows and find the hidden grove.\\\n\\\n"
            "The Silent Bell hangs before you — an iron bell that has never rung, "
            "or has not rung for so long that it has forgotten its own voice.\\\n\\\n"
            "You reach out and touch it. It is cold. Perfectly still. "
            "It does not resist as you lift it from its hook.\\\n\\\n"
            "(You have gained: Silent Bell)"
            if not s.has_flag("got_silent_bell") else
            s.set_flag("got_silent_bell") or None
        ),
    )

    # ===================================================
    # ISLAND 4: THE PROMISED LAND
    # (connects from sea3, direction: promised)
    # ===================================================

    l["promised_land"] = Location(
        "promised_land", "The Promised Land",
        "A land of impossible beauty — golden fruit hangs from silver trees, rivers of wine flow through meadows of eternal spring, and the air smells of home.",
        detailed_desc=(
            "This is the island at the end of the world.\\\n\\\n"
            "It is everything you have ever wanted. The sky is the perfect blue of "
            "a summer afternoon that never fades. The trees bear fruit of pure gold "
            "and silver. Rivers of wine and honey wind through meadows of flowers "
            "that bloom in colours you have never seen.\\\n\\\n"
            "The air is warm and gentle. The grass is soft as silk. "
            "In the distance, you can see white buildings of marble and crystal — "
            "a city that gleams like a promise.\\\n\\\n"
            "Your crew stands frozen, tears streaming down their faces. "
            "Diurán whispers: 'This is it, Captain. This is what the poets sing about. "
            "This is the Land of Promise.'\\\n\\\n"
            "A figure approaches — a luminous being in white robes, "
            "its face radiating infinite kindness and peace.\\\n\\\n"
            "It opens its arms and speaks:\\\n\\\n"
            "'Welcome, Mael Duin. Welcome home. You have crossed the edges of the world, "
            "braved monsters and wonders, and now you stand at the threshold of the Land of Promise. "
            "Here there is no pain, no sorrow, no death. Stay with us forever. "
            "All you have to do is say yes.'\\\n\\\n"
            "The offer hangs in the air. It is the most tempting thing you have ever heard.\\\n\\\n"
            "But somewhere — far away, across the sea — there is a small grey island "
            "where a woman waits. And a child who grew up without a father. "
            "And a story that is not yet finished."
        ),
        items=[],
        npcs=[npcs["guardian_of_peace"]],
        exits={"back": "sea3", "return": "sea3"},
        ambient=lambda s: (
            "The air is perfect. The light is gentle. The river of wine sings a melody "
            "that sounds like your mother's voice."
        ),
        on_enter=lambda s: (
            s.__setattr__('awaiting_choice', 'promised_land') or
            s.set_flag("promised_land_visited") or
            "You step onto the shore of the Promised Land, and your heart breaks with beauty.\n\n"
            "Everything is perfect. The grass is the exact softness you love. "
            "The temperature is exactly right. The fruit tastes of everything good "
            "you have ever eaten, all at once.\n\n"
            "Your crew is weeping. Diurán has dropped to his knees. "
            "Fergus stares at the golden city with the expression of a man who has "
            "found something he did not know he was looking for.\n\n"
            "The GUARDIAN OF PEACE stands before you, arms open, smile radiant.\n\n"
            "'Stay with us,' it says. 'There is nothing for you back there. "
            "No revenge worth taking. No love worth leaving. Stay. "
            "Rest. Be at peace. You have earned it.\n\n"
            "'Say YES and stay forever. Say NO and I will bless your journey home.'\n\n"
            "(Type YES to stay. Type NO to refuse and return home.)\n\n"
            "NOTE: Refusing the offer grants you the Wind of Return, "
            "which you will need to sail home."
            if not s.has_flag("promised_land_visited") else
            s.set_flag("promised_land_visited") or None
        ),
    )

    # ---------------------------------------------------
    # Register all new locations
    # ---------------------------------------------------
    LOCATIONS.update(l)

    # ---------------------------------------------------
    # Connect islands to sea hubs
    # ---------------------------------------------------

    # sea3 gets new exits
    try:
        sea3 = LOCATIONS["sea3"]
        sea3.exits["fish"] = "great_fish_belly"
        sea3.exits["fountain"] = "island_fountain"
        sea3.exits["silence"] = "island_silence"
        sea3.exits["promised"] = "promised_land"
    except KeyError:
        pass  # sea3 may not exist in some contexts
