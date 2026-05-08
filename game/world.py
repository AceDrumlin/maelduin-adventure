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
        "A shimmering pearl from the Island of the Cat. It glows with a soft inner light.",
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

    # ---- NEW ITEMS for the extra islands ----

    i["earplugs"] = Item(
        "earplugs", "Wax Earplugs",
        "A pair of earplugs made from beeswax. Perfect for blocking out loud noises.",
        examine_text="Two small, pliable balls of beeswax, carefully shaped to fit in your ears. They smell faintly of honey.",
        aliases=["earplugs", "wax plugs", "beeswax", "wax earplugs"],
    )

    i["wisdom_salmon"] = Item(
        "wisdom_salmon", "Wisdom Salmon",
        "A salmon from the Stream of Wisdom. Eating it will grant you incredible knowledge.",
        examine_text="A silver-scaled salmon with eyes that seem to hold the secrets of the universe. It glows faintly with inner light.",
        aliases=["salmon", "fish", "wisdom fish"],
        takeable=True,
        use_text="You take a bite of the Wisdom Salmon. Instantly, your mind floods with understanding. You see the patterns in the waves, the names of all the stars, and why the druid smiled cryptically. For a moment, you understand everything. Then you take another bite because it tastes really good.",
    )

    i["silver_net"] = Item(
        "silver_net", "Silver Net",
        "A finely woven net of silver thread. It shimmers like moonlight on water.",
        examine_text="A delicate net made of interwoven silver strands. It's surprisingly strong for its weight. Perfect for catching something... fishy?",
        aliases=["net", "silver net", "silver fishnet"],
    )

    i["demon_coin"] = Item(
        "demon_coin", "Demon's Coin",
        "A coin of black iron from the Demon's Forge, still warm to the touch. It bears the face of a laughing devil.",
        examine_text="A heavy coin of scorched iron. One side shows a leering demon face. The other side is blank, as if waiting to be stamped with your own face. Egotistical currency.",
        aliases=["coin", "demon coin", "iron coin", "black coin"],
    )

    i["crystal_pillar_fish"] = Item(
        "crystal_pillar_fish", "Golden Fish",
        "A fish made of pure gold, caught in a silver net at the base of the Golden Pillar.",
        examine_text="A perfect, life-sized fish crafted from solid gold. Every scale is individually rendered. It's worth a king's ransom. It's also very, very heavy.",
        aliases=["gold fish", "golden fish", "fish"],
    )

    i["trumpet_muffler"] = Item(
        "trumpet_muffler", "Trumpet Muffler",
        "A strange cloth stuffed into the giant trumpet's bell. It seems to be made of soundproofed otter fur.",
        examine_text="A thick, heavy cloth made of layered otter pelts and waxed linen. Whoever put this here knew exactly what they were doing.",
        aliases=["muffler", "cloth", "otter cloth"],
    )

    i["revolving_key"] = Item(
        "revolving_key", "Revolving Key",
        "A bronze key that turns in your hand of its own accord, as if it cannot stop moving.",
        examine_text="A large bronze key that rotates slowly in your palm. When you hold it still, it vibrates insistently. It wants to be turned.",
        aliases=["key", "bronze key", "revolving key"],
    )

    i["fiery_ash"] = Item(
        "fiery_ash", "Fiery Ash",
        "A handful of ash from the burning grass of the Island of Fiery Pigs. It still smolders warmly.",
        examine_text="Grey ash with tiny red embers glowing within. It's warm but not hot enough to burn. It smells like a campfire and roasted acorns.",
        aliases=["ash", "fiery ash", "embers"],
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
                "\"Ah, Mael Duin. I have been expecting you. You have learned of your father's murder, "
                "and vengeance burns in your heart. But be warned — the path of revenge is a twisted one, "
                "and the sea holds many mysteries.\n\n"
                "Take this Magic Thread. Tie it to your mast, and it will guide you through the mists. "
                "Take exactly three times nine men — no more, no less — and set sail to the west.\n\n"
                "When you find what you seek... you may find it is not what you expected.\"\n\n"
                "He presses a shimmering thread into your hand."
            ),
            "murder": (
                "\"Your father, Ailill Ochair Ága. Slain by raiders from the Northern Isles. "
                "They came in the night, burned your village, and left his body on the strand. "
                "Your foster mother found him at dawn, the tide washing his feet.\""
            ),
            "father": (
                "\"Ailill was a great warrior. His name meant 'noble wolf' and he earned it. "
                "He fell with his sword in his hand and his enemies' blood on his blade. "
                "The manner of his death was not shameful — it is revenge that may be.\""
            ),
            "vengeance": (
                "\"Vengeance is like drinking poison and expecting the other man to die. "
                "But I see you will not be swayed by philosophy. Very well — go, seek your revenge. "
                "The sea will teach you what I cannot.\""
            ),
            "sea": (
                "\"The sea is a living thing, Mael Duin. It has moods, memories, and a sense of humor. "
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
                "\"You are in my house. Few humans visit. Fewer still leave without giving me something I want. "
                "I smell... milk. Do you have milk for me?\"\n\n"
                "The cat's tail twitches expectantly."
            ),
            "milk": (
                "\"Milk. Yes. I like milk. Do you have milk?\""
            ),
            "riddle": (
                "\"Very well, a riddle. Answer and you may pass:\n\n"
                "\"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\"\n\n"
                "The cat's whiskers twitch."
            ),
            "answer": (
                "\"An echo! Correct. You are smarter than you look, for a human. You may pass.\""
            ),
            "wrong": (
                "\"Wrong. The correct answer is 'echo.' I am disappointed in you. Try again or bring me milk.\""
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
                "It's a work in progress.\""
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

    # ---- NEW NPCs ----

    n["skull"] = NPC(
        "skull", "The Talking Skull", "A human skull impaled on a thornbush. Its jaw clatters as it speaks, and its empty eye sockets somehow convey a look of profound boredom.",
        aliases=["skull", "talking skull", "skull", "head", "jaw"],
        dialogue={
            "greeting": (
                'The skull clacks its teeth together before speaking:\n\n'
                '"Well, well, well. A visitor! Do you have any idea how long I\'ve been sitting here? '
                "Decades! Centuries! And let me tell you, the view doesn't improve. "
                "Just bushes. Bushes and more bushes.\"\n\n"
                "The skull's jaw hangs open in what might be a sigh."
            ),
            "bush": (
                '"Thornbush. Singular. There\'s only the one. It\'s spiritual, apparently. '
                "I think it's just a bush that got lucky.\""
            ),
            "story": (
                '"How I ended up here? That\'s a long story involving a shipwreck, a bad decision, '
                "and a seagull with a grudge. The short version: don't trust seagulls.\""
            ),
            "advice": (
                '"My advice? Get off this island. There\'s nothing here but me and this bush, '
                "and I'm not much for conversation after the first century.\""
            ),
            "death": (
                '"Death? I\'ve been dead so long I\'m thinking of applying for a second career. '
                "The afterlife is mostly waiting, interspersed with brief moments of existential dread.\""
            ),
        }
    )

    n["water_horse"] = NPC(
        "water_horse", "The Water Horse", "A magnificent white horse standing on the water's surface as if it were solid ground. Its mane flows like seaweed, and its eyes are deep, dark pools that seem to have no bottom.",
        aliases=["horse", "water horse", "kelpie", "white horse", "sea horse"],
        dialogue={
            "greeting": (
                "The Water Horse tosses its mane and speaks in a voice like waves on a shingle beach:\n\n"
                "\"Well met, traveler! I am the Water Horse of the Western Sea. "
                "I can carry you across the ocean faster than any curragh. "
                "I can take you anywhere you wish to go.\"\n\n"
                "It stamps a hoof, and the water ripples outward in perfect circles.\n\n"
                "\"Climb on. I promise you a ride you'll never forget.\""
            ),
            "ride": (
                "\"Climb on my back. I'll take you across the sea. "
                "I won't even drown you. Much.\""
            ),
            "trick": (
                "The horse snorts. \"Trick? Me? I'm a horse of my word. Mostly.\""
            ),
            "forgiveness": (
                "\"Forgiveness? I know nothing of that. I am a creature of the moment. "
                "The past is like water under the bridge — gone, forgotten, and probably damp.\""
            ),
        }
    )

    n["demon_smith"] = NPC(
        "demon_smith", "The Demon Smith", "A hulking figure of fire and shadow, working a forge that burns with black flames. His skin is cracked like cooling lava, and his eyes glow like embers.",
        aliases=["demon", "smith", "demon smith", "black smith", "fire demon"],
        dialogue={
            "greeting": (
                'The Demon Smith looks up from his forge. The heat is intense.\n\n'
                '\"A mortal. How... bold. Most sailors see the smoke and turn back. \"\n'
                "But you came closer. Either you have great courage or a poor sense of self-preservation. "
                "I respect both.\"\n\n"
                "He gestures to a pile of iron coins on a stone table.\n\n"
                '"I forge coins here. Coins of power. Coins of pain. Coins that buy things no mortal merchant can offer. '
                "Would you like to make a trade?\""
            ),
            "trade": (
                '"I trade in souls, memories, and shiny objects. What do you have to offer?"'
            ),
            "coins": (
                '"These coins are forged from the tears of bankers and the screams of auditors. '
                "They spend anywhere — including places where money has no meaning.\""
            ),
            "fire": (
                '"The fire? That\'s not ordinary fire. That\'s the first fire — the spark Prometheus stole. "\n'
                "I bought it from him. He was short on rent that month.\""
            ),
            "soul": (
                '"Your soul? Please. I have a warehouse full of souls. They\'re the most overrated currency in the universe. "\n'
                "Give me something interesting instead.\""
            ),
        }
    )

    npcs.update(n)

_make_npcs()


# ============================================================
# LOCATIONS
# ============================================================

# Helper for unique items check in inventory
def _has_item(state, item_id):
    return any(i.id == item_id for i in state.inventory)

def _has_flag(state, flag):
    return state.has_flag(flag)


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

    # ---- ACT 2: THE SEA - First waters ----
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
        exits={
            "west": "island_ants", "north": "island_birds",
            "northeast": "island_cat", "east": "island_laughing",
            "south": "glass_bridge", "northwest": "island_smithy",
            "southeast": "island_women", "southwest": "sea_monsters",
            "deeper": "sea2", "far": "sea2",
        },
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
        exits={"west": "sea2"},
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
        exits={"south": "sea2"},
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
        exits={"north": "sea2", "up": "prophecy_tower", "enter": "prophecy_tower"},
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
        ambient=lambda s: "The pig snores. Each snore sounds like a small earthquake." if not s.has_flag("apple_taken") else "The pig glares at you balefully. It remembers.",
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
        npcs=[npcs["skull"]],
        items=[],
        exits={"east": "sea1"},
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

    # ================================================================
    # NEW ISLANDS FOR SEA2 AND SEA3
    # ================================================================

    # ---- SEA2: Deeper Waters ----
    l["sea2"] = Location(
        "sea2", "The Deeper Sea",
        "The water has changed color — a deep, midnight blue. Strange lights flicker beneath the surface.",
        detailed_desc=(
            "You have sailed beyond the familiar waters into the deeper sea. "
            "The coastline of Ireland is long gone. The sky is a different shade of grey here — "
            "somehow older, more ancient.\n\n"
            "The druid's Magic Thread pulls steadily westward. The wind has a different voice — "
            "it whispers names you don't recognize.\n\n"
            "Fergus squints at the horizon. 'We're in uncharted waters now, Captain. "
            "The stars are different here. They have... stranger names.'"
        ),
        exits={
            "north": "island_culdees", "south": "prophecy_tower",
            "east": "hermit_rock", "west": "island_four_fences",
            "northwest": "island_salmon", "deeper": "sea3",
            "far": "sea3", "back": "sea1",
        },
        ambient=lambda s: (
            "Bioluminescent creatures drift past the boat, trailing sparks of cold fire. "
            "The water glows where your oars dip in." if s.turns % 3 == 0 else
            "A deep, resonant sound echoes from below — like a whale singing, but older. "
            "Much older."
        ),
    )

    # ---- SEA3: The Final Stretch ----
    l["sea3"] = Location(
        "sea3", "The Final Sea",
        "The water is black as ink. The sky swirls with colors you've never seen. The end is near.",
        detailed_desc=(
            "This is the edge of the known world. The sea here is dark and still — "
            "no fish, no birds, no wind. Just your breath and the creak of the curragh.\n\n"
            "The Magic Thread glows brightly, pulling with purpose. You feel that your journey "
            "is almost at an end.\n\n"
            "Diurán has stopped writing. He stares at the horizon, pale. "
            "'Captain... I think we're close. I can feel it in my bones.'\n\n"
            "Islands dot the darkness like scattered jewels. One of them must be the home of your father's killers."
        ),
        exits={
            "north": "serpent_island", "east": "black_pig",
            "west": "speaking_skull", "south": "island_water_horse",
            "northeast": "island_fiery_pigs", "northwest": "island_revolving_castle",
            "southeast": "island_trumpet", "southwest": "island_demons",
            "southwest2": "island_golden_pillar",
            "west_north": "island_golden_pillar",
            "home": "homecoming",
        },
        ambient=lambda s: "The silence is oppressive. Even the water refuses to make noise." if s.turns % 2 == 0 else "A single light glimmers on the horizon, then vanishes. Was it a star? A ship? A warning?",
    )

    # ---- NEW ISLAND 1: FOUR FENCES ----
    l["island_four_fences"] = Location(
        "island_four_fences", "Island of the Four Fences",
        "An island divided by four fences — gold, silver, copper, and crystal. You must choose the right one.",
        detailed_desc=(
            "A flat, grey island stretches before you. It is divided into four sections by four different fences.\n\n"
            "The first fence is made of GOLD — gleaming, magnificent, clearly the most valuable. A gate stands open.\n\n"
            "The second fence is made of SILVER — elegant, understated, with a latch that lifts easily.\n\n"
            "The third fence is made of COPPER — humble, practical, with a simple rope holding the gate shut.\n\n"
            "The fourth fence is made of CRYSTAL — delicate, beautiful, but it looks like it would shatter at a touch.\n\n"
            "A faded sign reads: 'Beyond one fence lies a great treasure. Beyond the others, only regret. Choose wisely.'\n\n"
            "In the center of the island, just visible beyond all four fences, a treasure chest gleams."
        ),
        items=[],
        npcs=[],
        exits={"east": "sea2"},
        ambient=lambda s: "The fences seem to hum with different energies. The gold one radiates greed. The copper one whispers humility." if not s.has_flag("four_fences_solved") else "The copper fence has crumbled to dust. The path to the treasure is open.",
        on_enter=lambda s: (
            "A faint breeze carries a whisper: 'Not all that glitters is gold. Not all that is humble is worthless.'"
        ),
    )

    # ---- NEW ISLAND 2: SALMON STREAM ----
    l["island_salmon"] = Location(
        "island_salmon", "Island of the Wisdom Salmon",
        "An island with a single stream running through it, filled with silver salmon that leap against the current.",
        detailed_desc=(
            "A small, green island with a crystal-clear stream running from a spring in the center to the sea.\n\n"
            "The stream is FULL of salmon — fat, silver, magnificent fish that leap against the current "
            "with incredible determination.\n\n"
            "But these are no ordinary salmon. When you look into their eyes, you see... understanding. "
            "These are the Salmon of Wisdom, who ate the nine hazelnuts of knowledge.\n\n"
            "A small sign on the bank reads: 'He who eats of the Salmon of Wisdom gains the knowledge of all things. "
            "But catching one requires cunning, for they are wiser than any fish has a right to be.'\n\n"
            "The salmon look at you smugly. They know you don't have a fishing rod."
        ),
        items=[],
        npcs=[],
        exits={"southeast": "sea2"},
        ambient=lambda s: "A salmon leaps clear of the water, hangs in the air for a moment, and grins at you before splashing back down." if not s.has_flag("caught_salmon") else "The remaining salmon eye you warily. They've heard about what happened to their cousin.",
    )

    # ---- NEW ISLAND 3: WATER HORSE (KELPIE) ----
    l["island_water_horse"] = Location(
        "island_water_horse", "Island of the Water Horse",
        "A small, grassy island where a magnificent white horse stands on the water's surface as if it were solid ground.",
        detailed_desc=(
            "The island is little more than a grassy knoll emerging from the dark sea. "
            "But standing on the WATER beside it — not in it, ON it — is a magnificent WHITE HORSE.\n\n"
            "Its mane flows like seaweed. Its hooves rest on the surface of the sea as if on marble. "
            "It looks at you with eyes that are deep, dark pools.\n\n"
            '"Welcome, traveler," it says. "I can carry you across the ocean faster than any ship. '
            'I can take you anywhere you wish to go. Just climb on my back."\n\n'
            "Your crew shifts uneasily. Fergus whispers: 'Captain, I don't think that's a horse. "
            "I think that's a kelpie.'\n\n"
            "The horse smiles. It has too many teeth."
        ),
        items=[],
        npcs=[npcs["water_horse"]],
        exits={"north": "sea3"},
        ambient=lambda s: "The Water Horse stamps a hoof, and the water ripples in perfect, hypnotic circles." if not s.has_flag("kelpie_tricked") else "The Water Horse glares at you from a distance. It does not appreciate being outsmarted.",
        on_enter=lambda s: (
            'The Water Horse tosses its head. "Come, climb on. I promise you a ride you\'ll never forget."\n\n'
            "Fergus grabs your arm. 'Don't do it, Captain! A kelpie will take you to the bottom of the sea and devour you!'"
        ) if not s.has_flag("kelpie_tricked") else None,
    )

    # ---- NEW ISLAND 4: FIERY PIGS ----
    l["island_fiery_pigs"] = Location(
        "island_fiery_pigs", "Island of the Fiery Pigs",
        "An island covered in blackened grass. Pigs made of living flame trot across the scorched earth.",
        detailed_desc=(
            "The grass on this island is charred black. Small fires smolder everywhere. "
            "And trotting across the landscape are PIGS — but pigs made entirely of flame, "
            "their bodies crackling with fire, their eyes burning coals.\n\n"
            "Wherever they walk, the grass ignites. They seem to be... grazing on the ashes?\n\n"
            "At the center of the island, a stone altar stands untouched by fire. "
            "An inscription reads:\n\n"
            "'To calm the Fiery Pigs, you must give them what they crave — '\n"
            "'not water, not earth, but the memory of what was lost. '\n"
            "'A sacrifice of ash for ash, of fire for fire.'\n\n"
            "The pigs snort, and small fireballs shoot from their nostrils.\n"
        ),
        items=[],
        npcs=[],
        exits={"southwest": "sea3"},
        ambient=lambda s: "A pig trots past you, close enough that you feel the heat. It sniffs at your shoes, then moves on, disappointed." if not s.has_flag("fiery_pigs_pacified") else "The pigs have calmed down. They now glow warmly instead of burning hotly.",
    )

    # ---- NEW ISLAND 5: REVOLVING CASTLE ----
    l["island_revolving_castle"] = Location(
        "island_revolving_castle", "Island of the Revolving Castle",
        "A castle made of black stone that slowly rotates on a central axis. Its doors spin past at regular intervals.",
        detailed_desc=(
            "A strange castle dominates this island — a fortress of black obsidian that turns slowly, "
            "ceaselessly, like a great stone top.\n\n"
            "It has four doors — each one a different color: Red, Blue, Green, and Black. "
            "As the castle revolves, each door passes a stone platform at the base, "
            "staying aligned for only a few heartbeats before continuing its rotation.\n\n"
            "The doors are locked. Or rather... each door has a keyhole, but the key must match the moment.\n\n"
            "A stone plaque reads: 'Enter at the turning of the world. The right door at the right time. "
            "Choose poorly, and the castle will never let you go.'\n\n"
            "The castle GRINDS as it turns. It sounds almost alive."
        ),
        items=[],
        npcs=[],
        exits={"southeast": "sea3"},
        ambient=lambda s: "CREEEEAK... The castle turns. A door aligns with the platform, waits, then passes. The next one approaches." if not s.has_flag("castle_entered") else "The castle has stopped revolving. It sits silently, as if exhausted by the effort.",
    )

    # ---- NEW ISLAND 6: THE TRUMPET ISLAND ----
    l["island_trumpet"] = Location(
        "island_trumpet", "Island of the Giant Trumpet",
        "A barren island with a single giant brass trumpet mounted on a cliff, pointing out to sea.",
        detailed_desc=(
            "This island is a bare rock with a single feature: an enormous BRASS TRUMPET, "
            "as large as a ship, mounted on a stone pedestal at the edge of a cliff.\n\n"
            "The trumpet points out to sea. A mechanism of gears and levers connects to "
            "a set of giant leather bellows behind it.\n\n"
            "A chilling inscription is carved into the pedestal:\n\n"
            "'One blast of this trumpet will shatter any ship within a league. "
            "The sound is the voice of the sea god's anger. "
            "Do not sound it unless you wish to drown all who hear.'\n\n"
            "But you notice something: there is a small CLOTH stuffed into the trumpet's bell. "
            "Someone else was here before you, and they tried to muffle it."
        ),
        items=[items["earplugs"], items["trumpet_muffler"]],
        npcs=[],
        exits={"northwest": "sea3"},
        ambient=lambda s: "The trumpet gleams dully in the grey light. Wind whistles across its mouth, producing a low, mournful hum." if not s.has_flag("trumpet_muffled") else "The trumpet sits silent and harmless, its mouth stuffed with cloth.",
    )

    # ---- NEW ISLAND 7: ISLAND OF DEMONS ----
    l["island_demons"] = Location(
        "island_demons", "Island of the Demon Smith",
        "An island wreathed in black smoke. The ground is hot to the touch. A forge burns in the center with flames that are blacker than night.",
        detailed_desc=(
            "The air is thick with smoke and the smell of brimstone. The ground is black glass — "
            "melted and cooled volcanic rock.\n\n"
            "At the center of the island, a massive FORGE burns with BLACK FLAMES — "
            "fire that is darker than the smoke around it.\n\n"
            "A DEMON works the forge — a figure of cracked stone and living ember, "
            "his eyes like cooling coals. He hammers a piece of black iron into a coin.\n\n"
            "CLANG. Each strike sends out a wave of heat that warps the air.\n\n"
            "The demon looks up. 'Ah. A customer. Come to trade?'\n\n"
            "Coins of black iron are piled on a table nearby."
        ),
        items=[items["demon_coin"]],
        npcs=[npcs["demon_smith"]],
        exits={"northeast": "sea3"},
        ambient=lambda s: "The black flames hiss and pop. Each bubble of molten metal sounds like a whispered secret." if not s.has_flag("met_demon") else "The forge still burns, but the demon nods politely as you pass.",
    )

    # ---- NEW ISLAND 8: GOLDEN PILLAR ----
    l["island_golden_pillar"] = Location(
        "island_golden_pillar", "Island of the Golden Pillar",
        "A pillar of solid gold rises from the sea, impossibly tall. A silver fishnet hangs from its apex.",
        detailed_desc=(
            "A PILLAR of solid gold rises from the sea — so tall that its top disappears into the clouds. "
            "It is wider than a house, and polished to a mirror shine.\n\n"
            "Carved into its surface are images of fish, ships, and sea creatures — "
            "the history of the Atlantic, written in gold.\n\n"
            "Near the top — just visible at the cloud line — a SILVER NET hangs from a hook. "
            "Something gleams inside it.\n\n"
            "At the base of the pillar, a tidepool contains a single, perfectly round opening — "
            "a keyhole? Or something else?\n\n"
            "An inscription at the base reads:\n\n"
            "'He who would climb to heaven's gate must first see what the silver net makes great. "
            "The golden pillar holds the sky. The silver net holds the answer. Catch what glitters, but know its weight.'"
        ),
        items=[],
        npcs=[],
        exits={"northeast": "sea3", "east": "sea3"},
        ambient=lambda s: "The golden pillar gleams, reflecting the grey sea and sky. Standing beside it, you feel very small and very mortal." if not s.has_flag("got_golden_fish") else "The golden pillar still gleams, but the silver net hangs empty now.",
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
            "What do you do?\n\n"
            "Type YES to forgive them. Type NO to take your vengeance."
        ),
        npcs=[],
        items=[],
        exits={},
        on_enter=lambda s: (
            "The wind carries the smell of home. Your crew stands behind you, weapons drawn.\n\n"
            "This is the moment your voyage was meant to end. But how?"
            if not s.has_flag("confronted") else None
        ),
    )

    # Register all locations
    LOCATIONS.update(l)


_make_locations()


# ============================================================
# PUZZLE HANDLERS — called from Location lambdas and engine hooks
# ============================================================

def setup_special_events():
    """Configure special interactions that need custom logic.

    These handlers hook into the engine's give/use/fight/sing/joke system.
    They are registered in engine.py and called from there.
    """
    pass


# ---- PUZZLE: Four Fences ----
# The copper fence is the correct choice. Gold = greed, Silver = pride,
# Crystal = fragility, Copper = humility.
# Player types GO COPPER or GO THROUGH COPPER or GO GATE etc.
# We handle this via an on_enter that sets awaiting_choice.

# ---- PUZZLE: Wisdom Salmon ----
# Player needs to catch the salmon. USE NET (from Golden Pillar)
# or USE SPEAKING FEATHER (to distract), or USE SILVER BELL (to hypnotize).

# ---- PUZZLE: Water Horse ----
# Player must not ride the kelpie. Instead, GIVE something or
# USE CROSS to bless it, or just leave.

# ---- PUZZLE: Fiery Pigs ----
# Player must GIVE ASH to the pigs (from the trumpet muffler cloth
# being burned, or from the demon's forge). Or USE WATER.

# ---- PUZZLE: Revolving Castle ----
# Player must enter at the right door at the right time.
# The answer is the Black Door (death/acceptance) - or Blue (sea/sky).
# We'll make it a choice-based puzzle.

# ---- PUZZLE: Giant Trumpet ----
# Player must first take the earplugs, then USE EAPPLUGS on self
# before using the trumpet. Or USE MUFFLER on trumpet.

# ---- PUZZLE: Golden Pillar ----
# Player needs the Silver Net (already there), then USE NET on tidepool
# to catch the golden fish.
