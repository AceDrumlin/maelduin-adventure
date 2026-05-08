"""Level: 03 Sea3 — The Final Stretch"""

from ..engine import Location
from ._shared import items, npcs


def register(items, npcs):
    """Register this level's locations."""
    from ..engine import LOCATIONS
    l = {}

    # ═══════════════════════════════════════════
    # THE FINAL SEA
    # ═══════════════════════════════════════════
    l["sea3"] = Location(
        "sea3", "The Final Sea",
        "The water is black as ink. The sky swirls with colors you've never seen. The end is near.",
        detailed_desc=(
            "This is the edge of the known world. The sea here is dark and still — "
            "no fish, no birds, no wind. Just your breath and the creak of the curragh.\n\n"
            "The Magic Thread glows brightly, pulling with purpose. You feel that your journey "
            "is almost at an end. The air tastes different here — older, like a room that's been sealed for centuries.\n\n"
            "Diurán has stopped writing. He stares at the horizon, pale. "
            "'Captain... I think we're close. I can feel it in my bones. "
            "Also, my quill just wrote 'DEATH' on its own. Probably a coincidence.'\n\n"
            "Islands dot the darkness like scattered jewels. One of them must be the home of your father's killers. "
            "Or it might be another wonder. At this point, you're not sure which is which."
        ),
        exits={
            "north": "serpent_island", "east": "black_pig",
            "west": "speaking_skull", "south": "island_water_horse",
            "northeast": "island_fiery_pigs", "northwest": "island_revolving_castle",
            "southeast": "island_trumpet", "southwest": "island_demons",
            "gold": "island_golden_pillar",
            "home": "homecoming",
        },
        ambient=lambda s: (
            "The silence is oppressive. Even the water refuses to make noise. "
            "Your own heartbeat sounds like a drum."
            if s.turns % 2 == 0 else
            "A single light glimmers on the horizon, then vanishes. "
            "Was it a star? A ship? A warning? Or just Fergus's lantern?"
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE GREAT SNAKE
    # ═══════════════════════════════════════════
    l["serpent_island"] = Location(
        "serpent_island", "Island of the Great Snake",
        "An island circled by a serpent so large it forms a continuous ring around the land.",
        detailed_desc=(
            "You approach an island that is encircled by an enormous SNAKE — "
            "its body forms a complete ring around the land, head to tail. "
            "The scales are the size of shields, each one a different shade of purple and green.\n\n"
            "As you draw near, the serpent raises its head — large enough to swallow your boat whole — "
            "and hisses. The sound is like a thousand swords being drawn at once.\n\n"
            "But it doesn't attack. It just... watches. Its scales shimmer with a purple iridescence. "
            "It blinks slowly. One eye is the size of your curragh.\n\n"
            "There is a narrow gap between the serpent's head and tail. You could slip through if you're quick.\n\n"
            "Purple herbs grow on the island — the antidote to the serpent's poison. "
            "The serpent seems to be... guarding them? Or growing them?"
        ),
        items=[items["antidote_herb"]],
        npcs=[],
        exits={"south": "sea3", "through": "serpent_island_center"},
        blocked={"through": ("the serpent blocks your way — it responds to the sound of silver",
                             lambda s: s.get_item_from_inventory("silver_bell") is None)},
        ambient=lambda s: (
            "The serpent's scales make a soft rustling sound as it shifts, like leaves in a gentle breeze. "
            "It is beautiful and terrifying in equal measure."
            if not s.has_flag("serpent_pacified") else
            "The serpent has moved aside, allowing passage. It nods as you pass. A polite snake."
        ),
    )

    l["serpent_island_center"] = Location(
        "serpent_island_center", "Within the Serpent's Ring",
        "The center of the serpent-ringed island. Peaceful, fertile, eerily quiet.",
        detailed_desc=(
            "The center of the island is surprisingly idyllic — green grass, a small spring, "
            "and the purple antidote herbs growing in abundance. "
            "It's like a hidden garden, protected from the rest of the world.\n\n"
            "A stone altar stands at the center, carved with ouroboros — the snake eating its own tail. "
            "The carving is so old that the edges have worn smooth.\n\n"
            "The serpent's head looms above you, but it makes no move to attack. "
            "It seems to be... waiting. Maybe it wants you to understand something.\n\n"
            "A quiet voice — perhaps your own thought, perhaps the island's — whispers: "
            "'The serpent guards not the island, but the wisdom within.'"
        ),
        items=[items["antidote_herb"]],
        npcs=[],
        exits={"out": "serpent_island"},
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE BLACK PIG
    # ═══════════════════════════════════════════
    l["black_pig"] = Location(
        "black_pig", "Island of the Black Pig",
        "An island with a single massive apple tree made of gold. A black pig guards it.",
        detailed_desc=(
            "A single tree stands on this island — an apple tree whose trunk, branches, and leaves "
            "are made of solid GOLD. Golden apples hang from its branches, glowing with an inner light.\n\n"
            "At the base of the tree, a BLACK PIG the size of a cow snoozes contentedly. "
            "Its sides heave with each breath. Drool — liquid gold — pools beneath its snout.\n\n"
            "The pig's tusks are the size of daggers. Its snout twitches as it dreams of... "
            "probably truffles. Or world domination. Hard to tell.\n\n"
            "A sign next to the tree reads: \"Take one apple, lose one hand.\"\n\n"
            "The handwriting is surprisingly good for a pig. "
            "There's a small footnote that says 'No, seriously. I will bite you.'"
        ),
        items=[items["golden_apple"]],
        npcs=[],
        exits={"west": "sea3"},
        ambient=lambda s: (
            "The pig snores. Each snore sounds like a small earthquake. "
            "A golden apple falls from the tree and the pig catches it in its sleep without opening its eyes."
            if not s.has_flag("apple_taken") else
            "The pig glares at you balefully. It remembers. It will always remember."
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE SPEAKING SKULL
    # ═══════════════════════════════════════════
    l["speaking_skull"] = Location(
        "speaking_skull", "Island of the Thorny Bush",
        "An island with a single thorny bush growing through an old human skull. The skull speaks.",
        detailed_desc=(
            "On this small, barren island, a single thorny bush grows from a crack in the rock. "
            "There is nothing else. No trees, no grass, no sign of life except the bush.\n\n"
            "A HUMAN SKULL is impaled on one of its thorns. The bone is yellowed with age, "
            "polished smooth by centuries of wind and rain.\n\n"
            "As you approach, the skull's jaw drops open, and a voice rasps from its empty mouth:\n\n"
            '"A visitor! Do you have any idea how long I\'ve been sitting here? '
            "Decades! Centuries! And let me tell you, the view doesn't improve. "
            "Just bushes. Bushes and more bushes.\"\n\n"
            "The skull's empty eye sockets seem to fix you with an expectant stare. "
            "Despite having no facial muscles, it manages to convey profound boredom."
        ),
        npcs=[npcs["skull"]],
        items=[],
        exits={"east": "sea3"},
        ambient=lambda s: (
            "The bush rustles, though there's no wind. "
            "The skull mutters something about the younger generation."
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE WATER HORSE (Kelpie)
    # ═══════════════════════════════════════════
    l["island_water_horse"] = Location(
        "island_water_horse", "Island of the Water Horse",
        "A small, grassy island where a magnificent white horse stands on the water's surface as if it were solid ground.",
        detailed_desc=(
            "The island is little more than a grassy knoll emerging from the dark sea. "
            "But standing on the WATER beside it — not in it, ON it — is a magnificent WHITE HORSE.\n\n"
            "Its mane flows like seaweed. Its hooves rest on the surface of the sea as if on marble. "
            "It looks at you with eyes that are deep, dark pools — bottomless, hypnotic.\n\n"
            '"Welcome, traveler," it says. Its voice is smooth as silk and twice as slippery. '
            '"I can carry you across the ocean faster than any ship. '
            'I can take you anywhere you wish to go. Just climb on my back."\n\n'
            "Your crew shifts uneasily. Fergus whispers: 'Captain, I don't think that's a horse. "
            "I think that's a kelpie. If you ride it, it'll drag you to the bottom of the sea "
            "and eat your liver.'\n\n"
            "The horse smiles. It has too many teeth. Far too many."
        ),
        items=[],
        npcs=[npcs["water_horse"]],
        exits={"north": "sea3", "ride": "water_horse_doom", "mount": "water_horse_doom"},
        blocked={"ride": ("the kelpie's eyes are hypnotic — you need something to break its spell",
                          lambda s: s.get_item_from_inventory("truth_ring") is None
                          and s.get_item_from_inventory("laughing_potion") is None)},
        ambient=lambda s: (
            "The Water Horse stamps a hoof, and the water ripples in perfect, hypnotic circles. "
            "It is singing something in a language that sounds like waves."
            if not s.has_flag("kelpie_tricked") else
            "The Water Horse glares at you from a distance. "
            "It does not appreciate being outsmarted. Its too-many teeth are bared."
        ),
        on_enter=lambda s: (
            'The Water Horse tosses its head. "Come, climb on. '
            'I promise you a ride you\'ll never forget."\n\n'
            "Fergus grabs your arm. 'Don't do it, Captain! "
            "A kelpie will take you to the bottom of the sea and devour you!'\n\n"
            "You have the Truth Ring — you could expose its lies.\n"
            "Or the Laughing Potion — you could make it too drunk to drown you.\n"
            "Or you could try to ride it and hope for the best (not recommended)."
            if not s.has_flag("kelpie_tricked") else None
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE FIERY PIGS
    # ═══════════════════════════════════════════
    l["island_fiery_pigs"] = Location(
        "island_fiery_pigs", "Island of the Fiery Pigs",
        "An island covered in blackened grass. Pigs made of living flame trot across the scorched earth.",
        detailed_desc=(
            "The grass on this island is charred black. Small fires smolder everywhere. "
            "And trotting across the landscape are PIGS — but pigs made entirely of flame, "
            "their bodies crackling with fire, their eyes burning coals.\n\n"
            "Wherever they walk, the grass ignites. They seem to be... grazing on the ashes? "
            "One of them roots in the sooty earth and pulls out a glowing ember, which it eats with evident pleasure.\n\n"
            "At the center of the island, a stone altar stands untouched by fire. "
            "An inscription reads:\n\n"
            "'To calm the Fiery Pigs, you must give them what they crave — '\n"
            "'not water, not earth, but the memory of what was lost.'\n"
            "'A sacrifice of ash for ash, of fire for fire.'\n\n"
            "The pigs snort, and small fireballs shoot from their nostrils. "
            "They look hungry. Not for food — for something else."
        ),
        items=[items["fiery_ash"]],
        npcs=[],
        exits={"southwest": "sea3"},
        blocked={"southwest": ("the fiery pigs surge around you — the heat is unbearable",
                                lambda s: not s.has_flag("fiery_pigs_pacified"))},
        ambient=lambda s: (
            "The fiery pigs snort and stamp. Their hooves leave scorch marks on the stone. "
            "They will not let you leave until you give them what they want.\n\n"
            "The altar inscription says: 'A sacrifice of ash for ash, of fire for fire.'"
            if not s.has_flag("fiery_pigs_pacified") else
            "The pigs have calmed down. They now glow warmly instead of burning hotly. "
            "One of them offers you a smoldering clover."
        ),
        on_enter=lambda s: (
            "The fiery pigs surround you! They are hungry — not for food, but for something else.\n\n"
            "The altar's inscription echoes in your mind: 'A sacrifice of ash for ash, of fire for fire.'\n\n"
            "If you have Fiery Ash, you could give it to them."
            if not s.has_flag("fiery_pigs_pacified") else None
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE REVOLVING CASTLE
    # ═══════════════════════════════════════════
    l["island_revolving_castle"] = Location(
        "island_revolving_castle", "Island of the Revolving Castle",
        "A castle made of black stone that slowly rotates on a central axis. Its doors spin past at regular intervals.",
        detailed_desc=(
            "A strange castle dominates this island — a fortress of black obsidian that turns slowly, "
            "ceaselessly, like a great stone top. It has been turning for so long that the ground around it is worn into a perfect circle.\n\n"
            "It has four doors — each one a different color: Red, Blue, Green, and Black. "
            "As the castle revolves, each door passes a stone platform at the base, "
            "staying aligned for only a few heartbeats before continuing its rotation.\n\n"
            "The doors are locked. Or rather... each door has a keyhole, but the key must match the moment.\n\n"
            "A stone plaque reads: 'Enter at the turning of the world. The right door at the right time. "
            "Choose poorly, and the castle will never let you go.'\n\n"
            "The castle GRINDS as it turns. It sounds almost alive. "
            "Like a great stone beast, breathing in slow circles."
        ),
        items=[],
        npcs=[],
        exits={"southeast": "sea3",
               "red": "castle_red", "blue": "castle_blue",
               "green": "castle_green", "black": "castle_black"},
        blocked={"red": ("the Red Door is locked — a keyhole turns restlessly",
                          lambda s: s.get_item_from_inventory("revolving_key") is None),
                 "blue": ("the Blue Door is sealed — no keyhole, just a smooth surface", lambda s: True),
                 "green": ("the Green Door is frozen shut", lambda s: True),
                 "black": ("the Black Door is a void — you sense nothing but emptiness beyond", lambda s: True)},
        ambient=lambda s: (
            "CREEEEAK... The castle turns. A door aligns with the platform, waits, then passes. "
            "The Red Door has a keyhole that seems to match your restless key. "
            "The others are sealed."
            if not s.has_flag("castle_entered") else
            "The castle has stopped revolving. It sits silently, as if exhausted by the effort. "
            "The doors are all open now, revealing empty rooms."
        ),
        on_enter=lambda s: (
            "The castle grinds to a halt. The Red Door is aligned with the platform. "
            "Its keyhole glows faintly, waiting.\n\n"
            "Your Revolving Key vibrates eagerly in your pack.\n\n"
            "Type RED to enter the Red Door with your key."
            if s.get_item_from_inventory("revolving_key") and not s.has_flag("castle_entered")
            else None
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE GIANT TRUMPET
    # ═══════════════════════════════════════════
    l["island_trumpet"] = Location(
        "island_trumpet", "Island of the Giant Trumpet",
        "A barren island with a single giant brass trumpet mounted on a cliff, pointing out to sea.",
        detailed_desc=(
            "This island is a bare rock with a single feature: an enormous BRASS TRUMPET, "
            "as large as a ship, mounted on a stone pedestal at the edge of a cliff.\n\n"
            "The trumpet points out to sea. A mechanism of gears and levers connects to "
            "a set of giant leather bellows behind it. One pull of the lever would produce a sound "
            "that would carry for miles.\n\n"
            "A chilling inscription is carved into the pedestal:\n\n"
            "'One blast of this trumpet will shatter any ship within a league. "
            "The sound is the voice of the sea god's anger. "
            "Do not sound it unless you wish to drown all who hear.'\n\n"
            "But you notice something: there is a small CLOTH stuffed into the trumpet's bell. "
            "Someone else was here before you, and they tried to muffle it. "
            "Maybe they knew something you don't."
        ),
        items=[items["earplugs"], items["trumpet_muffler"]],
        npcs=[],
        exits={"northwest": "sea3"},
        ambient=lambda s: (
            "The trumpet gleams dully in the grey light. Wind whistles across its mouth, "
            "producing a low, mournful hum. It sounds like a lament for ships that never returned."
            if not s.has_flag("trumpet_muffled") else
            "The trumpet sits silent and harmless, its mouth stuffed with cloth. "
            "The wind no longer whistles through it. It is, for the first time in ages, truly quiet."
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE DEMON SMITH
    # ═══════════════════════════════════════════
    l["island_demons"] = Location(
        "island_demons", "Island of the Demon Smith",
        "An island wreathed in black smoke. The ground is hot to the touch. A forge burns with flames that are blacker than night.",
        detailed_desc=(
            "The air is thick with smoke and the smell of brimstone. The ground is black glass — "
            "melted and cooled volcanic rock that crunches under your feet. "
            "Each step sounds like breaking bones.\n\n"
            "At the center of the island, a massive FORGE burns with BLACK FLAMES — "
            "fire that is darker than the smoke around it, fire that drinks light instead of giving it.\n\n"
            "A DEMON works the forge — a figure of cracked stone and living ember, "
            "his eyes like cooling coals. He hammers a piece of black iron into a coin.\n\n"
            "CLANG. Each strike sends out a wave of heat that warps the air. "
            "CLANG. Each coin bears the face of a different screaming soul.\n\n"
            "The demon looks up. 'Ah. A customer. Come to trade? "
            "I don't get many visitors. Most people see the black flames and turn back. "
            "Cowards.' He grins. His teeth are made of molten gold.\n\n"
            "Coins of black iron are piled on a table nearby."
        ),
        items=[items["demon_coin"]],
        npcs=[npcs["demon_smith"]],
        exits={"northeast": "sea3"},
        ambient=lambda s: (
            "The black flames hiss and pop. Each bubble of molten metal sounds like a whispered secret. "
            "The demon hums a tune — 'Danny Boy' in a minor key."
            if not s.has_flag("met_demon") else
            "The forge still burns, but the demon nods politely as you pass. 'Come back anytime.'"
        ),
    )

    # ═══════════════════════════════════════════
    # ISLAND OF THE GOLDEN PILLAR
    # ═══════════════════════════════════════════
    l["island_golden_pillar"] = Location(
        "island_golden_pillar", "Island of the Golden Pillar",
        "A pillar of solid gold rises from the sea, impossibly tall. A silver fishnet hangs from its apex.",
        detailed_desc=(
            "A PILLAR of solid gold rises from the sea — so tall that its top disappears into the clouds. "
            "It is wider than a house, and polished to a mirror shine. "
            "You can see your reflection in it — and behind your reflection, the reflection of your crew, "
            "and behind them, the reflection of the entire sea.\n\n"
            "Carved into its surface are images of fish, ships, and sea creatures — "
            "the history of the Atlantic, written in gold. You see ships from every era: "
            "curraghs, Viking longships, Spanish galleons, modern trawlers.\n\n"
            "Near the top — just visible at the cloud line — a SILVER NET hangs from a hook. "
            "Something gleams inside it. Something golden.\n\n"
            "At the base of the pillar, a tidepool contains a single, perfectly round opening — "
            "a keyhole. Or a socket. Or a mouth.\n\n"
            "An inscription at the base reads:\n\n"
            "'He who would climb to heaven's gate must first see what the silver net makes great. "
            "The golden pillar holds the sky. The silver net holds the answer. "
            "Catch what glitters, but know its weight.'\n\n"
            "The pillar hums faintly, like a tuning fork struck by the gods."
        ),
        items=[items["silver_net"], items["crystal_pillar_fish"]],
        npcs=[],
        exits={"northeast": "sea3", "east": "sea3"},
        ambient=lambda s: (
            "The golden pillar gleams, reflecting the grey sea and sky. "
            "Standing beside it, you feel very small and very mortal. "
            "Also very poor, because it's solid gold and you can't take it with you."
            if not s.has_flag("got_golden_fish") else
            "The golden pillar still gleams, but the silver net hangs empty now. "
            "The pillar seems... satisfied, somehow."
        ),
    )

    LOCATIONS.update(l)
