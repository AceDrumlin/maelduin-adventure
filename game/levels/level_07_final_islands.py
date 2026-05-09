"""Level: 07 Final Islands — The last 5 islands from the original immram."""

from ..engine import LOCATIONS, Location


def register(items, npcs):
    """Register this level's locations and add exits to sea hubs."""
    l = {}
    from .. import engine as _eng

    # ===================================================
    # Helper: register new direction aliases
    # ===================================================
    _eng.VERBS["giant"] = ("go", lambda s, a: _eng.handle_go(s, "giant"))
    _eng.VERBS["treasure"] = ("go", lambda s, a: _eng.handle_go(s, "treasure"))
    _eng.VERBS["dog"] = ("go", lambda s, a: _eng.handle_go(s, "dog"))
    _eng.VERBS["lion"] = ("go", lambda s, a: _eng.handle_go(s, "lion"))
    _eng.VERBS["anchorite"] = ("go", lambda s, a: _eng.handle_go(s, "anchorite"))

    # ===================================================
    # ISLAND 1: THE GIANT KILLER
    # (connects from sea2, direction: "giant")
    # ===================================================

    l["island_giant"] = Location(
        "island_giant", "Island of the Giant Killer",
        "A rocky island dominated by a high cliff. A monstrous giant perches on top, silhouetted against the grey sky, a pile of stones beside him.",
        detailed_desc=(
            "This island is little more than a jagged rock jutting from the sea — a single, "
            "steep-sided CLIFF that rises a hundred feet above the waves. The rock is dark basalt, "
            "streaked with white where seabirds have nested for centuries.\n\n"
            "At the top of the cliff, silhouetted against the grey sky, stands the GIANT. "
            "He is massive — twenty feet of crude muscle and malice — and beside him lies a pile "
            "of stones, each one large enough to crush a man. His shadow falls across the water "
            "like a stain.\n\n"
            "The only way to approach is by sea, and the giant has already seen you. "
            "His arm draws back. A stone is coming.\n\n"
            "The shore is rocky but passable. A narrow path leads to the base of the cliff."
        ),
        items=[],
        npcs=[npcs["giant"]],
        exits={"back": "sea2", "sea": "sea2", "southwest": "sea2"},
        ambient=lambda s: (
            "The giant grumbles on his cliff, occasionally hurling a stone at a passing wave. "
            "The sea around the island is littered with the shattered remains of his target practice."
            if s.has_flag("giant_defeated") or s.has_flag("giant_mollified") else
            "The giant bellows and stamps his feet. Stones tumble down the cliff. "
            "The ground shakes. The air smells of ozone and rage."
        ),
        on_enter=lambda s: (
            (s.set_flag("giant_encountered") or
            "The giant spots your approach and ROARS! He hefts a stone the size of a man's head "
            "and hurls it with terrifying accuracy. It smashes into the side of your curragh, "
            "splintering the frame. Your crew scrambles to keep the boat steady.\n\n"
            "One of your crew — " + (s.lose_crew() or type("obj", (), {"name": "a young man from the west"})()).name
            + " — is struck by a flying splinter and falls, clutching his chest. "
            "He does not rise again.\n\n"
            "The giant bellows with laughter and reaches for another stone.\n\n"
            "You must act! TALK to the giant with the Speaking Feather, FIGHT with the Magic Harpoon, "
            "or GIVE him food (Everlasting Fruit, Crew Provisions) to distract him.")
            if not s.has_flag("giant_encountered") else None
        ),
    )

    # ===================================================
    # ISLAND 2: ISLAND OF THE TREASURE
    # (connects from sea1, direction: "treasure")
    # ===================================================

    l["treasure_cave"] = Location(
        "treasure_cave", "Island of the Treasure",
        "A small, barren island with a single dark cave at its center. The mouth is blocked by a massive serpent coiled in the shadows.",
        detailed_desc=(
            "A small, barren island of grey stone and sparse grass. Nothing grows here — "
            "the soil is too thin, the wind too harsh.\n\n"
            "At the center of the island, a CAVE mouth yawns in the rock. It is dark inside, "
            "but you can see a faint golden glow emanating from the depths — the glint of ancient treasure.\n\n"
            "Coiled before the cave entrance is a massive SERPENT, its scales shimmering with "
            "a deep, oily green. It is the size of a small ship, and its body completely blocks "
            "the way in. Its eyes — vertical slits of gold — open and fix on you with ancient hunger.\n\n"
            "It hisses, tasting the air. It knows what you want. It knows you will have to go through it."
        ),
        items=[],
        npcs=[npcs["treasure_serpent"]],
        exits={"back": "sea1", "sea": "sea1", "northwest": "sea1",
               "in": "treasure_cave", "enter": "treasure_cave"},
        blocked={
            "in": (
                "The serpent blocks the cave entrance with its massive body. "
                "You must deal with it first — FIGHT it, GIVE it the Antidote Herb, or BRIBE it with treasure.",
                lambda s: not s.has_flag("serpent_passed")
            ),
            "enter": (
                "The serpent blocks the cave entrance with its massive body. "
                "You must deal with it first.",
                lambda s: not s.has_flag("serpent_passed")
            ),
        },
        ambient=lambda s: (
            "The serpent watches you with unblinking eyes. Its tail twitches. "
            "The gold gleams from within the cave, calling to you."
            if not s.has_flag("serpent_passed") else
            "The cave mouth is clear. The treasure is yours for the taking. "
            "The air inside smells of ancient dust and forgotten kings."
        ),
        on_enter=lambda s: (
            (s.set_flag("serpent_encountered") or
            "The serpent's head rises, blocking the cave completely.\n\n"
            "'MINE,' it says, the word resonating deep in its throat. "
            "'The gold is mine. The cave is mine. Turn back, little thief.'\n\n"
            "You catch a glimpse of gold beyond the serpent's coils. "
            "The treasure is close enough to touch — if you can get past the guardian.")
            if not s.has_flag("serpent_encountered") else None
        ),
    )

    # ===================================================
    # ISLAND 3: ISLAND OF THE DOG
    # (connects from sea1, direction: "dog")
    # ===================================================

    l["island_dog"] = Location(
        "island_dog", "Island of the Dog",
        "A grassy mound rises from the sea. At its summit, a stone pedestal holds a gleaming silver torc. A massive hound lies beside it, ever watchful.",
        detailed_desc=(
            "A gentle, grassy island — a single green mound rising from the grey sea like the back of a "
            "sleeping whale. The grass is soft and thick, and wildflowers grow in scattered patches.\n\n"
            "At the summit of the mound stands a stone PEDESTAL, ancient and weathered. "
            "Upon it rests a SILVER TORC — a beautiful neck-ring of woven silver wire, "
            "gleaming with the light of a thousand years. It is clearly a masterwork of ancient craftsmanship.\n\n"
            "Before the pedestal, curled like a guard who has never abandoned his post, lies a GREAT HOUND "
            "the size of a small horse. Its coat is iron-grey, and its eyes glow like banked embers. "
            "It watches you approach with the patient stillness of a creature that has waited centuries.\n\n"
            "It does not attack. Not yet. But it makes it clear: the torc is not yours to take lightly."
        ),
        items=[items["silver_torc"]],
        npcs=[npcs["great_hound"]],
        exits={"back": "sea1", "sea": "sea1", "northeast": "sea1"},
        ambient=lambda s: (
            "The hound yawns, revealing teeth like ivory daggers, then settles back down. "
            "Its eyes never leave you. The torc gleams, untouched."
            if not s.has_flag("dog_pacified") else
            "The hound dozes peacefully, one ear flicking occasionally. "
            "The silver torc is gone, but the hound seems content. "
            "It has finally earned its rest."
        ),
        on_enter=lambda s: (
            (s.set_flag("dog_encountered") or
            "The Great Hound rises slowly, hackles raised. A low, rumbling growl issues from its chest.\n\n"
            "It does not charge. It stands between you and the torc, watching, waiting. "
            "This is not a beast of blind rage — this is a guardian of ancient purpose.\n\n"
            "You could GIVE it food (Bowl of Milk, Everlasting Fruit) to earn passage, "
            "FIGHT it, or TALK to it with the Speaking Feather.")
            if not s.has_flag("dog_pacified") and not s.has_flag("dog_encountered") else None
        ),
    )

    # ===================================================
    # ISLAND 4: ISLAND OF THE LION
    # (connects from sea2, direction: "lion")
    # ===================================================

    l["island_lion"] = Location(
        "island_lion", "Island of the Lion",
        "A scrub-covered island with a large cave at its center. A mountain lion crouches before it, wounded and furious.",
        detailed_desc=(
            "A harsh island of scrub brush and sharp rocks. The wind whistles through the thorny bushes, "
            "creating an eerie, keening sound.\n\n"
            "At the center of the island, a wide CAVE mouth opens into the hillside. "
            "Before it, crouched in a posture of pure aggression, is a MOUNTAIN LION. "
            "Its coat is the colour of dried grass, and its muscles ripple beneath the skin "
            "with coiled power.\n\n"
            "But you notice something — a deep GASH along its flank, weeping and infected. "
            "The beast is in agony, and its fury is born of pain. Its roars are as much "
            "anguish as anger.\n\n"
            "You could FIGHT it (with Magic Harpoon or Giant's Club), USE the Silver Bell to calm it, "
            "or TALK to it with the Speaking Feather to learn of its wound."
        ),
        items=[],
        npcs=[npcs["mountain_lion"]],
        exits={"back": "sea2", "sea": "sea2", "south": "sea2"},
        ambient=lambda s: (
            "The lion paces before the cave, limping slightly. Its growls echo off the rocks."
            if not s.has_flag("lion_pacified") and not s.has_flag("lion_fought") else
            "The cave mouth is quiet. The lion is gone — driven off or healed. "
            "A single claw lies on the ground where the beast once stood."
        ),
        on_enter=lambda s: (
            (s.set_flag("lion_encountered") or
            "The mountain lion roars — a raw, ragged sound that vibrates through your bones! "
            "It bares its fangs and crouches, ready to spring.\n\n"
            "But as it shifts its weight, the wound on its flank gapes open — "
            "a terrible, infected gash that oozes and smells of rot. "
            "The beast is suffering. Its attacks are born of pain, not malice.\n\n"
            "You could FIGHT it (with Magic Harpoon, Giant's Club), USE the Silver Bell to calm it, "
            "or TALK to it with the Speaking Feather to learn more.")
            if not s.has_flag("lion_pacified") and not s.has_flag("lion_fought") and not s.has_flag("lion_encountered") else None
        ),
    )

    # ===================================================
    # ISLAND 5: THE SECOND HERMIT (ANCHORITE)
    # (connects from sea2, direction: "anchorite")
    # ===================================================

    l["anchorite_cave"] = Location(
        "anchorite_cave", "The Anchorite's Cave",
        "A small cave on a lonely rock, just large enough for one man to shelter. A single candle burns within, casting a warm, steady light.",
        detailed_desc=(
            "A solitary rock rises from the sea — barely large enough to be called an island. "
            "On it, a small CAVE has been worn into the stone by wind and wave. Inside, "
            "a single CANDLE burns with a flame that does not flicker, though the wind howls outside.\n\n"
            "Sitting cross-legged at the mouth of the cave is a man in a simple grey robe. "
            "His face is weathered by decades of salt spray and contemplation. His eyes are calm — "
            "the calm of someone who has stopped running. Beside him, a small wooden cross rests on a stone.\n\n"
            "He looks up as you approach, and smiles — a warm, genuine smile that makes the grey day "
            "feel brighter. The sea around the rock is unusually calm, as if the water itself respects his peace.\n\n"
            "There is nothing to take here. No treasure. No puzzle. "
            "Only a man who has been waiting to speak with you."
        ),
        items=[],
        npcs=[npcs["anchorite"]],
        exits={"back": "sea2", "sea": "sea2", "east": "sea2"},
        ambient=lambda s: (
            "The candle burns steadily. The sea whispers softly against the rock. "
            "A sense of deep peace settles over you, like a warm blanket after a long voyage."
        ),
        on_enter=lambda s: (
            (s.set_flag("met_anchorite") or
            "The Anchorite looks up and smiles.\n\n"
            "'Sit, Mael Duin. Rest. You have travelled far.\n\n"
            "The sea has shown you many wonders. But the greatest wonder — the one you have been "
            "sailing toward all along — is the one you carry inside you.\n\n"
            "Let us talk.'")
            if not s.has_flag("met_anchorite") else None
        ),
    )

    # ---------------------------------------------------
    # Register all new locations
    # ---------------------------------------------------
    LOCATIONS.update(l)

    # ---------------------------------------------------
    # Connect islands to sea hubs
    # ---------------------------------------------------

    # sea1 gets new exits
    try:
        sea1 = LOCATIONS["sea1"]
        sea1.exits["treasure"] = "treasure_cave"
        sea1.exits["dog"] = "island_dog"
    except KeyError:
        pass  # sea1 may not exist in some contexts

    # sea2 gets new exits
    try:
        sea2 = LOCATIONS["sea2"]
        sea2.exits["giant"] = "island_giant"
        sea2.exits["lion"] = "island_lion"
        sea2.exits["anchorite"] = "anchorite_cave"
    except KeyError:
        pass  # sea2 may not exist in some contexts
