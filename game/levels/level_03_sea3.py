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
            "homecoming": "homecoming_beach", "home": "homecoming_beach",
        },
        ambient=lambda s: (
            "The silence is oppressive. Even the water refuses to make noise. "
            "Your own heartbeat sounds like a drum."
            if s.turns % 2 == 0 else
            "A single light glimmers on the horizon, then vanishes. "
            "Was it a star? A ship? A warning? Or just Fergus's lantern?"
        ),
        npcs=[npcs["young_conganchnes"]],
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
        npcs=[npcs["serpent"]],
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
        npcs=[npcs["black_pig"]],
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
            "ceaselessly, like a great stone top. It has been turning for so long that the ground around it is worn into a perfect circle.\\n\\n"
            "It has four doors — each one a different color: Red, Blue, Green, and Black. "
            "As the castle revolves, each door passes a stone platform at the base, "
            "staying aligned for only a few heartbeats before continuing its rotation.\\n\\n"
            "The doors are locked. The keyhole on the Red Door turns restlessly, as if waiting for a matching key...\\n\\n"
            "A stone plaque reads: 'Enter at the turning of the world. The right door at the right time. "
            "Choose poorly, and the castle will never let you go.'\\n\\n"
            "The castle GRINDS as it turns. It sounds almost alive. "
            "Like a great stone beast, breathing in slow circles.\\n\\n"
            "You could try to USE the REVOLVING KEY on the DOOR, "
            "or EXAMINE the WALLS for a secret entrance, "
            "or WAIT for the right moment."
        ),
        items=[],
        npcs=[],
        exits={"southeast": "sea3",
               "enter": "castle_entrance", "in": "castle_entrance"},
        blocked={"enter": ("the castle is still revolving — the doors spin past too quickly to enter",
                           lambda s: not s.has_flag("castle_unlocked")),
                 "in": ("the castle is still revolving — the doors spin past too quickly to enter",
                        lambda s: not s.has_flag("castle_unlocked"))},
        ambient=lambda s: (
            "CREEEEAK... The castle turns. A door aligns with the platform, waits, then passes. "
            "The Red Door has a keyhole that seems to match your restless key."
            if not s.has_flag("castle_unlocked") else
            "The castle has stopped revolving. It sits silently, as if exhausted by the effort. "
            "The Red Door stands open, revealing a dark entrance hallway."
        ),
        on_enter=lambda s: (
            "The castle looms before you, a fortress of black obsidian that turns slowly, ceaselessly.\\n\\n"
            "Four doors — Red, Blue, Green, and Black — revolve past a stone platform at the base, "
            "each aligned for only a few heartbeats before continuing their eternal rotation.\\n\\n"
            "The Revolving Key in your pack vibrates eagerly. It wants to be turned.\\n\\n"
            "Three ways in:\\n"
            "  1. USE the REVOLVING KEY on the DOOR (the intended path)\\n"
            "  2. EXAMINE the WALLS for a secret entrance\\n"
            "  3. WAIT and time the doors (patience is a virtue)\\n\\n"
            "Or you could simply leave and explore other islands."
            if not s.has_flag("castle_unlocked") else None
        ),
    )

    # ── Castle Entrance (hallway) ──
    l["castle_entrance"] = Location(
        "castle_entrance", "The Castle Entrance",
        "A dark hallway of polished obsidian, lit by a faint red glow from a door at the far end.",
        detailed_desc=(
            "You step through the entrance into a dark hallway. The walls are polished black obsidian, "
            "smooth as glass. A faint red glow emanates from a door at the far end — the Red Door, now open.\\n\\n"
            "The air is still and cold. The grinding of the castle has stopped, and the silence is profound.\\n\\n"
            "Carved into the wall beside you, an inscription reads:\\n\\n"
            "'The heart of the castle beats in the Red Chamber. Enter, and claim what was left for you.'\\n\\n"
            "The Red Door beckons."
        ),
        items=[],
        npcs=[],
        exits={"out": "island_revolving_castle", "back": "island_revolving_castle",
               "red": "castle_red", "forward": "castle_red", "in": "castle_red"},
        ambient=lambda s: (
            "The silence is so complete you can hear your own heartbeat. "
            "The red glow pulses faintly, like a distant beacon."
        ),
    )

    # ── Revolving Castle interior rooms ──
    l["castle_red"] = Location(
        "castle_red", "The Red Door — Heart of the Castle",
        "A circular chamber of black obsidian. A single shaft of red light illuminates a stone pedestal at the center.",
        detailed_desc=(
            "The Red Door swings open with a groan of ancient hinges. You step into a circular chamber "
            "of polished black obsidian. The walls curve inward overhead, forming a dome. "
            "A single shaft of red light — from where, you cannot tell — illuminates a STONE PEDESTAL "
            "at the exact center of the room.\\n\\n"
            "On the pedestal rests a SILVER NET, finely woven, shimmering like moonlight on water.\\n\\n"
            "The castle shudders around you, as if acknowledging your presence. "
            "You have entered the heart of the turning world."
        ),
        items=[items["silver_net"]],
        npcs=[npcs["garbh"]],
        exits={"out": "castle_entrance", "back": "castle_entrance"},
        on_enter=lambda s: (
            s.set_flag("castle_entered") or
            s.set_flag("confronted_murderer") or
            "The Red Door swings open with a groan of ancient hinges...\\n\\n"
            "You step into the heart of the Revolving Castle. The room is circular, "
            "made of black obsidian polished to a mirror shine. A red shaft of light "
            "illuminates a pedestal at the center.\\n\\n"
            "On the pedestal: a Silver Net. This must be what you came for.\\n\\n"
            "But you are not alone. A ONE-EYED WARRIOR sits on a stone bench in the shadows, "
            "a drinking horn in his hand. He watches you with a tired, knowing gaze.\\n\\n"
            "This is Garbh. The man who killed your father."
            if not s.has_flag("castle_entered") else None
        ),
    )

    l["castle_blue"] = Location(
        "castle_blue", "The Blue Door — Chamber of Storms",
        "A room filled with howling wind and freezing rain. The floor is slick with ice.",
        detailed_desc=(
            "The Blue Door opens onto a tempest. Wind howls through the chamber, "
            "whipping rain into your face. The floor is treacherous with black ice.\\n\\n"
            "In the center of the storm, barely visible through the sleet, a pedestal "
            "holds a single item: a pair of WAX EARPLUGS.\\n\\n"
            "The storm is too fierce. You cannot reach it without being frozen solid. "
            "This door was not meant for you."
        ),
        items=[],
        npcs=[],
        exits={"out": "castle_entrance", "back": "castle_entrance"},
        on_enter=lambda s: (
            "The Blue Door resists at first, then opens to a howling gale. "
            "You shield your eyes against the stinging ice. "
            "There is nothing for you here — the storm would kill you before you reached the center."
            if not s.has_flag("castle_blue_entered") else None
        ),
    )

    l["castle_green"] = Location(
        "castle_green", "The Green Door — Garden of Stone",
        "A room that was once a garden. Petrified vines hang from the ceiling like frozen snakes.",
        detailed_desc=(
            "The Green Door opens onto what was once a lush garden. Everything — vines, flowers, "
            "a small fountain — has turned to grey stone. The air is dry and still.\\n\\n"
            "In the center of the garden, a stone table holds a SCROLL etched in stone, "
            "but the text is too weathered to read. Whatever wisdom was here has been lost to time.\\n\\n"
            "This door, too, was sealed long ago. The Green path holds nothing for you now."
        ),
        items=[],
        npcs=[],
        exits={"out": "castle_entrance", "back": "castle_entrance"},
    )

    l["castle_black"] = Location(
        "castle_black", "The Black Door — The Void",
        "Absolute darkness. The floor may or may not exist. You cannot tell.",
        detailed_desc=(
            "You open the Black Door and step into — nothing.\\n\\n"
            "There is no light. No sound. No sensation of floor beneath your feet, "
            "yet you do not fall. You simply... exist, in a space that has no dimensions.\\n\\n"
            "A voice — perhaps your own thoughts — whispers: 'You were not meant to enter here. "
            "The Black Door is the end of all journeys, not the middle. Go back.'\\n\\n"
            "You step backward and find yourself outside again, shaken."
        ),
        items=[],
        npcs=[],
        exits={"out": "castle_entrance", "back": "castle_entrance"},
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
            "Someone else was here before you, and they tried to muffle it.\n\n"
            "There are also WAX EARPLUGS lying nearby. Whoever was here left in a hurry.\n\n"
            "WARNING: The trumpet's bellows are filling again. If you try to leave without muffling "
            "the trumpet, the blast will deafen your crew!"
        ),
        items=[items["earplugs"], items["trumpet_muffler"]],
        npcs=[],
        exits={"northwest": "sea3"},
        blocked={"northwest": ("THE TRUMPET BLASTS as you try to leave! The sound is deafening! "
                               "You stagger back, ears ringing. You need to muffle the trumpet first, "
                               "or protect yourself with earplugs!",
                               lambda s: not s.has_flag("trumpet_muffled")
                               and not s.has_flag("earplugs_used"))},
        ambient=lambda s: (
            "The bellows creak as they fill with air. The trumpet is almost ready to sound again... "
            "You can feel the pressure building in the mechanism."
            if not s.has_flag("trumpet_muffled") else
            "The trumpet sits silent and harmless, its mouth stuffed with cloth. "
            "The wind no longer whistles through it. It is, for the first time in ages, truly quiet."
        ),
        on_enter=lambda s: (
            "The ground trembles slightly. The bellows behind the trumpet are slowly filling with air. "
            "You don't have much time before it sounds again.\n\n"
            "Use the EARPLUGS to protect your ears, or use the MUFFLER on the TRUMPET to silence it permanently."
            if not s.has_flag("trumpet_muffled") else None
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
