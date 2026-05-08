"""Shared items and NPCs for all levels."""

from ..engine import Item, NPC

items = {}
npcs = {}

def load_shared():
    """Populate all shared items and NPCs."""
    _make_items()

    # ---- PROLOGUE NPCS (interactive at Keep and Beach) ----

    npcs["ailill"] = NPC(
        "ailill", "Ailill Ochair Ága", "A giant of a man with a beard like rusted iron and arms thick as mast timbers. He is laughing — always laughing — with a drinking horn in his fist. His sword, Wolf's Fang, leans against his throne. He is the Wolf of the Arans, and he does not know this is his last night alive.",
        aliases=["ailill", "father", "wolf", "ailill ochair ága", "the wolf"],
        dialogue={
            "greeting": (
                'Ailill looks up and grins. His teeth are white against his beard.\n\n'
                '"Well, well! A visitor! Come, sit, drink! The night is young and so are we — '
                'well, I\'m not young, but I\'m still here, and that\'s what counts!\n\n'
                'You have the look of a storyteller. Or a spy. Or a storyteller who is also a spy. '
                'Either way, you\'re welcome at my table. Pull up a bench!\n\n'
                'The mead is sweet and the company is finer. What brings you to my hall?"'
            ),
            "dead": (
                'Ailill lies still on the cold sand. His eyes are open, staring at the grey sky. '
                'The tide washes over his feet, and his sword — Wolf\'s Fang — is still clasped in his dead hand.\n\n'
                'He does not answer. He cannot. The Wolf of the Arans is gone.'
            ),
            "father": (
                '"My son? Mael Duin? He\'s asleep by the fire. Barely a year old and already '
                'he has the grip of a warrior. He grabbed my finger today and would not let go. '
                'I told his mother: this one will be a fighter.\n\n'
                'I hope he grows up strong. I hope he grows up kind. I hope he grows up to be '
                'a better man than his father. That\'s all any father can wish for."'
            ),
            "war": (
                '"War? War is a young man\'s game, and I am no longer young. But I am still '
                'good at it. The Northern Isles sent a raiding party last month. I sent them back '
                'in pieces. They will think twice before crossing the Wolf again.\n\n'
                'But tonight? Tonight we feast. War can wait until morning."'
            ),
            "wife": (
                '"My wife? She is the best of me. She keeps me grounded, keeps me human. '
                'Without her, I would be just another brute with a sword. With her, I am... '
                'something more.\n\n'
                'She worries. That is her job. My job is to make sure she has nothing to worry about."'
            ),
        }
    )

    npcs["mother"] = NPC(
        "mother", "Your Mother", "A woman with tired eyes and a gentle face. She sits by the cradle, her hand resting on it as if she is afraid to let go. She has not laughed all night. She knows something is wrong.",
        aliases=["mother", "mother", "woman", "your mother", "ailill's wife", "wife"],
        dialogue={
            "greeting": (
                'She looks up at you with eyes that have seen too much.\n\n'
                '"Shh. The baby is sleeping. He is so small, so fragile. I look at him and I see '
                'his father — the same stubborn chin, the same way of furrowing his brow.\n\n'
                'I hope he grows up to be a better man than Ailill. I hope he grows up at all.\n\n'
                'The world is cruel and the sea is crueler. But perhaps... perhaps there is hope for him yet."'
            ),
            "ailill": (
                '"He does not know when to stop. The feasting, the fighting, the laughing. '
                'He lives every day as if it is his last. And one day, it will be.\n\n'
                'I have told him a hundred times: the Northern raiders will come back. They always do. '
                'But he just laughs and says, \"Let them come. I will be waiting.\"\n\n'
                'I fear he will wait for them once too often."'
            ),
            "baby": (
                '"Mael Duin. My son. He has his father\'s strength but — I pray — none of his recklessness. '
                'I look at him and I see a future I will not live to witness. But that is the way of things. '
                'Mothers give birth to children who will bury them. That is the natural order.\n\n'
                'I just hope he remembers me. When I am gone. I hope he knows I loved him."'
            ),
        }
    )

    _make_npcs()


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
        aliases=["earplugs", "wax plugs", "beeswax", "wax earplugs", "plugs"],
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


    # ---- PROLOGUE ITEMS ----
items["childhood_toy"] = Item(
    "childhood_toy", "Carved Wooden Horse",
    "A small wooden horse, carved by your father before you were born. Your foster mother kept it all these years.",
    examine_text="A simple horse, carved from oak. The craftsmanship is rough but loving. One of the legs is slightly shorter than the others, making it rock when you set it down. Your father's hands made this. You can feel it.",
    aliases=["horse", "wooden horse", "toy", "carving"],
)

items["fathers_ring"] = Item(
    "fathers_ring", "Ailill's Signet Ring",
    "A heavy silver ring, worn smooth by years of wear. The crest of the Wolf of the Arans is still visible — a wolf's head, howling at a crescent moon.",
    examine_text="A band of tarnished silver, set with a carnelian stone carved into a wolf's head. The wolf is howling. You wonder if it was howling in victory or grief. The ring fits your thumb perfectly.",
    aliases=["ring", "signet ring", "silver ring", "father's ring"],
)

items["bronze_brooch"] = Item(
    "bronze_brooch", "Bronze Brooch",
    "A beautifully crafted bronze brooch from the Ancient Bird's nest, shaped like a spiral. It must be centuries old.",
    examine_text="A bronze brooch in the shape of an unbroken spiral, the symbol of eternity. The craftsmanship is exquisite — every curve is perfect. It would fetch a good price in any market.",
    aliases=["brooch", "bronze brooch", "spiral"],
)

items["dragon_tooth"] = Item(
    "dragon_tooth", "Dragon's Tooth",
    "A massive tooth from some ancient beast, found in the Bird's nest. It's as long as your forearm and still sharp at the tip.",
    examine_text="A fossilised tooth, black with age. The root is worn smooth, but the tip could still pierce hide. Serrated edges run along one side. Whatever this belonged to, you're glad it's dead.",
    aliases=["tooth", "dragon tooth", "fang"],
)


_make_items()


npcs = {}

def _smith_trade_handler(state, item):
    """Handle trading any item to the smith for the Magic Harpoon."""
    harpoon = items.get("magic_harpoon")
    if not harpoon or state.has_flag("got_harpoon"):
        return (
            f"The smith looks at the {item.name} and grunts. "
            + '"Not bad. But I already made you a weapon. One per customer."'
        )

    state.set_flag("got_harpoon")
    state.score += 3
    state.inventory.append(harpoon)
    return (
        f"The smith takes the {item.name} and turns it in his massive hands."
        + "\n\nHmm. Not bad at all. I can work with this."
        + "\n\nHe tosses it into the forge and works the bellows. "
        + "The ground shakes. Sparks fly. "
        + "After an hour of hammering, he holds up a gleaming MAGIC HARPOON "
        + "- dark iron etched with spirals, humming with power."
        + '\n\n"This harpoon always returns to its thrower. '
        + "Don't lose it. Well, you CAN lose it, but it'll come back."
        + '"\n\n(+3 points. Gained: Magic Harpoon)'
    )

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
            "on_take": {
                # Accept any item as trade payment, give the harpoon
                "__any__": lambda state, item: _smith_trade_handler(state, item)
            }
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

    n["ancient_bird"] = NPC(
        "ancient_bird", "The Ancient Bird", "An enormous old bird perched on a nest of silver twigs and gold. Its eyes are milky with age, but they miss nothing. It shifts with the slow dignity of something that has seen empires rise and fall.",
        aliases=["bird", "ancient bird", "old bird", "elder"],
        dialogue={
            "greeting": (
                'The Ancient Bird fixes you with one milky eye.\n\n'
                '"Mael Duin," it says. Its voice is like old parchment being folded. '
                '"I have been expecting you. Well, not you specifically. I\'ve been expecting someone. '
                'It\'s been a long time since anyone climbed up here. My legs don\'t work like they used to."\n\n'
                'It shifts on its nest, revealing a stash of shiny objects — coins, buttons, '
                'a thimble, a bronze brooch, and what looks like a dragon\'s tooth.\n\n'
                '"Take what you need," it says. "I\'m too old to guard treasure. '
                'I mostly just nap and complain about the weather."'
            ),
            "treasure": (
                '"Take what you want from the nest. Coins, trinkets, an old dragon tooth. '
                'They mean nothing to me. I\'ve had them so long they feel like clutter."'
            ),
            "weather": (
                '"The weather? Terrible. Always terrible. When I was young, the sun was warmer '
                'and the fish were fatter. Now it\'s all mist and cold and young birds who don\'t '
                'know respect."'
            ),
        }
    )

    n["speaking_bird"] = NPC(
        "speaking_bird", "A Chatty Bird", "A small, iridescent bird perched on a rocky ledge, tilting its head at you with obvious curiosity. Its feathers shimmer with every colour of the rainbow.",
        aliases=["bird", "speaking bird", "chatty bird", "red bird"],
        dialogue={
            "greeting": (
                'The bird hops closer and cocks its head.\n\n'
                '"Welcome, hairless one! We don\'t get many visitors. '
                'Most sailors hear us talking and think it\'s the wind playing tricks. '
                'But you came ashore. That takes guts. Or poor judgment. Both, probably!"\n\n'
                'It chirps what sounds like laughter.'
            ),
            "feather": (
                '"Looking for a feather? The old one up top sheds them sometimes. '
                'They\'re magic, you know. Whisper secrets when you hold them to your ear. '
                'I\'d give you one of mine but... I\'m using them."'
            ),
            "salmon": (
                '"Salmon are the philosophers of the sea. They swim upstream for years, '
                'thinking deep thoughts, then get eaten by bears. It\'s a metaphor for something. '
                'I forget what."'
            ),
        }
    )

    n["queen_ant"] = NPC(
        "queen_ant", "The Queen Ant", "A massive ant the size of a house, sitting regally upon a throne of woven branches and golden fruit. Her compound eyes reflect the world in a thousand fragments. She regards you with ancient, patient stillness.",
        aliases=["queen", "queen ant", "ant queen", "giant ant"],
        dialogue={
            "greeting": (
                'The queen ant clicks her mandibles three times. The sound echoes like a gong. '
                'She tilts her head, examining you from every angle with her compound eyes.\n\n'
                'She does not speak — not in words — but you understand her meaning nonetheless: '
                '"You are strange. You are not ant. But you are not enemy either. What brings you to my grove?"\n\n'
                'A worker ant approaches, holding a golden fruit in its jaws. It offers it to you.\n\n'
                'The queen waits. The gift is offered. Whether you take it or not is your choice.'
            ),
            "fruit": (
                'The queen ant gestures with a feeler toward the golden fruit. '
                'It is an offering — a gesture of peace from the colony to the strange hairless ones.',
            ),
        }
    )

    n["beach_mother"] = NPC(
        "beach_mother", "Your Mother", "A woman kneeling in the wet sand, her hands covered in her husband's blood. She does not weep — she is past weeping. She holds a lock of his hair in her hand and stares at the grey sea as if it has stolen everything she loved.",
        aliases=["mother", "woman", "wife", "ailill's wife"],
        dialogue={
            "greeting": (
                'She does not look up at you. Her voice is barely a whisper.\n\n'
                '"He\'s gone. The Wolf is gone. I told him — I told him a hundred times — '
                'the raiders would come back. But he just laughed. He always laughed.\n\n'
                'Now he lies in the sand, and our son will grow up without a father, '
                'and I will grow old alone on this grey shore.\n\n'
                'There is nothing you can say. Nothing anyone can say. '
                'The sea has taken everything."\n\n'
                'She falls silent. The tide continues its slow work.'
            ),
            "ailill": (
                '"He was the best of us. Brave, foolish, kind. He died with a sword in his hand '
                'and a curse on his lips. That was Ailill — always fighting, always laughing, '
                'even at the end."'
            ),
            "baby": (
                '"Mael Duin. My son. He is so small. He will not remember any of this. '
                'Perhaps that is a mercy. Perhaps it is a cruelty. I do not know which."'
            ),
        }
    )

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

    

    # ---- PROLOGUE NPCS ----

    n["foster_mother"] = NPC(
        "foster_mother", "Your Foster Mother", "A woman in her fifties, her face weathered by wind and grief. Her hands are gentle but strong. She has raised you as her own since you were a baby, and she has carried the secret of your father's death like a stone in her chest for twenty years.",
        aliases=["mother", "foster mother", "woman", "foster mother"],
        dialogue={
            "greeting": (
                'Your foster mother looks at you with eyes that have seen too much and loved too deeply.\n\n'
                '"You have the look of your father," she says softly. "More every day. '
                'I see him in the way you stand, the way you laugh, the way you stare at the sea.\n\n'
                'I knew him, you know. Before you were born. Before any of this. '
                'He was the kindest man I ever knew, and the fiercest. '
                'He would sing to the goats. He would fight a dozen men without blinking. '
                'He was not a simple man. He was a storm in human shape.\n\n'
                'And you are his son. Never forget that."'
            ),
            "father": (
                '"Ailill. Your father. He was the Wolf of the Arans. '
                'He led the raids against the Northern Isles. He was feared and loved in equal measure.\n\n'
                'The night he died... I found him on the beach at dawn. The tide was washing his feet. '
                'His sword was still in his hand. He had killed seven of them before they brought him down.\n\n'
                'I never told you because I wanted you to be free. '
                'A man who knows his father was murdered is never free."'
            ),
            "voyage": (
                '"I knew this day would come. From the moment you could walk, you were drawn to the sea. '
                'I used to find you standing on the beach, staring at the horizon, as if you could see something '
                'the rest of us couldn\'t.\n\n'
                'Go. Find them. Do what you must. But come back alive, Mael Duin. Come back alive."'
            ),
            "ring": (
                '"Your father\'s ring. I kept it hidden all these years. '
                'I was going to give it to you on your wedding day. But I think you need it more now.\n\n'
                'He wore it on his thumb. It will fit yours the same way. '
                'It\'s not magic. It won\'t protect you from swords or storms. '
                'But it will remind you that you are not alone. You carry him with you."'
            ),
        }
    )

    n["lorcan"] = NPC(
        "lorcan", "Lorcán the Taunter", "A broad-shouldered warrior with a scar across his cheek and mead on his breath. He is the kind of man who starts fights he can't finish and tells truths he doesn't understand.",
        aliases=["lorcan", "taunter", "warrior", "drunk"],
        dialogue={
            "greeting": (
                'Lorcán sneers at you, swaying slightly.\n\n'
                '"So. The bastard returns. I see you\'ve heard the truth about your daddy. '
                'The great Ailill Ochair Ága. The Wolf of the Arans. '
                'Slain on the beach like a dog while his wife watched.\n\n'
                'What are you going to do about it, boy? Cry? Run to the druid? '
                'Or are you going to do something a real man would do?"'
            ),
            "apology": (
                '"An apology? You want an apology from me?\n\n'
                'Look, I was drunk. I say things when I\'m drunk. '
                'But I didn\'t lie. Everything I said was true. '
                'The truth doesn\'t need an apology.\n\n'
                'But if it makes you feel better... I\'m sorry I said it in front of everyone. '
                'That was cruel. I\'m not a cruel man. Just a drunk one."'
            ),
        }
    )

    n["young_conganchnes"] = NPC(
        "young_conganchnes", "Conganchnes (Young)", "A young warrior with the build of a bear and skin that cannot be cut. He grins at you with the confidence of someone who has never lost a fight and doesn't intend to start now.",
        aliases=["conganchnes", "congan", "young warrior", "champion"],
        dialogue={
            "greeting": (
                'Conganchnes grins and claps you on the shoulder — hard.\n\n'
                '"There you are! I was beginning to think you\'d changed your mind. '
                'Don\'t tell me you\'re having second thoughts. '
                'I\'ve already sharpened my sword three times in anticipation.\n\n'
                'We\'re going to see wonders, you and I. Monsters to fight. Islands to explore. '
                'Treasure to find. And at the end of it all, the men who killed your father.\n\n'
                'I wouldn\'t miss this for anything."'
            ),
            "fight": (
                '"You want to fight? Now? We\'re about to sail across the ocean! '
                'Fine. One round. Don\'t blame me when I knock you on your backside."'
            ),
        }
    )

    n["young_fergus"] = NPC(
        "young_fergus", "Fergus (Young)", "A thin young man with eyes that are always looking at something far away. He is already the best navigator on the islands, and he knows it.",
        aliases=["fergus", "navigator", "young fergus"],
        dialogue={
            "greeting": (
                'Fergus looks up from his star charts.\n\n'
                '"Ah, Captain. I\'ve been calculating our route. '
                'If we sail west-northwest from the harbor, we\'ll hit the Gulf Stream, '
                'which will carry us past the first cluster of islands. '
                'After that... well, the maps stop. There be monsters, as they say.\n\n'
                'But I\'ve been reading the stars, and they say something interesting. '
                'They say this journey will change everything. Every single thing.\n\n'
                'Also that I should have worn a warmer cloak. But it\'s too late for that now."'
            ),
        }
    )

    n["young_diuran"] = NPC(
        "young_diuran", "Diurán (Young)", "A young man with ink-stained fingers and a scroll case perpetually tucked under his arm. He sees poetry in everything, especially danger.",
        aliases=["diuran", "poet", "scribe", "young diuran"],
        dialogue={
            "greeting": (
                'Diurán looks up from his writing, quill poised.\n\n'
                '"Captain! I\'ve already written the first chapter. '
                'I call it "The Wolf\'s Awakening." It\'s about a young hero who discovers his father was '
                'murdered and sets sail across the sea for revenge. It\'s very dramatic.\n\n'
                'I\'m going to make this voyage into the greatest epic ever sung. '
                'Assuming we survive, of course. A tragic ending would sell more copies, '
                'but I\'d prefer a happy one. For friendship. And also because I\'d like to keep living."'
            ),
        }
    )

    n["young_druid"] = NPC(
        "young_druid", "The Druid (Younger)", "The same druid, but years younger. He still moves like an old man, though. Some people are born ancient.",
        aliases=["young druid", "old man", "wise man"],
        dialogue={
            "greeting": (
                'The druid looks at you with knowing eyes.\n\n'
                '"You have questions. Good. Questions are how we grow.\n\n'
                'You want to know about your father. I can see it in your eyes. '
                'But I cannot tell you yet. You are not ready. The truth would break you, '
                'and a broken boy cannot become the man he needs to be.\n\n'
                'When you are ready, I will tell you everything. '
                'Until then, learn to fight. Learn to read the stars. '
                'Learn to be kind when kindness is hard. These will serve you better than any secret."'
            ),
        }
    )
    npcs.update(n)



_make_npcs()

