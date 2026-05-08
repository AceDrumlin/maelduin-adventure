"""The Voyage of Mael Duin - World data: locations, items, NPCs, puzzles."""

from .engine import Location, Item, NPC, GameState, LOCATIONS

# ============================================================
# ITEMS
# ============================================================

items = {}

def _make_items():
    i = {}

    i["magic_thread"] = Item(
        "magic_thread", "Magic Thread",
        "A silken thread given by the druid. He said to tie it to your mast for safe passage.",
        examine_text="A thin, silvery thread that glows faintly. It feels warm to the touch, as if alive.",
        aliases=["thread", "druid thread", "silken thread", "magic thread"],
    )

    i["everlasting_fruit"] = Item(
        "everlasting_fruit", "Everlasting Fruit",
        "A golden fruit from the Island of Ants. It never rots and never fills you up, but it smells divine.",
        examine_text="A golden, glowing fruit that looks freshly picked. The smell is intoxicatingly sweet.",
        aliases=["fruit", "golden fruit"],
    )

    i["speaking_feather"] = Item(
        "speaking_feather", "Speaking Feather",
        "A feather from a bird that speaks in human tongues. It whispers secrets when held to the ear.",
        examine_text="A large, iridescent feather. If you hold it to your ear, you can hear faint whispers of ancient wisdom.",
        aliases=["feather", "bird feather"],
    )

    i["glass_shard"] = Item(
        "glass_shard", "Glass Shard",
        "A piece of the glass bridge. It's sharp enough to cut and clear enough to see through.",
        examine_text="A razor-sharp piece of crystalline glass. Through it, you can see things that are far away as if they were close.",
        aliases=["shard", "glass", "glass piece"],
    )

    i["golden_apple"] = Item(
        "golden_apple", "Golden Apple",
        "A perfect apple of pure gold from the Island of the Black Pig. Worth a fortune. Or maybe it's just an apple painted gold? No, it's definitely solid gold.",
        examine_text="A solid gold apple. It's surprisingly heavy. You could buy a small kingdom with this. Or eat it and probably die.",
        aliases=["apple", "gold apple"],
    )

    i["magic_harpoon"] = Item(
        "magic_harpoon", "Magic Harpoon",
        "A harpoon forged by the giant smith of the Smithy Island. It always returns to its thrower.",
        examine_text="A beautifully crafted harpoon of dark iron, etched with spirals. It hums faintly, eager to be thrown.",
        aliases=["harpoon", "spear"],
        takeable=True,
        usable_with=["sea_monster"],
        use_text="You hurl the Magic Harpoon at the sea monster! It strikes true, and the creature roars before diving deep. The harpoon returns to your hand, slick with ichor.",
    )

    i["silver_bell"] = Item(
        "silver_bell", "Silver Bell",
        "A small silver bell from the Island of the Culdees. Its ring can calm storms.",
        examine_text="A delicate silver bell engraved with crosses. When rung, it produces a pure, calming tone.",
        aliases=["bell", "silver bell"],
    )

    i["talking_cat_tribute"] = Item(
        "talking_cat_tribute", "Bowl of Milk",
        "A simple bowl of fresh milk, perfect for offering to a large, judgmental cat.",
        examine_text="A clay bowl filled with creamy milk. A cat would love this.",
        aliases=["milk", "bowl", "bowl of milk"],
    )

    i["hermit_blessing"] = Item(
        "hermit_blessing", "Hermit's Blessing",
        "A small wooden cross given by the holy hermit. It brings peace to the bearer.",
        examine_text="A simple cross of two twigs bound with dried grass. It radiates a quiet calm.",
        aliases=["cross", "blessing", "wooden cross"],
        takeable=True,
    )

    i["otter_pelt"] = Item(
        "otter_pelt", "Otter Pelt",
        "A sleek otter pelt from the hermit's companion. Water slides off it like morning dew.",
        examine_text="A glossy brown otter pelt. It's impossibly soft and completely waterproof.",
        aliases=["pelt", "otter"],
    )

    i["pearl"] = Item(
        "pearl", "Sea Pearl",
        "A shimmering pearl from the Island of Sea-Birds. It glows with a soft inner light.",
        examine_text="A flawless pearl, the size of your thumb, pulsing with a gentle luminescence. It seems to contain the light of a full moon.",
        aliases=["pearl", "sea pearl"],
    )

    i["prophecy_scroll"] = Item(
        "prophecy_scroll", "Prophecy Scroll",
        "A scroll given by the prophetic boy. It contains a riddle about your journey's true purpose.",
        examine_text='The scroll reads: "Seek not the blood of your father\'s slayer, for vengeance is a cup that empties the drinker. The truth of your voyage lies not at the end of your spear, but at the beginning of your heart."',
        aliases=["scroll", "prophecy", "prophecy scroll"],
    )

    i["crew_provisions"] = Item(
        "crew_provisions", "Crew Provisions",
        "Dried fish, oatcakes, and a skin of water. Enough for the voyage ahead.",
        examine_text="Standard Irish seafaring rations. They won't win any culinary awards, but they'll keep you alive.",
        aliases=["provisions", "food", "rations"],
    )

    i["antidote_herb"] = Item(
        "antidote_herb", "Antidote Herb",
        "A strange purple herb from the Island of the Great Snake. Neutralizes any poison.",
        examine_text="A withered purple plant with thorns. The smell is acrid, like burning copper.",
        aliases=["herb", "antidote", "purple herb"],
    )

    i["laughing_potion"] = Item(
        "laughing_potion", "Laughing Potion",
        "A bubbling vial from the Island of the Laughing People. One sip will have you howling.",
        examine_text="A small glass vial containing a fizzing, golden liquid. Bubbles rise endlessly from the bottom.",
        aliases=["potion", "laughing potion", "vial"],
    )

    i["truth_ring"] = Item(
        "truth_ring", "Truth Ring",
        "A ring from the Queen of the Women's Island. She who wears it cannot tell a lie.",
        examine_text="A simple silver band. When you look at it, you feel an overwhelming urge to confess your deepest secrets.",
        aliases=["ring", "truth ring", "silver ring"],
    )

    items.update(i)

_make_items()


# ============================================================
# NPCS
# ============================================================

npcs = {}

def _make_npcs():
    n = {}

    n["druid"] = NPC(
        "druid", "Druid", "An old, wise druid with a beard that reaches his waist. His eyes are milky white — he sees more than mortal men.",
        aliases=["old man", "wise man", "druid"],
        dialogue={
            "greeting": (
                "The druid strokes his long beard and speaks in a voice like rustling leaves:\n\n"
                '"Ah, Mael Duin. I have been expecting you. You have learned of your father\'s murder, '
                'and vengeance burns in your heart. But be warned — the path of revenge is a twisted one, '
                "and the sea holds many mysteries.\n\n"
                'Take this Magic Thread. Tie it to your mast, and it will guide you through the mists. '
                'Take exactly three times nine men — no more, no less — and set sail to the west.\n\n'
                'When you find what you seek... you may find it is not what you expected."\n\n'
                'He presses a shimmering thread into your hand.'
            ),
            "murder": (
                '"Your father, Ailill Ochair Ága. Slain by raiders from the Northern Isles. '
                "They came in the night, burned your village, and left his body on the strand. "
                "Your foster mother found him at dawn, the tide washing his feet.\""
            ),
            "father": (
                '"Ailill was a great warrior. His name meant \"noble wolf\" and he earned it. '
                "He fell with his sword in his hand and his enemies' blood on his blade. "
                "The manner of his death was not shameful — it is revenge that may be."
            ),
            "vengeance": (
                '"Vengeance is like drinking poison and expecting the other man to die. '
                "But I see you will not be swayed by philosophy. Very well — go, seek your revenge. "
                'The sea will teach you what I cannot."'
            ),
            "sea": (
                '"The sea is a living thing, Mael Duin. It has moods, memories, and a sense of humor. '
                "Respect it, and it may let you live. Mock it, and it will show you depths you never wished to see.\""
            ),
        }
    )

    n["cat"] = NPC(
        "cat", "The Cat", "A massive black cat sitting on a golden throne. Its eyes are ancient and knowing, and it looks at you like you're something it just coughed up.",
        aliases=["cat", "big cat", "black cat", "giant cat", "king cat"],
        dialogue={
            "greeting": (
                "The enormous cat blinks slowly, then speaks in a voice like gravel rolling downhill:\n\n"
                '"You are in my house. Few humans visit. Fewer still leave without giving me something I want. '
                "I smell... milk. Do you have milk for me?\"\n\n"
                "The cat's tail twitches expectantly."
            ),
            "milk": (
                '"Milk. Yes. I like milk. Do you have milk?"'
            ),
            "riddle": (
                '"Very well, a riddle. Answer and you may pass:\n\n'
                '"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"\n\n'
                "The cat's whiskers twitch."
            ),
            "answer": (
                '"An echo! Correct. You are smarter than you look, for a human. You may pass."'
            ),
            "wrong": (
                '"Wrong. The correct answer is \"echo.\" I am disappointed in you. Try again or bring me milk."'
            ),
            "on_take": {
                "talking_cat_tribute": lambda state, item: (
                    state.inventory.append(items["pearl"]) or
                    state.set_flag("cat_pacified") or
                    'You offer the bowl of milk to the cat. It sniffs once, then delicately laps it all up.\n\n'
                    '"Acceptable tribute. You may pass through my island safely. And take this — '
                    'a cat always pays its debts."\n\n'
                    'The cat produces a shimmering Pearl from somewhere (you\'re not sure where) and drops it at your feet.\n\n'
                    '(+1 point, and you\'ve earned the cat\'s respect.)'
                )
            }
        }
    )

    n["queen"] = NPC(
        "queen", "The Queen", "The most beautiful woman you have ever seen. She wears a gown of silver thread and a crown of morning dew. Her smile promises everything. Her eyes promise nothing.",
        aliases=["queen", "lady", "beautiful woman"],
        dialogue={
            "greeting": (
                'The Queen of the Women\'s Island smiles radiantly and opens her arms.\n\n'
                '"Welcome, weary voyagers! Stay with us. Eat, drink, be merry. '
                'There is no sorrow here, no hunger, no pain. Only pleasure, forever and ever."\n\n'
                'Around you, beautiful women laugh and dance. The smell of roasting meat fills the air. '
                'Your crew looks at you with hopeful eyes.\n\n'
                "Will you stay, Mael Duin?"
            ),
            "stay": (
                '"Stay with us forever. What is there to return to? A cold village, a blood feud, '
                "a grave you cannot fill with vengeance? Here, there is only warmth.\""
            ),
            "leave": (
                '"Leave? But you\'ve only just arrived! Stay a little longer. One more day. '
                "One more feast. What harm could one more day do?\"",
            ),
            "time": (
                '"Time? What is time but a cage, Mael Duin? Here, there is no time. Only now."'
            ),
            "husband": (
                '"My husband? Gone. Lost at sea. Like so many. Like your father. We are the same, you and I."'
            ),
        }
    )

    n["hermit"] = NPC(
        "hermit", "The Hermit", "A gaunt, holy man in a rough-spun robe, standing on a bare rock in the middle of the sea. An otter sits at his feet, offering him a fish.",
        aliases=["hermit", "holy man", "monk", "ascetic"],
        dialogue={
            "greeting": (
                'The hermit looks at you with eyes that have seen too much and want nothing.\n\n'
                '"You have traveled far, Mael Duin. And yet you have not traveled at all. '
                'The sea you cross is the sea within you — stormy, deep, full of monsters you have yet to name.\n\n'
                "Sit with me. The otter will share his fish. And I will tell you what the waves have been whispering.\""
            ),
            "father": (
                '"Your father is at peace. He does not ask for revenge. He asks that you live."'
            ),
            "voyage": (
                '"Every island you visit is a part of yourself you have not yet met. '
                "The giant ants are your anger. The laughing people are your fear. "
                "The silent cat is your conscience. When you have met them all, you will be whole.\""
            ),
            "blessing": (
                '"I have little to give, but what I have is yours."\n\n'
                "He hands you a small wooden cross, made of two twigs bound with grass.\n\n"
                '"This will bring you peace when you need it most."'
            ),
            "forgiveness": (
                '"The men who killed your father — they were following a blood feud older than your father\'s father. '
                "If you kill them, you do not end the feud. You feed it. And your sons will sail this sea after you.\""
            ),
        }
    )

    n["smith"] = NPC(
        "smith", "The Giant Smith", "A giant forged from muscle and soot, wielding a hammer the size of a horse. His beard crackles with sparks.",
        aliases=["smith", "giant", "blacksmith", "giant smith"],
        dialogue={
            "greeting": (
                "The giant smith bellows over the roar of his forge:\n\n"
                '"HO, LITTLE MAN! You\'ve come to the forge at the edge of the world! '
                "Most people sail right past — they hear the hammering and think it's thunder. "
                "But you came closer. That takes guts. Or stupidity. Both, probably.\"\n\n"
                "He laughs, and the ground shakes."
            ),
            "weapon": (
                '"A weapon, eh? I forged the sword that hangs at the sun\'s belt. '
                "I made the spear that killed the first boar. I can make you something... special.\n\n"
                'But I\'ll need payment. I don\'t work for free. What have you got?"'
            ),
            "trade": (
                '"Something shiny? Something rare? Something that hasn\'t been forged before? '
                "Show me what you have, and I'll tell you if it's worth my time.\""
            ),
            "forgiveness": (
                '"Forgiveness? I don\'t forge that, little man. That you have to make yourself. '
                "And it's the hardest thing you'll ever make.\""
            ),
            "storm": (
                '"The bellows? Oh, that\'s just my bellows. When I pump them, it makes the weather. '
                "Sorry about the storm — I was trying to stoke the fire. Gets cold this far north.\"",
            ),
        }
    )

    n["prophet_boy"] = NPC(
        "prophet_boy", "The Prophetic Boy", "A young boy sitting in a crystal tower, reading a book that has no pages. He looks up and smiles as if he's been expecting you your whole life.",
        aliases=["boy", "prophet", "child", "prophetic boy", "young boy"],
        dialogue={
            "greeting": (
                'The boy closes his book and giggles.\n\n'
                '"You\'re early! I didn\'t expect you for another three chapters. '
                'But since you\'re here — ask me anything. I already know the answer, '
                "but you don't, so it's more fun if you ask.\""
            ),
            "father": (
                '"Your father\'s spirit watches over you. He disapproves of your diet. Too much fish."'
            ),
            "revenge": (
                '"You will find the men who killed your father. But by the time you do, '
                "you won't want to kill them anymore. That's the funny thing about journeys — "
                "they change the traveler more than the destination.\""
            ),
            "home": (
                '"You will return home. But home will not be the same, because you will not be the same. '
                "And that, Mael Duin, is the whole point.\""
            ),
            "death": (
                '"Everyone dies. Even islands die. Even stories die. But some stories get reborn as adventures."'
            ),
        }
    )

    n["laughing_king"] = NPC(
        "laughing_king", "The Laughing King", "A king sitting on a one-legged stool, laughing uncontrollably. Tears stream down his face. He hasn't stopped laughing in years.",
        aliases=["king", "laughing man", "laughing king"],
        dialogue={
            "greeting": (
                "The Laughing King points at you and HOWLS with laughter.\n\n"
                '"HA HA HA HA! Your FACE! The way you LOOK! So SERIOUS! '
                "Like you've never laughed in your LIFE! Oh, this is the BEST day!\"\n\n"
                "He laughs so hard he falls off his stool, gets up, and keeps laughing."
            ),
            "serious": (
                '"Serious? SERIOUS?! Why would anyone be serious when you can LAUGH?! '
                "HA HA HA! Look at the OCEAN! It's SO WET! That's HILARIOUS!\""
            ),
            "help": (
                '"Help? HA! We don\'t need help! We need MORE JOKES! Tell me a joke, sailor! '
                "If it's funny, I'll give you anything! If it's not... HA HA! I'll laugh anyway!\"",
            ),
            "joke": (
                "You tell the king a joke. He freezes for a moment, then erupts with renewed laughter.\n\n"
                '"THAT\'S the one! THAT\'S the best joke I\'ve ever heard! Here, take this!"\n\n'
                'He tosses you a bubbling vial of golden liquid.\n\n'
                '(+1 point, gained: Laughing Potion)'
            ),
            "answer": (
                '"Oh, you didn\'t tell a joke! You ANSWERED a question! That\'s even BETTER! '
                'Wait, no, that doesn\'t make sense, HA HA HA!"'
            ),
        }
    )

    n["diuran_npc"] = NPC(
        "diuran_npc", "Diurán", "Diurán, your poet and scribe, sharpening his quill with a small knife.",
        aliases=["diuran", "poet", "scribe"],
        dialogue={
            "greeting": (
                'Diurán looks up from his parchment.\n\n'
                '"Captain! I\'ve been chronicling our voyage. This will make an excellent epic someday. '
                "Assuming we survive to tell it. How goes the adventure?\""
            ),
            "advice": (
                '"My mother always said: when in doubt, talk to the cat. She was a strange woman."'
            ),
            "poem": (
                '"I\'ve composed a verse for our journey:\n\n'
                '"The waves like greyhounds leap and bound,\n'
                'The sky is cold and grey,\n'
                'We\'ve left our homes on Irish ground,\n'
                "And no one knows the way.\"\n\n"
                "It's a work in progress."
            ),
        }
    )

    n["conganchnes_npc"] = NPC(
        "conganchnes_npc", "Conganchnes", "Conganchnes, the invulnerable warrior, sharpening his already-sharp sword.",
        aliases=["conganchnes", "congan", "warrior", "champion"],
        dialogue={
            "greeting": (
                'Conganchnes grunts. "Captain. We ready for a fight whenever you are. '
                "I've been practicing. The sea is a poor sparring partner — it doesn't hit back.\""
            ),
            "fight": (
                '"I was born for battle, Captain. My skin cannot be pierced, my bones cannot be broken. '
                "The only thing I fear is... paperwork.\""
            ),
        }
    )

    n["fergus_npc"] = NPC(
        "fergus_npc", "Fergus", "Fergus, your navigator, staring at the stars even though it's daytime.",
        aliases=["fergus", "navigator"],
        dialogue={
            "greeting": (
                'Fergus squints at the sky. "Captain. I\'ve been reading the stars. '
                "They say we're heading in the right direction. They also say I should've become a farmer.\""
            ),
            "directions": (
                '"The stars tell me we\'re far from home. But I can get us back — provided we don\'t '
                "sail off the edge of the world. Some say there's a waterfall there.\""
            ),
        }
    )

    npcs.update(n)

_make_npcs()


# ============================================================
# LOCATIONS
# ============================================================

def _make_locations():
    l = {}

    # ---- ACT 1: HOME ----
    l["home"] = Location(
        "home", "Your Village — The Aran Islands",
        "Your village on the Aran Islands. The stone huts huddle against the wind, and the grey Atlantic stretches to the horizon.",
        detailed_desc=(
            "You stand at the edge of your village on Inishmore, the largest of the Aran Islands. "
            "The stone walls of your people's huts are worn smooth by centuries of Atlantic wind. "
            "To the west, the endless grey ocean stretches toward the edge of the known world. "
            "To the east, the fields of Ireland are a distant green smudge.\n\n"
            "Your curragh — a sturdy boat of wicker and hide — is pulled up on the beach, ready to sail. "
            "The memory of your father's murder burns in your chest like a hot coal.\n\n"
            "An old DRUID sits by a fire near the village center."
        ),
        items=[items["crew_provisions"], items["magic_thread"]],
        npcs=[npcs["druid"]],
        exits={"west": "sea1", "beach": "sea1", "sea": "sea1"},
    )

    # ---- ACT 2: THE SEA ----
    l["sea1"] = Location(
        "sea1", "The Open Sea",
        "Your curragh rises and falls on the grey Atlantic. The coast of Ireland is a fading line behind you.",
        detailed_desc=(
            "The wind fills your square-rigged sail. Your crew of 27 men man the oars, "
            "their faces set with determination — and a hint of seasickness.\n\n"
            "The druid's Magic Thread flutters from the mast, pulling gently to the west "
            "as if guided by an invisible hand.\n\n"
            "Ahead, the sea stretches endlessly. Diurán the poet is already writing about "
            "the experience. Conganchnes the invulnerable stands at the prow, scanning for enemies."
        ),
        exits={"west": "island_ants", "north": "island_birds", "northeast": "island_cat", "east": "island_laughing", "south": "glass_bridge"},
        ambient=lambda s: "The waves slap against the curragh's hide. A seabird cries overhead." if s.turns % 2 == 0 else "A cold mist rolls across the water. Somewhere, a bell buoys tolls."
    )

    # ---- ISLAND 1: ANTS ----
    l["island_ants"] = Location(
        "island_ants", "Island of the Giant Ants",
        "An island covered in trees bearing golden fruit. The ground trembles with the marching of giant ants.",
        detailed_desc=(
            "You step onto a beach of white sand. Beyond it, a forest of strange trees rises — "
            "each one laden with golden, glowing fruit that never rots.\n\n"
            "But the trees are crawling with ANTS. Each ant is the size of a horse, "
            "with mandibles that could snap an oar in two.\n\n"
            "They seem to be... farming the trees. They tend the fruit with surprising care.\n\n"
            "One of them is watching you. It tilts its head."
        ),
        items=[items["everlasting_fruit"]],
        npcs=[],
        exits={"east": "sea1", "in": "ants_grove", "grove": "ants_grove"},
        ambient=lambda s: "The ants click their mandibles rhythmically, like tiny swords being sharpened." if not s.has_flag("ants_pacified") else "The ants now ignore you completely.",
    )

    l["ants_grove"] = Location(
        "ants_grove", "The Ant Grove",
        "The heart of the ant colony. A massive queen ant sits atop a mound of golden fruit.",
        detailed_desc=(
            "The grove opens into a clearing where the QUEEN ANT — the size of a house — "
            "sits regally upon a throne of woven branches and golden fruit.\n\n"
            "She regards you with compound eyes that reflect the world in a thousand fragments.\n\n"
            "The fruit here is piled high. A single branch hangs low, offering its golden bounty.\n\n"
            "The worker ants have stopped their labor. They watch you."
        ),
        items=[items["everlasting_fruit"]],
        npcs=[],
        exits={"out": "island_ants", "east": "island_ants"},
        on_enter=lambda s: (
            "The queen ant clicks her mandibles three times. A single ant approaches you, "
            "holding a golden fruit in its jaws. It offers it to you.\n\n"
            "It seems the ants are... friendly? Or they think you're a very ugly ant." if not s.has_flag("ants_pacified") else None
        ),
    )

    # ---- ISLAND 2: BIRDS ----
    l["island_birds"] = Location(
        "island_birds", "Island of the Speaking Birds",
        "An island of sheer cliffs covered in birds of every color. They sing in human tongues.",
        detailed_desc=(
            "The cliffs rise like cathedral walls, every ledge occupied by a bird. "
            "They are not ordinary birds — they speak. Not just mimicry, but actual conversation.\n\n"
            '"Welcome, hairless ones!" cries a red-feathered creature.\n'
            '"Did you bring snacks?" asks another.\n\n'
            "At the top of the cliff, an ENORMOUS OLD BIRD perches — ancient, half-blind, "
            "and clearly the elder of this feathered parliament.\n\n"
            "A single, iridescent feather lies at the base of the cliff."
        ),
        items=[items["speaking_feather"]],
        npcs=[],
        exits={"east": "sea1", "up": "birds_nest", "climb": "birds_nest"},
        ambient=lambda s: "The birds are arguing about the meaning of life. One of them makes an excellent point about salmon." if not s.has_flag("bird_talked") else "The birds now respectfully nod as you pass.",
    )

    l["birds_nest"] = Location(
        "birds_nest", "The Ancient Bird's Perch",
        "The nest of the Ancient Bird, built from silver twigs and lined with gold.",
        detailed_desc=(
            "The Ancient Bird fixes you with one milky eye.\n\n"
            '"Mael Duin," it says. Its voice is like old parchment. "I have been expecting you. '
            'Well, not you specifically. I\'ve been expecting someone. It\'s been a long time since '
            "anyone climbed up here. My legs don't work like they used to.\"\n\n"
            "It shifts on its nest, revealing a stash of shiny objects."
        ),
        items=[],
        npcs=[],
        exits={"down": "island_birds"},
    )

    # ---- ISLAND 3: CAT ISLAND ----
    l["island_cat"] = Location(
        "island_cat", "Island of the Cat",
        "A small, tidy island with a single stone house. A massive black cat sits by the door.",
        detailed_desc=(
            "This island is immaculate. The grass is perfectly trimmed, the path is swept clean, "
            "and a stone house stands at the center with a neatly painted door.\n\n"
            "Before the door, on a golden throne, sits a CAT.\n\n"
            "It is the largest cat you have ever seen — the size of a bear. "
            "Its fur is black as ink, and its eyes are ancient green gold.\n\n"
            "It licks a paw with careful dignity, then looks at you.\n\n"
            "You get the distinct feeling you are being judged."
        ),
        items=[items["talking_cat_tribute"]],
        npcs=[npcs["cat"]],
        exits={"east": "sea1"},
        ambient=lambda s: "The cat's tail flicks once, twice. It is unimpressed with your existence." if not s.has_flag("cat_pacified") else "The cat purrs contentedly as you pass. You have been deemed acceptable.",
    )

    # ---- ISLAND 4: LAUGHING ISLAND ----
    l["island_laughing"] = Location(
        "island_laughing", "Island of the Laughing People",
        "An island where EVERYONE is laughing. Babies laugh. Dogs laugh. Even the trees seem to chuckle.",
        detailed_desc=(
            "As you step ashore, a wave of laughter hits you. Everyone — and everything — on this island is laughing.\n\n"
            "A farmer laughs as he plows. His horse laughs. The chickens laugh. "
            "A woman offers you a cup of water, laughing so hard she spills half of it.\n\n"
            "In the center of the village, a KING sits on a one-legged stool, laughing uproariously "
            "at absolutely nothing visible.\n\n"
            "Your crew is starting to giggle. Conganchnes looks deeply uncomfortable."
        ),
        items=[],
        npcs=[npcs["laughing_king"]],
        exits={"east": "sea1"},
        ambient=lambda s: "HA HA HA HA HA! The laughter never stops. You feel your own lips twitching." if not s.has_flag("king_pacified") else "The island seems quieter now. People still chuckle, but it's a gentle mirth.",
    )

    # ---- ISLAND 5: GLASS BRIDGE ----
    l["glass_bridge"] = Location(
        "glass_bridge", "Island of the Glass Bridge",
        "A glittering island with a bridge made entirely of crystal, leading to a palace beyond.",
        detailed_desc=(
            "A palace of white marble gleams in the distance. But to reach it, you must cross "
            "a BRIDGE made entirely of transparent glass, suspended over a chasm of swirling mist.\n\n"
            "The glass is perfectly clear. You can see straight through it to the jagged rocks below.\n\n"
            "A beautiful woman stands on the far side of the bridge, beckoning.\n\n"
            '"Cross, brave sailor. I will not let you fall."'
        ),
        items=[items["glass_shard"]],
        npcs=[],
        exits={"east": "sea1", "cross": "glass_palace", "bridge": "glass_palace"},
        blocked={"cross": ("a sheer drop" if False else None, lambda s: not s.has_flag("crossed_bridge"))},
        ambient=lambda s: "The glass bridge shimmers in the light. It's beautiful and absolutely terrifying."
    )

    l["glass_palace"] = Location(
        "glass_palace", "The Glass Palace",
        "A palace of crystal and light. Music plays from nowhere, and the air smells of honey.",
        detailed_desc=(
            "You step into a palace that seems built from frozen light. "
            "Every surface reflects a thousand colors. Music — harps and flutes — "
            "plays without any musician.\n\n"
            "A beautiful woman offers you a seat on cushions of silk.\n\n"
            "This place feels like a dream. It also feels like a trap.\n\n"
            "The floor is suspiciously transparent in places."
        ),
        items=[],
        npcs=[],
        exits={"back": "glass_bridge", "east": "glass_bridge"},
    )

    # ---- ISLAND 6: SMITHY ----
    l["island_smithy"] = Location(
        "island_smithy", "Island of the Smithy",
        "An island of volcanic rock, dominated by a massive forge that belches fire and smoke.",
        detailed_desc=(
            "The air shimmers with heat. A mountain of slag and cinder rises from the center of the island, "
            "topped by a FORGE the size of a hill.\n\n"
            "CLANG. CLANG. CLANG.\n\n"
            "Each hammer strike shakes the ground beneath your feet.\n\n"
            "A GIANT works the bellows — each breath of the bellows sends a gale across the island. "
            "You realize the bellows are what create storms at sea. The giant sneezes, and a bolt of lightning "
            "cracks across the sky.\n\n"
            "He hasn't noticed you yet."
        ),
        npcs=[npcs["smith"]],
        exits={"east": "sea1"},
        items=[],
        ambient=lambda s: "The forge roars. Embers drift like fireflies. The giant hums a tune that sounds suspiciously like a lullaby." if not s.has_flag("got_harpoon") else "The forge is quiet now. The giant waves cheerily as you pass.",
    )

    # ---- ISLAND 7: WOMEN'S ISLAND ----
    l["island_women"] = Location(
        "island_women", "Island of Women",
        "An island of perpetual sunset, where beautiful women feast, dance, and sing endlessly.",
        detailed_desc=(
            "You step onto an island that seems untouched by time. The sun is always just setting, "
            "painting everything in gold and rose.\n\n"
            "Beautiful women in silken gowns approach, offering trays of roasted meats, fresh bread, "
            "and honeyed wine. Music floats on the warm air.\n\n"
            "Your crew is already drooling.\n\n"
            "At the center of the feast, a QUEEN sits on a throne of flowers. She smiles at you."
        ),
        npcs=[npcs["queen"]],
        items=[items["truth_ring"]],
        exits={"east": "sea1"},
        ambient=lambda s: "The music swells. A woman laughs somewhere. The food smells incredible." if not s.has_flag("left_women") else "The island is silent now. The palace stands empty, as if everyone left in a hurry.",
    )

    # ---- ISLAND 8: HERMIT'S ROCK ----
    l["hermit_rock"] = Location(
        "hermit_rock", "The Hermit's Rock",
        "A bare rock in the middle of the ocean. A holy man stands upon it, one with the elements.",
        detailed_desc=(
            "You approach a solitary ROCK jutting from the sea. It is no larger than your curragh.\n\n"
            "Upon it stands a HERMIT, soaked by spray, lashed by wind, his eyes closed in prayer.\n\n"
            "At his feet, an OTTER sits, holding a fish in its mouth.\n\n"
            "The hermit opens his eyes and looks directly at you.\n\n"
            '"I was wondering when you\'d get here," he says. "The otter caught a large one today — there\'s enough for everyone."'
        ),
        npcs=[npcs["hermit"]],
        items=[items["otter_pelt"]],
        exits={"east": "sea1"},
        on_enter=lambda s: (
            "The hermit's blessing washes over you as you step onto the rock. "
            "For a moment, the weight of your quest lifts from your shoulders." if not s.has_flag("met_hermit") else None
        ),
    )

    # ---- ISLAND 9: CULDEES (MONASTERY) ----
    l["island_culdees"] = Location(
        "island_culdees", "Island of the Culdees",
        "A peaceful island with a small monastery. A bell rings itself, calling the monks to prayer.",
        detailed_desc=(
            "A monastery of grey stone stands on this quiet island. The Culdees — anchorites devoted to God — "
            "tend a garden of herbs and vegetables.\n\n"
            "A SILVER BELL hangs in a small tower. It rings of its own accord, at the exact hour of prayer.\n\n"
            "The monks pay you no mind. They are busy praying, gardening, and ignoring the mortal world.\n\n"
            "One monk looks up from his weeding and nods once."
        ),
        items=[items["silver_bell"]],
        npcs=[],
        exits={"east": "sea1"},
        ambient=lambda s: "The self-ringing bell tolls softly. A monk chants in Latin. It is... peaceful." if not s.has_flag("took_bell") else "Without the bell, the island feels incomplete. The monks seem quieter now.",
    )

    # ---- ISLAND 10: PROPHECY TOWER ----
    l["prophecy_tower"] = Location(
        "prophecy_tower", "Island of Prophecy",
        "An island with a single tower of crystal, rising from the sea like a prism.",
        detailed_desc=(
            "A tower of pure crystal rises from the sea, catching the light and scattering it into rainbows.\n\n"
            "A door of silver stands open. Inside, stairs spiral upward.\n\n"
            "At the top of the tower, a YOUNG BOY sits cross-legged, reading a book that has no pages.\n\n"
            'He looks up and grins. "Took you long enough!"'
        ),
        npcs=[npcs["prophet_boy"]],
        items=[items["prophecy_scroll"]],
        exits={"east": "sea1", "up": "prophecy_tower", "enter": "prophecy_tower"},
    )

    # ---- ISLAND 11: SEA MONSTERS ----
    l["sea_monsters"] = Location(
        "sea_monsters", "The Sea of Monsters",
        "Still, glassy water that feels wrong. Something moves beneath the surface.",
        detailed_desc=(
            "The sea is unnaturally calm — flat as glass. Not a breath of wind stirs.\n\n"
            "Your crew rows nervously. Too quietly. Too watchfully.\n\n"
            "Something HUGE passes beneath the boat. A shadow the size of your curragh glides in the depths.\n\n"
            "Then — a giant hand reaches up from the water, grabbing the side of your boat!"
        ),
        npcs=[],
        items=[],
        exits={"east": "island_women", "west": "sea1", "north": "island_laughing"},
        on_enter=lambda s: (
            "A monstrous hand erupts from the water, clutching the gunwale of your curragh! "
            "The boat lurches violently. Crew members grab for their swords.\n\n"
            "You have a moment to act!" if not s.has_flag("sea_monster_defeated") else None
        ),
        ambient=lambda s: "The water beneath you is impossibly deep and dark. Something is watching." if not s.has_flag("sea_monster_defeated") else "The sea is calm and safe now."
    )

    # ---- ISLAND 12: THE BLACK PIG ----
    l["black_pig"] = Location(
        "black_pig", "Island of the Black Pig",
        "An island with a single massive apple tree made of gold. A black pig guards it.",
        detailed_desc=(
            "A single tree stands on this island — an apple tree whose trunk, branches, and leaves "
            "are made of solid GOLD. Golden apples hang from its branches.\n\n"
            "At the base of the tree, a BLACK PIG the size of a cow snoozes contentedly.\n\n"
            "The pig's tusks are the size of daggers. Its snout twitches as it dreams of... "
            "probably truffles. Or world domination. Hard to tell.\n\n"
            "A sign next to the tree reads: \"Take one apple, lose one hand.\"\n\n"
            "The handwriting is surprisingly good for a pig."
        ),
        items=[items["golden_apple"]],
        npcs=[],
        exits={"east": "sea1"},
        ambient=lambda s: f"The pig snores. Each snore sounds like a small earthquake." if not s.has_flag("apple_taken") else "The pig glares at you balefully. It remembers.",
    )

    # ---- ISLAND 13: THE SPEAKING SKULL ----
    l["speaking_skull"] = Location(
        "speaking_skull", "Island of the Thorny Bush",
        "An island with a single thorny bush growing through an old human skull. The skull speaks.",
        detailed_desc=(
            "On this small, barren island, a thorny bush grows from a crack in the rock.\n\n"
            "A HUMAN SKULL is impaled on one of its thorns. As you approach, the skull's jaw "
            "drops open, and a voice rasps from its empty mouth:\n\n"
            '"A visitor! Do you have any idea how long I\'ve been sitting here? '
            "Decades! Centuries! And let me tell you, the view doesn't improve. "
            "Just bushes. Bushes and more bushes.\"\n\n"
            "The skull's empty eye sockets seem to fix you with an expectant stare."
        ),
        npcs=[],
        items=[],
        exits={"east": "sea1"},
        on_enter=lambda s: (
            f'"{s.get_location().name if s.get_location() else "..."}"' if not s.has_flag("met_skull") else None
        ),
        ambient=lambda s: "The bush rustles, though there's no wind. The skull mutters something about the younger generation."
    )

    # ---- ISLAND 14: THE SERPENT ----
    l["serpent_island"] = Location(
        "serpent_island", "Island of the Great Snake",
        "An island circled by a serpent so large it forms a continuous ring around the land.",
        detailed_desc=(
            "You approach an island that is encircled by an enormous SNAKE — "
            "its body forms a complete ring around the land, head to tail.\n\n"
            "As you draw near, the serpent raises its head — large enough to swallow your boat whole — "
            "and hisses.\n\n"
            "But it doesn't attack. It just... watches. Its scales shimmer with a purple iridescence.\n\n"
            "There is a narrow gap between the serpent's head and tail. You could slip through if you're quick.\n\n"
            "Purple herbs grow on the island — the antidote to the serpent's poison."
        ),
        items=[items["antidote_herb"]],
        npcs=[],
        exits={"east": "sea1", "through": "serpent_island_center"},
        blocked={"through": ("the serpent blocks your way", lambda s: not s.has_flag("serpent_pacified"))},
        ambient=lambda s: "The serpent's scales make a soft rustling sound as it shifts, like leaves in a gentle breeze." if not s.has_flag("serpent_pacified") else "The serpent has moved aside, allowing passage.",
    )

    l["serpent_island_center"] = Location(
        "serpent_island_center", "Within the Serpent's Ring",
        "The center of the serpent-ringed island. Peaceful, fertile, eerily quiet.",
        detailed_desc=(
            "The center of the island is surprisingly idyllic — green grass, a small spring, "
            "and the purple antidote herbs growing in abundance.\n\n"
            "A stone altar stands at the center, carved with ouroboros — the snake eating its own tail.\n\n"
            "The serpent's head looms above you, but it makes no move to attack. It seems to be... waiting."
        ),
        items=[items["antidote_herb"]],
        npcs=[],
        exits={"out": "serpent_island"},
    )

    # ---- FINAL ISLAND: HOME AGAIN ----
    l["homecoming"] = Location(
        "homecoming", "The Coast of Ireland — Home at Last",
        "The familiar coast of Ireland. But something is different now.",
        detailed_desc=(
            "After countless islands and wonders, your curragh finally scrapes onto a familiar shore.\n\n"
            "This is the coast where your father was murdered. You recognize the strand, "
            "the black rocks, the twisted tree.\n\n"
            "And there — by a fire — sit three men. They are the raiders who killed Ailill Ochair Ága.\n\n"
            "They see you. They reach for their weapons.\n\n"
            "But there is something in their eyes — not defiance, but weariness. "
            "They are old now. The firelight shows grey in their beards.\n\n"
            "One of them speaks: \"We knew you would come, son of Ailill. We have been waiting.\"\n\n"
            "The prophecy rings in your ears: vengeance is a cup that empties the drinker.\n\n"
            "What do you do?"
        ),
        npcs=[],
        items=[],
        exits={},
        on_enter=lambda s: (
            "The wind carries the smell of home. Your crew stands behind you, weapons drawn.\n\n"
            "This is the moment your voyage was meant to end. But how?" if not s.has_flag("confronted") else None
        ),
    )

    # Register all
    l.update({
        "ants_grove": l["ants_grove"],
        "birds_nest": l["birds_nest"],
        "glass_palace": l["glass_palace"],
        "prophecy_tower": l["prophecy_tower"],
        "serpent_island": l["serpent_island"],
        "serpent_island_center": l["serpent_island_center"],
        "homecoming": l["homecoming"],
    })

    LOCATIONS.update(l)

_make_locations()


# ============================================================
# SPECIAL EVENT HANDLERS (registered in engine.py)
# ============================================================

def setup_special_events():
    """Configure special interactions that need custom logic."""
    pass
