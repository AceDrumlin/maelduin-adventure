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
            "death": (
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
        },
        visible_if=lambda s: not s.has_flag('witnessed_death'),
    )

    npcs["mother"] = NPC(
        "mother", "Your Mother", "A woman with tired eyes and a gentle face. She sits by the cradle, her hand resting on it as if she is afraid to let go. She has not laughed all night. She knows something is wrong.",
        aliases=["mother", "woman", "your mother", "ailill's wife", "wife"],
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
        },
        visible_if=lambda s: not s.has_flag('witnessed_death'),
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

    # ---- MISSING ISLANDS ITEMS ----

    i["millstone_fragment"] = Item(
        "millstone_fragment", "Millstone Fragment",
        "A heavy fragment of a millstone, broken from the Mill of the Sea. One edge is sharp, the other smooth. It is dense and weighty.",
        examine_text="A chunk of dark granite, curved on one side where it was once part of a great wheel. The grinding surface is still rough and abrasive.",
        aliases=["millstone", "fragment", "stone", "millstone fragment"],
        takeable=True,
    )

    i["fleece_of_change"] = Item(
        "fleece_of_change", "Fleece of Change",
        "A shimmering fleece that shifts between black and white depending on how you look at it. It feels warm and alive, as if it remembers being a sheep.",
        examine_text="The fleece ripples with color - black one moment, white the next. When you hold it still, it settles into a soft, silvery grey. It seems to contain both darkness and light.",
        aliases=["fleece", "sheep fleece", "fleece of change", "wool", "shimmering fleece"],
        takeable=True,
    )

    i["horsehair_bridle"] = Item(
        "horsehair_bridle", "Horsehair Bridle",
        "A bridle woven from the mane of the Stallion King. It thrums with wild energy, eager for a gallop across the waves.",
        examine_text="A bridle of braided white and black horsehair, studded with sea-shells. When you hold it, you feel the urge to ride fast - impossibly fast - across the open sea.",
        aliases=["bridle", "horsehair bridle", "reins", "horse reins"],
        takeable=True,
        use_text="You hold the Horsehair Bridle up to the wind. It thrumms with energy, and for a moment you feel the Stallion King's presence beside you — a herd of giant horses galloping across the waves. The bridle glows warmly, eager to be used on a worthy steed.\n\n(Perhaps you can use it on the Water Horse? Try: USE BRIDLE ON WATER HORSE)"
    )

    i["sunstone"] = Item(
        "sunstone", "Sunstone",
        "A golden crystal that glows with captured sunlight. It illuminates the darkest places and warms the coldest chambers.",
        examine_text="A hexagonal crystal of pale gold, warm to the touch. Light swirls within it like honey, casting a soft, golden glow in every direction. It pulses gently, like a heartbeat made of sunshine.",
        aliases=["sunstone", "crystal", "golden crystal", "sun crystal", "light stone"],
        takeable=True,
    )

    i["golden_horn"] = Item(
        "golden_horn", "Golden Horn",
        "A magnificent horn of pure gold, curved and polished, taken from one of the Sacred Oxen. When blown, it produces a sound that carries across worlds.",
        examine_text="A perfect golden horn, warm and heavy. Etched with spirals and ancient symbols. The mouthpiece is worn smooth from centuries of use by beings older than mankind.",
        aliases=["horn", "golden horn", "ox horn", "war horn"],
        takeable=True,
        use_text="You raise the Golden Horn to your lips and blow. A deep, resonant note rolls across the sea - a sound that seems to answer a question you did not know you were asking. Somewhere, something ancient stirs in response.",
    )

    i["water_of_vision"] = Item(
        "water_of_vision", "Water of Vision",
        "A vial of shimmering water from the Well of Sight. Drink to see what is hidden.",
        examine_text="A small glass vial filled with water that glows with an inner, silvery light. When you hold it up, you can see reflections of things that are not in front of you - doorways, paths, secrets.",
        aliases=["water", "vision water", "well water", "water of vision", "vial"],
        takeable=True,
        use_text="You drink the Water of Vision. For a moment, the world goes silver. Veils peel away from reality - you see the hidden paths between islands, the true nature of the Revolving Castle doors, and the face of your father, smiling at you from across the sea. The vision fades, but you remember everything.",
    )

    i["ever_grinding_grain"] = Item(
        "ever_grinding_grain", "Ever-Grinding Grain",
        "A handful of golden grain from the Mill of the Sea. It multiplies when you are not looking - one grain becomes two, two become four, four become eight.",
        examine_text="A handful of golden wheat grains that seem to multiply while you watch. The pile grows slowly, inexorably, like time itself. You will never go hungry again.",
        aliases=["grain", "golden grain", "ever grinding grain", "wheat", "magic grain"],
        takeable=True,
    )

    # ---- MISSING ISLANDS 2 ITEMS (Level 06) ----

    i["fish_tooth"] = Item(
        "fish_tooth", "Fish Tooth",
        "A serrated tooth the size of your hand, still warm from the belly of the Great Fish.",
        examine_text="A massive, serrated tooth, curved like a dagger. It is still warm and slightly slick with digestive fluids. The edges are razor-sharp.",
        aliases=["tooth", "fish tooth", "great fish tooth", "serrated tooth"],
        takeable=True,
    )

    i["fountain_water"] = Item(
        "fountain_water", "Fountain Water",
        "Milk-white water from the Fountain Island. It shimmers with inner light.",
        examine_text="A small flask of milky, luminescent water. It swirls gently with its own inner light, and the smell is sweet and honeyed.",
        aliases=["water", "fountain water", "milk water", "healing water"],
        takeable=True,
        use_text="You drink the Fountain Water. A warm glow spreads through your body. You feel whole, rested, and healed.",
    )

    i["silent_bell"] = Item(
        "silent_bell", "Silent Bell",
        "An iron bell that makes no sound. When you ring it, everything around you stills.",
        examine_text="A cold iron bell, perfectly still. When you shake it, you feel the clapper move, but no sound emerges. The silence around it seems to deepen.",
        aliases=["bell", "silent bell", "iron bell", "mute bell"],
        takeable=True,
    )

    i["wind_of_return"] = Item(
        "wind_of_return", "Wind of Return",
        "A sealed bottle holding a favourable wind. The guardian said it would take me home.",
        examine_text="A small glass bottle sealed with wax. Inside, a tiny whirlwind spins endlessly, catching the light. When you hold it, you feel the pull of home - a direction, a longing, a certainty.",
        aliases=["wind", "bottle", "wind bottle", "wind of return", "favourable wind"],
        takeable=True,
        use_text="You unseal the Wind of Return. A warm, steady wind fills your sails, carrying you homeward with unerring certainty.",
    )
    # ---- FINAL ISLANDS ITEMS (Level 07) ----
    i["kelpie_scale"] = Item(
        "kelpie_scale", "Kelpie Scale",
        "An iridescent scale from the Water Horse of the deep. It pulses with a warm, gentle light and smells faintly of salt and secrets.",
        examine_text="A single scale, shimmering with all the colours of a sunken rainbow. It is warm to the touch, as if still alive. When you hold it to your ear, you can hear the distant sound of waves.",
        aliases=["scale", "kelpie scale", "water horse scale", "iridescent scale"],
        takeable=True,
    )

    # ---- FINAL ISLANDS ITEMS (Level 07) ----
    i["giants_club"] = Item(
        "giants_club", "Giant's Club",
        "A crude club of oak and stone, stolen from a dead giant. It is heavy enough to crush a skull with one swing.",
        examine_text="A massive club of dark oak, bound with leather and studded with sharp stones. The head is stained dark — blood, long dried. It fits your grip perfectly, as if made for you.",
        aliases=["club", "giant club", "giant's club", "oak club"],
        takeable=True,
    )

    i["treasure_gold"] = Item(
        "treasure_gold", "Ancient Gold",
        "A hoard of golden coins, enough to buy a kingdom. They gleam with ancient, stolen light.",
        examine_text="A small chest overflowing with ancient gold coins. Each one bears the face of a king you have never heard of — a king whose kingdom is now seaweed and memory. The gold is warm to the touch.",
        aliases=["gold", "treasure", "coins", "ancient gold", "gold coins", "chest"],
        takeable=True,
    )

    i["silver_torc"] = Item(
        "silver_torc", "Silver Torc",
        "A beautiful silver neck-ring, gleaming with ancient craftsmanship. It feels warm against your skin.",
        examine_text="A delicate torc of woven silver wire, ending in two ornate knobs shaped like wolf heads. The metal is impossibly smooth — polished by centuries of wear. It hums faintly with old magic.",
        aliases=["torc", "silver torc", "neck-ring", "neck ring", "silver ring"],
        takeable=True,
    )

    i["lions_claw"] = Item(
        "lions_claw", "Lion's Claw",
        "A razor-sharp claw, still warm from the beast. It can be used as a tool or a weapon.",
        examine_text="A single claw, curved like a scimitar, still warm and slightly wet at the base. The keratin gleams like amber. It is sharp enough to cut rope, leather, or flesh with equal ease.",
        aliases=["claw", "lion claw", "lion's claw", "claw dagger"],
        takeable=True,
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
            "greeting_if_learned_truth": (
                "The druid nods slowly, a hint of a smile on his ancient face.\n\n"
                "\"So. You know. The truth sits heavy in your chest, doesn't it? "
                "Good. That means you are ready.\n\n"
                "The magic thread will guide you. The sea will test you. "
                "And when you return, you will not be the man who left.\n\n"
                "Now go. The tide waits for no man, not even one with vengeance in his heart.\""
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
            "greeting_if_cat_pacified": (
                "The enormous cat is sprawled across its golden throne, purring like a dozen bees in a barrel.\n\n"
                "\"Ah. The milk-bringer. You may approach. I have deemed you... acceptable.\n\n"
                "You may pass through my island whenever you wish. Consider yourself one of the few humans "
                "I don't actively despise. Don't let it go to your head.\"\n\n"
                "It closes its eyes and resumes purring."
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
            "greeting_if_resisted_queen": (
                'The Queen watches you from her throne, her smile cold and precise.\n\n'
                '\"You\'re back. I didn\'t think you would be. Most men who leave do not return — '
                'they cannot bear to see what they have refused.\n\n'
                'But you are not most men, are you, Mael Duin? You have the Wolf\'s blood in you. '
                'Stubborn. Foolish. Brave.\n\n'
                'I respect you for it. But do not mistake respect for warmth. '
                'My island is no longer open to you. Leave before I change my mind.\"'
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
                '\"You have traveled far, Mael Duin. And yet you have not traveled at all. '
                'The sea you cross is the sea within you — stormy, deep, full of monsters you have yet to name.\n\n'
                "Sit with me. The otter will share his fish. And I will tell you what the waves have been whispering.\""
            ),
            "greeting_if_otter_pelt_returned": (
                'The hermit is sitting on his rock, the otter pelt wrapped around his shoulders. '
                'He looks warmer now. More at peace.\n\n'
                '\"Mael Duin. You returned my companion\'s pelt. I cannot thank you enough.\n\n'
                "It\'s funny — I thought the otter was gone forever. "
                "But he never really left. He was just waiting to come home in a different form.\n\n"
                'You carry the same burden I carried — the weight of a father lost. '
                "But you carry it forward. That takes strength.\""
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
                '\"HO, LITTLE MAN! You\'ve come to the forge at the edge of the world! '
                "Most people sail right past — they hear the hammering and think it's thunder. "
                "But you came closer. That takes guts. Or stupidity. Both, probably.\"\n\n"
                "He laughs, and the ground shakes."
            ),
            "greeting_if_got_harpoon": (
                'The smith looks up from his work and grins, his face lit by the glow of the forge.\n\n'
                '\"Back again, little man? I hope you\'re not looking for another harpoon — '
                'one masterpiece per customer is my rule.\n\n'
                'But if you\'ve got something shiny to trade, I\'m always listening. '
                'A smith\'s work is never done.\"'
            ),
            "greeting_if_got_harpoon": (
                'The smith looks up from his work and grins, his face lit by the glow of the forge.\n\n'
                '\"Back again, little man? I hope you\'re not looking for another harpoon — '
                'one masterpiece per customer is my rule.\n\n'
                'But if you\'ve got something shiny to trade, I\'m always listening. '
                'A smith\'s work is never done.\"'
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
            "greeting_if_king_pacified": (
                'The Laughing King wipes a tear from his eye and lets out a long, contented sigh.\n\n'
                '"Ahhh. That was a good laugh. The BEST laugh.\n\n'
                'He smiles a genuine, peaceful smile.\n\n'
                '"You know, I\'d forgotten what silence sounds like. It\'s... nice. '
                'Still funny, though. Everything is still funny. Just... quieter."\n\n'
                "He hums contentedly, tapping his fingers on his one-legged stool."
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
        },
        visible_if=lambda s: s.has_flag('witnessed_death'),
    )

    n["skull"] = NPC(
        "skull", "The Talking Skull", "A human skull impaled on a thornbush. Its jaw clatters as it speaks, and its empty eye sockets somehow convey a look of profound boredom.",
        aliases=["skull", "talking skull", "head", "jaw"],
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
            "father": (
                'The skull\'s eye sockets seem to deepen as it speaks.\n\n'
                '"Your father\'s murderer is closer than you think. '
                'He drinks and laughs in a castle that turns like the world — '
                'the Revolving Castle. He is a one-eyed man named Garbh, '
                'and he carries the scar of your father\'s last blow on his face.\n\n'
                'I see him in the fragments of memory the wind brings me. '
                'He does not laugh with joy. He laughs to forget.\n\n'
                'Seek him if you must. But know this: the dead do not thank the living for revenge."\n\n'
                'The skull falls silent, its words hanging in the air like smoke.'
            ),
            "revenge": (
                'The skull rattles, almost laughing.\n\n'
                '"Vengeance is a cup that empties the drinker. The hermit knows this. '
                'The druid knows this. Even this bush knows this, and it\'s a bush.\n\n'
                'You have sailed across the edge of the world, Mael Duin. '
                'You have seen wonders that no other Irishman has seen. '
                'And still you carry the same stone in your heart that you carried when you left.\n\n'
                'Kill Garbh, and the blood feud lives on. Forgive him, and the feud dies with you.\n\n'
                'The choice is yours. But make it with open eyes, not a closed fist."\n\n'
                'The skull\'s teeth chatter once, sharply, as if emphasizing the point.'
            ),
            "home": (
                'The skull\'s voice softens, becoming almost gentle.\n\n'
                '"You will return when the wind forgives you. Not before.\n\n'
                'Home is not a place, Mael Duin. It is a moment. A feeling. '
                'The smell of turf smoke. The sound of your foster mother\'s voice. '
                'The weight of your father\'s ring on your thumb.\n\n'
                'You carry home with you. You always have. '
                'You will find it again when you stop looking for it.\n\n'
                'The sea gives back what it takes, but only when the taking is done."\n\n'
                'A wind rustles the bush, and for a moment the skull\'s jaw hangs slack, as if exhausted by the effort of wisdom.'
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
                '"A mortal. How... bold. Most sailors see the smoke and turn back. "\n'
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

    n["black_pig"] = NPC(
        "black_pig", "The Black Pig", "A massive black boar the size of a cow, with tusks like daggers and eyes like burning coals. It guards the golden apple tree with unwavering vigilance. Drool — liquid gold — pools beneath its snout.",
        aliases=["pig", "black pig", "boar", "black boar"],
        dialogue={
            "greeting": (
                "The black pig snorts and stamps a massive hoof, making the ground tremble.\n\n"
                "\"GRUNFF. You are not welcome here, little man. This tree is mine. "
                "These apples are mine. This island is mine. Everything you see is mine.\"\n\n"
                "It lowers its tusks and glares at you. The message is clear: come closer and get gored."
            ),
            "apple": (
                "\"The golden apples? MINE. Every single one. I've been guarding this tree "
                "since before your grandfather's grandfather was born. You think I'm going "
                "to let some scrawny sailor waltz in and take one? GRUNFF. Think again.\""
            ),
            "fight": (
                "\"You want to fight? HA! I've fought wolves, bears, and a dragon once. "
                "The dragon ran away crying. I ate its lunch. You don't stand a chance, "
                "but I'd be happy to add your bones to my collection.\"\n\n"
                "It snorts aggressively and scrapes the ground with its hooves."
            ),
            "food": (
                "The pig's ears perk up slightly at the word 'food'.\n\n"
                "\"Food? What kind of food? I like apples. Golden ones. "
                "If you have something edible... I MIGHT listen. MIGHT. "
                "No promises. I'm a pig of my word. Which means I change my mind a lot.\""
            ),
        },
        visible_if=lambda s: not s.has_flag('pig_pacified'),
    )

    n["serpent"] = NPC(
        "serpent", "The Great Serpent", "An enormous serpent that encircles the entire island, its body forming a continuous ring. Its scales are the size of shields, shimmering in shades of purple and green. Its head is large enough to swallow a boat whole.",
        aliases=["serpent", "snake", "great serpent", "dragon"],
        dialogue={
            "greeting": (
                "The great serpent raises its head, towering above you. Its forked tongue flickers, tasting the air. Its eyes narrow to slits.\n\n"
                "\"You enter my domain, little one. Few who come here leave again. "
                "The herb you seek is mine to guard, and I do not part with it willingly. "
                "State your purpose, or be gone before I lose my patience.\""
            ),
            "herb": (
                "\"The antidote herb? It grows here, in the center of my ring. "
                "It is the only thing on this island I cannot digest — my one weakness. "
                "Do you think I would simply let you take it? I guard it because it guards the world from me.\""
            ),
            "mercy": (
                "The serpent's head lowers slightly. Its voice softens.\n\n"
                "\"Mercy... an interesting word from a creature who came here to take what is mine. "
                "But I am not unreasonable. I have been alone for a long time. "
                "Perhaps there is a way we can both leave this island satisfied. "
                "Show me something I have not seen before, and I may be persuaded.\""
            ),
            "poison": (
                "\"My venom is the deadliest in all the seas. One drop can kill a whale. "
                "Two drops can kill a god. Three drops... well, I've never tried three drops. "
                "The island would probably dissolve. The herb you seek is the only antidote. "
                "Funny, isn't it? The cure grows beside the poison.\""
            ),
        },
        visible_if=lambda s: not s.has_flag('serpent_calmed'),
    )

    # ---- MISSING ISLANDS NPCS ----

    n["mill_guardian"] = NPC(
        "mill_guardian", "The Mill Guardian",
        "An old, stooped man with flour-dusted skin and ears like cauliflowers — half-deaf from decades of grinding noise. He shuffles in circles around the mill, muttering to himself in a repetitive, grinding cadence.",
        aliases=["guardian", "old man", "mill keeper", "miller", "mill guardian"],
        dialogue={
            "greeting": (
                "The old man does not seem to notice you at first. He keeps shuffling, grinding, grinding. When he finally looks up, his eyes are pale and milky.\n\n"
                "Grind... grind... grind... The sea must be ground. The sea is too full. Too much water. Too many ships. The mill grinds them all down, down, down into foam.\n\n"
                "He taps his ear. 'Speak up, lad. These old ears have heard nothing but stone-on-stone for sixty years. What was that? Speak up!'"
            ),
            "mill": (
                "The mill? Oh, it grinds the sea. Always has. Always will. Salt and stone, stone and salt. That is all there is. That is all there ever was. Grind... grind... grind...\n\n"
                "He pauses. 'Sometimes I dream of silence. But the mill does not dream. The mill only grinds.'"
            ),
            "stop": (
                "Stop the mill? STOP THE MILL?!\n\n"
                "He cackles, a dry wheezing sound. 'If you could stop it, boy, you would be the first in a thousand years. The gears are older than Ireland. The stones were cut from the bones of the world. You cannot stop it. You can only... feed it.'"
            ),
            "gears": (
                "Gears within gears, lad. Great wheels of bronze and iron, turning since before your grandfather's grandfather was a gleam in his father's eye. They catch the sea and crush it. You can hear them groaning if you press your ear to the stone."
            ),
        }
    )

    n["ghostly_shepherd"] = NPC(
        "ghostly_shepherd", "The Ghostly Shepherd",
        "A translucent figure in a tattered wool cloak, leaning on a crook. He seems to exist in two places at once — solid one moment, mist the next. His eyes are the color of twilight — neither black nor white, but something in between.",
        aliases=["shepherd", "ghost", "ghostly shepherd", "old shepherd", "phantom"],
        dialogue={
            "greeting": (
                "The Ghostly Shepherd turns to face you, and for a moment you see the sky through his chest. He speaks in a voice like wind through dry grass.\n\n"
                "'Welcome, traveler. You have come to the fields of change, where black becomes white and white becomes black, and nothing stays as it was.\n\n"
                "My sheep know the secret. They cross between the fields and are transformed. They are neither black nor white when they walk the middle path — they are both. They are the space between.'\n\n"
                "He smiles, and his smile is grey."
            ),
            "riddle": (
                "'The riddle is simple, traveler. I am neither black nor white, yet I contain both. Walk with me, and you shall pass. What am I?'"
            ),
            "answer": (
                "'The shadow. The twilight. The place between. Yes, you understand. You may cross the fields of change unchanged. Go with my blessing.'"
            ),
            "sheep": (
                "'The sheep are not sheep, traveler. They are souls — caught between one life and the next. When they cross the black field, they forget. When they cross the white field, they remember. They spend eternity forgetting and remembering, and that is their penance.'"
            ),
        }
    )

    n["stallion_king"] = NPC(
        "stallion_king", "The Stallion King",
        "A magnificent white stallion, larger than any horse you have ever seen, with a mane that flows like sea-foam and eyes that burn with wild intelligence. He stands proudly on the shore, hooves planted as if he owns the island and everything beyond it.",
        aliases=["stallion", "horse", "stallion king", "white stallion", "king of horses"],
        dialogue={
            "greeting": (
                "The Stallion King snorts and stamps the ground. The earth trembles.\n\n"
                "He does not speak — not in words you can understand — but his meaning is clear: You are not welcome here, little two-legs. These are MY pastures. MY mares. MY island. Turn back before I teach you the meaning of speed."
            ),
            "calm": (
                "The horse's ears pivot forward. Its stance softens, just slightly. It regards you with something like curiosity now — a predator sizing up an unusually interesting piece of prey."
            ),
        }
    )

    n["little_cat"] = NPC(
        "little_cat", "The Little Cat",
        "A tiny, scruffy kitten, no larger than your fist, with fur the color of rust and eyes like twin emeralds. It purrs constantly, a sound like a tiny engine. It is utterly unafraid of you.",
        aliases=["cat", "kitten", "little cat", "small cat", "kitty", "flaming cat"],
        dialogue={
            "greeting": (
                "The little cat looks up at you, blinks slowly, and lets out a tiny 'mew.' It rubs against your ankle, leaving a trail of warm fur. Its purring intensifies.\n\n"
                "There is something ancient in those green eyes — something that knows more than it should. But for now, it just wants to be petted."
            ),
            "pet": (
                "You reach down and scratch behind its ears. The cat leans into your hand, purring so hard it vibrates. It looks up at you with something like gratitude.\n\n"
                "Then it bites your finger — gently — and darts away, looking back as if to say: 'That's enough of that. Now give me what I really want.'"
            ),
            "tribute": (
                "The cat's ears perk up. Its tail twitches. 'Mew?' it says, with obvious interest. It looks at you expectantly, then glances at a small alcove behind it where a golden glow emanates from a crystal."
            ),
        }
    )

    n["sacred_oxen"] = NPC(
        "sacred_oxen", "The Sacred Oxen",
        "Two magnificent white oxen with horns of pure gold that gleam even in the dimmest light. They stand motionless as statues, their breath forming clouds in the cool air. Their eyes are deep, dark pools — ancient, patient, knowing.",
        aliases=["oxen", "ox", "sacred oxen", "white oxen", "golden-horned oxen", "bulls", "bull"],
        dialogue={
            "greeting": (
                "The golden-horned oxen turn their massive heads to regard you. One of them lowss — a sound so deep it vibrates in your bones. They do not seem hostile, but they do not seem welcoming either. They simply... observe.\n\n"
                "The larger of the two takes a step forward and lowers its head, presenting its golden horn as if offering it. Or challenging you to take it."
            ),
            "horn": (
                "The ox's golden horn gleams in the grey light. It is magnificent — a spiral of pure gold, warm and alive. The ox stands still, waiting. It seems to be offering a choice."
            ),
            "peace": (
                "The larger ox lowers its head and makes a sound like a contented sigh. The smaller one nuzzles its flank. They seem to be saying: 'We have been here a long time. We do not wish for violence. Take what you need, but take no more.'"
            ),
        }
    )

    

    # ---- PROLOGUE NPCS ----

    n["foster_mother"] = NPC(
        "foster_mother", "Your Foster Mother", "A woman in her fifties, her face weathered by wind and grief. Her hands are gentle but strong. She has raised you as her own since you were a baby, and she has carried the secret of your father's death like a stone in her chest for twenty years.",
        aliases=["mother", "foster mother", "woman"],
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
            "greeting_if_training_seen": (
                'Your foster mother watches you with proud, sad eyes.\n\n'
                '\"Look at you. A warrior now. I remember when you were so small you fit in the crook of my arm.\n\n'
                'She steps closer and adjusts your collar, a gesture from childhood.\n\n'
                '\"Your father\'s ring. I kept it all these years. '
                'He would want you to have it. You have his strength, Mael Duin.\"'
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
            "greeting_if_taunting_seen": (
                'Lorc\xe1n looks up as you approach, his face flushing. '
                'He does not meet your eyes.\n\n'
                '\"Look... about what I said. I was drunk. That\'s not an excuse.'
                '\n\nHe shifts uncomfortably.\n\n'
                '\"Your father was a great man. If you sail after those raiders, '
                'I hope you find them. And I hope you come back."'
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
            "recruit": (
                'Conganchnes slaps you on the back, nearly knocking the wind out of you.\n\n'
                '"Join your crew? I thought you\'d never ask! '
                'I\'ve been sharpening my sword for exactly this. '
                'Lead on, Captain — I\'ll follow you to the ends of the earth. '
                'And the ends of anyone who gets in our way."\n\n'
                '(Type YES to welcome Conganchnes into your crew.)'
            ),
        },
        visible_if=lambda s: not s.has_flag('recruited_young_conganchnes'),
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
            "recruit": (
                'Fergus folds his star charts with careful precision.\n\n'
                '"Join your crew? I\'ve already charted the course. '
                'The stars have been telling me for years that I\'d sail with you one day. '
                'I just didn\'t know when you\'d finally ask.\n\n'
                'I can navigate us through any storm, read any sky, '
                'and find our way home when all seems lost. '
                'You need me, Captain. And I... I need this voyage."\n\n'
                '(Type YES to welcome Fergus into your crew.)'
            ),
        },
        visible_if=lambda s: not s.has_flag('recruited_young_fergus'),
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
            "recruit": (
                'Diurán sets down his quill and smiles.\n\n'
                '"Join your crew? Captain, I\'ve been writing this story in my head '
                'since the day we met. Every chapter, every verse, every song — '
                'they all lead to this moment.\n\n'
                'I will chronicle every island, every monster, every miracle. '
                'When we return, the world will know the name Mael Duin. '
                'And they\'ll know it because I wrote it down."\n\n'
                '(Type YES to welcome Diurán into your crew.)'
            ),
        },
        visible_if=lambda s: not s.has_flag('recruited_young_diuran'),
    )

    n["young_druid"] = NPC(
        "young_druid", "The Druid (Younger)", "The same druid, but years younger. He still moves like an old man, though. Some people are born ancient.",
        aliases=["druid", "young druid", "young"],
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

    # ---- REVOLVING CASTLE NPCS ----

    n["garbh"] = NPC(
        "garbh", "Garbh the Raider",
        "A one-eyed warrior with a face carved by a lifetime of violence. A long, jagged scar runs from his forehead across his missing eye and down to his jaw \u2014 the last gift your father gave him. He sits on a stone bench in the red-lit chamber, a drinking horn in his hand. When he sees you, he does not reach for his sword. He simply waits.",
        aliases=["garbh", "garbh the raider", "one-eyed man", "one-eyed", "raider", "murderer"],
        dialogue={
            "greeting": (
                'Garbh looks up from his drinking horn. His one good eye fixes you with a gaze that is neither hostile nor kind \u2014 just... tired.\n\n'
                '"So. The Wolf\'s cub comes to the castle that turns. I\'ve been expecting you."\n\n'
                'He takes a long drink and sets the horn down. The scar across his face gleams in the red light.\n\n'
                '"I knew you would come, sooner or later. The sea always brings what it owes."'
            ),
            "father": (
                'Garbh\'s face hardens. He touches the scar on his face.\n\n'
                '"Ailill. Your father. The Wolf of the Arans."\n\n'
                'He pauses, staring at the red-lit wall as if seeing something far away.\n\n'
                '"It was a blood feud, not a murder. His raiders had killed my brother \u2014 burned his village, took his head as a trophy. I did what any man would do. I came for blood."\n\n'
                '"We met on the strand at dawn. He was the finest fighter I ever faced. He took my eye \u2014 this scar is his signature, his last message to the world."\n\n'
                '"But I was faster that morning. One thrust under the arm, where the mail gapes. He fell looking me in the eye, and he was... smiling. Laughing, even. That\'s the worst part. He didn\'t hate me. He respected me."\n\n'
                'Garbh shakes his head slowly.\n\n'
                '"It was not personal, Mael Duin. It was the way of things. Your father knew it. That\'s why he could laugh."'
            ),
            "revenge": (
                'Garbh meets your gaze steadily.\n\n'
                '"Kill me and you become me. Another man in a long line of dead men, passing the sword from hand to hand."\n\n'
                '"Your father\'s blood is on my hands. My brother\'s blood is on his. Where does it end?"\n\n'
                'He leans forward, his voice dropping.\n\n'
                '"If you kill me, my sons will come for you. And if they fail, their sons will come. And your sons will kill them, and their sons will come for your grandsons. It never stops \u2014 unless someone decides it stops here."\n\n'
                '"The question is not whether you can kill me. The question is whether you should."'
            ),
            "forgiveness": (
                'Garbh\'s shoulders sag slightly. His voice softens.\n\n'
                '"You are a better man than your father. And he was a good man."\n\n'
                'He looks away, his one eye glistening.\n\n'
                '"I have lived with what I did every day. I see his face in my dreams \u2014 that laughing, impossible face. He haunts me, Mael Duin. Not because I regret it, but because he would have forgiven me if our positions were reversed. And I knew that even as I struck."\n\n'
                '"If you can forgive me... then maybe the wolf can rest. Maybe we both can."\n\n'
                'He extends his hand, palm open. No weapon. Just the hand of a tired, old warrior waiting for judgment.'
            ),
        }
    )

    # ---- MISSING ISLANDS 2 NPCS (Level 06) ----

    n["silence_guardian"] = NPC(
        "silence_guardian", "The Guardian of Silence",
        "A tall, pale figure draped in flowing grey robes. Its face is smooth and featureless — no eyes, no mouth, no nose. When it speaks, the words do not come from its face, but from the air around it, as if the silence itself is parting to let sound through.",
        aliases=["guardian", "silence guardian", "pale figure", "goddess", "grey figure", "guardian of silence"],
        dialogue={
            "greeting": (
                "The grey figure does not move. It does not breathe. But the silence around it thickens, becomes heavier, like a blanket pressing down on your ears.\n\n"
                "When it speaks, the words are cold and distant, as if coming from the bottom of a deep well:\n\n"
                "'You have entered the domain of silence. Here, sound is forbidden. Music is forbidden. Laughter is forbidden. The world has enough noise. In my valley, there is only peace. Only stillness. Only silence.'\n\n"
                "It pauses, and the silence becomes so complete you can hear your own blood moving.\n\n"
                "'You may stay. But you must not break the silence. If you sing or laugh or speak above a whisper... there will be a price.'"
            ),
            "anger": (
                "The Guardian of Silence turns its blank face toward you. The temperature drops.\n\n"
                "'YOU HAVE BROKEN THE SILENCE. Sound is a wound upon the world, and you have opened a wound in my valley. You must pay tribute — give me something precious — and the silence will be restored.'\n\n"
                "Its empty face waits. If you have something to offer, GIVE it to the guardian."
            ),
            "peace": (
                "The Guardian of Silence bows its head slightly — a gesture of respect.\n\n"
                "'You have kept the silence. You have walked softly in my valley. For this, you may take the Silent Bell. It will serve you well, for silence is the oldest magic — older than speech, older than song, older than the sea itself.'\n\n"
                "It gestures toward the grove where the bell hangs."
            ),
            "tribute": (
                "'Give me something precious. Something that holds sound — a memory of music, a word of power, a song you have forgotten. The silence must be restored.'"
            ),
        }
    )

    n["guardian_of_peace"] = NPC(
        "guardian_of_peace", "The Guardian of Peace",
        "A luminous figure in flowing white robes, surrounded by a soft golden light. Its face is kind and infinitely gentle, radiating a warmth that feels like coming home after a long journey. Its eyes hold the compassionate patience of something that has watched the ages turn.",
        aliases=["guardian", "angel", "luminous figure", "being", "spirit", "guardian of peace", "peace"],
        dialogue={
            "greeting": (
                "The Guardian of Peace opens its arms, and a wave of warmth washes over you.\n\n"
                "'Welcome, Mael Duin. Welcome to the Land of Promise. You have crossed the edges of the known world, braved monsters and wonders, and now you stand at the threshold of peace itself.\n\n"
                "'Here there is no pain, no sorrow, no hunger, no death. The rivers run with wine and honey. The trees bear fruit of pure gold. The air is warm and gentle. Stay with us forever. All you have to do is say yes.'\n\n"
                "Its smile is radiant. The offer is sincere.\n\n"
                "(Type YES to stay forever. Type NO to refuse and receive the Wind of Return.)"
            ),
            "stay": (
                "'Stay. Rest. Be at peace. You have earned this. There is nothing waiting for you back there — no revenge worth taking, no love worth leaving. Stay in the land where all is well.'\n\n"
                "The guardian's voice is hypnotic, gentle. The land behind it shimmers with impossible beauty."
            ),
            "leave": (
                "The Guardian of Peace nods slowly, its expression unchanged — still warm, still kind.\n\n"
                "'I understand. The world beyond calls to you. Your story is not yet finished. Your home is waiting.\n\n"
                "'Take this Wind of Return — a bottle holding a favourable wind. When you are ready, use it to sail home. It will carry you across the sea with unerring certainty, to the shore where you belong.'\n\n"
                "It places a sealed glass bottle in your hands. Inside, a tiny whirlwind spins endlessly.\n\n"
                "'Go with my blessing, Mael Duin. And remember: you carry home with you now.'"
            ),
            "home": (
                "'Your home is waiting. But you carry it with you now — in your heart, in your memories, in the weight of your father's ring on your thumb. The Promised Land is not a place. It is a feeling. And you have felt it all along.'"
            ),
        }
    )

    # ---- FINAL ISLANDS NPCS (Level 07) ----

    n["giant"] = NPC(
        "giant", "The Giant",
        "A monstrous giant perched on a high cliff, his skin the colour of lichen-covered stone. He is easily twenty feet tall, with arms like tree trunks and a face twisted by crude malice. Beside him, a pile of fist-sized stones waits to be hurled at passing ships.",
        aliases=["giant", "ogre", "stone thrower", "cliff giant"],
        dialogue={
            "greeting": (
                "The giant roars as he spots your approach! He hefts a stone the size of a man's head "
                "and hurls it at your curragh with terrifying accuracy. The missile crashes into the hull, "
                "splintering wood.\n\n"
                "One of your crew — a young man from the west — is struck by a flying splinter and falls, "
                "clutching his chest. He does not rise again.\n\n"
                "You have lost a crew member. The giant bellows with laughter and reaches for another stone.\n\n"
                "You must act quickly: FIGHT the giant with the Magic Harpoon, TALK to him with the Speaking Feather, "
                "or GIVE him food (Everlasting Fruit, Crew Provisions) to distract him."
            ),
            "fight": (
                "You hurl the Magic Harpoon at the giant. It strikes him square in the chest — "
                "a blow that would kill any mortal man. The giant bellows in pain, tearing at the harpoon, "
                "but the enchanted weapon returns to your hand before he can pull it free.\n\n"
                "He stumbles backward, clutching his wound, and topples from the cliff. The ground shakes "
                "as his body crashes onto the rocks below. The waves wash over him, and he is still.\n\n"
                "At the base of the cliff, you find his GIANT'S CLUB — a crude weapon of oak and stone. "
                "It is heavy, but you lift it. It may serve you yet.\n\n"
                "(+3 points. Gained: Giant's Club)"
            ),
            "talk": (
                "You hold up the Speaking Feather and address the giant in his own tongue.\n\n"
                "The giant halts mid-throw, his brow furrowing with confusion. "
                "'You speak the Old Tongue?' he rumbles. 'No man has spoken it in a hundred years.'\n\n"
                "You negotiate. The giant was angry because the last ships that passed did not respect his territory. "
                "You promise to leave his cliff alone and never return. He grunts, mollified.\n\n"
                "'You are a strange little man,' he says. 'But you have honour. Take this — it fell from my tooth "
                "last winter. I have no use for it.'\n\n"
                "He tosses you a GIANT'S TOOTH — a massive, yellowed fang that could serve as a dagger or a trophy.\n\n"
                "(+3 points. Gained: Giant's Tooth)"
            ),
            "give": (
                "You offer food to the giant. He squints at it, sniffs suspiciously, "
                "then snatches it from your hand and stuffs it into his mouth.\n\n"
                "'Hmph,' he grunts, chewing noisily. 'Not bad. You may pass, little man. "
                "But tell your friends to bring better food next time.'\n\n"
                "The giant settles back onto his cliff, patting his belly with satisfaction. "
                "He does not throw any more stones.\n\n"
                "(+1 point. No crew lost.)"
            ),
            "father": (
                "'Your father? Never met him. I crush everyone who sails past. "
                "I don't stop to ask their family history.'\n\n"
                "He throws another stone for emphasis."
            ),
        },
        visible_if=lambda s: not (s.has_flag('giant_defeated') or s.has_flag('giant_mollified')),
    )

    n["treasure_serpent"] = NPC(
        "treasure_serpent", "The Treasure Serpent",
        "A massive serpent coiled before the mouth of a dark cave. Its scales shimmer with a deep, oily green, and its eyes — vertical slits of gold — follow your every movement. It is the size of a small ship, and its body completely blocks the entrance to the cave.",
        aliases=["serpent", "dragon", "snake", "guardian", "treasure serpent"],
        dialogue={
            "greeting": (
                "The serpent hisses — a sound like steam escaping from a fissure. It raises its wedge-shaped head, "
                "tasting the air with a forked tongue as long as your arm.\n\n"
                "'Mine,' it says. The word is surprisingly clear, though it seems to come from somewhere deep "
                "in its throat. 'The gold is mine. The cave is mine. Everything you see is mine. "
                "Turn back, little thief, or become my next meal.'\n\n"
                "The serpent coils tighter, blocking the cave entrance completely. Beyond it, you can glimpse "
                "the glint of ancient gold.\n\n"
                "You could FIGHT the serpent (dangerous), GIVE it the Antidote Herb (it is sick — the herb may heal it), "
                "or GIVE it the Golden Apple or Everlasting Fruit as a bribe."
            ),
            "fight": (
                "You draw your weapon and rush at the serpent! It strikes with blinding speed — "
                "its fangs sink into your shoulder... but Conganchnes shoves you aside, taking the blow himself. "
                "The fangs snap against his invulnerable skin!\n\n"
                "The serpent recoils, hissing in confusion. In that moment of distraction, you land a blow "
                "on its neck. It thrashes, knocking you both to the ground, and lashes out with its tail — "
                "sending you tumbling out of the cave.\n\n"
                "When you scramble back to your feet, the serpent has retreated deeper into the cave. "
                "Its hiss echoes from the darkness: 'Fine. Take the gold. It brings nothing but greed and death anyway.'\n\n"
                "You emerge with the treasure, battered but victorious. One crew member was wounded but will recover.\n\n"
                "(+2 points. You may now take the treasure gold.)"
            ),
            "mercy": (
                "You hold out the Antidote Herb. The serpent's head draws back, its nostrils flaring.\n\n"
                "'That smell... I know that smell. It is the herb that grows on the Serpent's Island — "
                "the one cure for the venom I have carried in my blood since I was wounded by a sea drake.\n\n"
                "The serpent lowers its head. Its voice is softer now. 'Give it to me. Please. "
                "I have been in pain for a hundred years. This gold is not worth the agony.'\n\n"
                "You give the herb to the serpent. It swallows it whole, and a shudder runs through its massive body. "
                "Its scales ripple, and the sickly yellow in its eyes fades to a healthy gold.\n\n"
                "'The pain... is gone. Thank you, little one. The gold is yours. Take it all. "
                "I will find a new cave, one without ancient curses in it.'\n\n"
                "The serpent uncoils and slides past you into the sea, free at last.\n\n"
                "(+3 points. You may now take the treasure gold.)"
            ),
            "give": (
                "You offer the tribute to the serpent. It inspects the offering with its tongue, then — "
                "slowly — uncoils a fraction of its body, revealing a narrow gap in the cave entrance.\n\n"
                "'Payment accepted,' it hisses. 'The gold is in the back. Take what you can carry. "
                "But hurry — my patience is as thin as my skin.'\n\n"
                "You slip past the serpent into the cave. The treasure awaits.\n\n"
                "(+1 point. You may now enter the cave.)"
            ),
        },
        visible_if=lambda s: not s.has_flag('serpent_passed'),
    )

    n["great_hound"] = NPC(
        "great_hound", "The Great Hound",
        "A hound the size of a small horse, with a coat of iron-grey fur and eyes that burn like embers. It lies before a stone pedestal, upon which rests a silver torc that gleams with ancient light. The hound's lips curl back to reveal teeth like ivory daggers.",
        aliases=["dog", "hound", "wolf", "beast", "great hound", "guard dog"],
        dialogue={
            "greeting": (
                "The Great Hound rises slowly, hackles raised. A low, rumbling growl issues from its chest — "
                "a sound like falling rocks. Its eyes fix on you with unwavering intensity.\n\n"
                "It does not attack. Not yet. It stands between you and the silver torc, guarding it with the "
                "patience of a creature that has stood sentinel for centuries.\n\n"
                "The torc gleams on its pedestal. It is clearly valuable — a masterpiece of ancient silversmithing.\n\n"
                "You could GIVE the hound food (Bowl of Milk, Everlasting Fruit), FIGHT it, or TALK to it "
                "with the Speaking Feather."
            ),
            "give": (
                "You offer the food to the hound. Its ears perk up. The growling stops.\n\n"
                "It sniffs the offering once, twice, then takes it gently from your hand with surprising delicacy. "
                "It eats in three quick bites, then licks its chops — and its tail wags once.\n\n"
                "Just once. A massive, heavy thump against the ground.\n\n"
                "The hound steps aside and lies down, watching you with mild interest. You may take the torc.\n\n"
                "(+1 point. The Silver Torc is yours.)"
            ),
            "fight": (
                "You rush the hound with your weapon drawn. It meets your charge with terrifying speed — "
                "knocking you flat and pinning you to the ground with one massive paw.\n\n"
                "Its jaws close around your arm — but do not bite down. It holds you there, staring into your eyes, "
                "breathing hot and wet on your face.\n\n"
                "Then it releases you, steps back, and lies down again. It seems to be saying: "
                "'I could have killed you. I chose not to. Try a different approach.'\n\n"
                "You scramble to your feet, unharmed but humbled. The hound watches, unimpressed."
            ),
            "talk": (
                "You hold up the Speaking Feather. The hound cocks its head, and you hear its voice "
                "in your mind — rough, ancient, weary.\n\n"
                "'You speak the language of beasts. Few do, these days.'\n\n"
                "'This torc was placed here by my master a thousand years ago. He asked me to guard it until he returned. "
                "He never did. I have waited. I have watched. I have kept my word.'\n\n"
                "'But I am old now. My joints ache. My eyes grow dim. I would like to rest. "
                "If you can give me something to ease my hunger and my vigil, the torc is yours.'\n\n"
                "The hound's voice fades. You know what you must do.\n\n"
                "(Talked to the hound. Give it food to complete the bargain.)"
            ),
            "master": (
                "'My master was a king of this island. He sailed east a thousand years ago "
                "and never returned. I have kept my promise. I hope he kept his.'\n\n"
                "The hound whines softly and lays its head on its paws."
            ),
        },
        visible_if=lambda s: not s.has_flag('dog_pacified'),
    )

    n["mountain_lion"] = NPC(
        "mountain_lion", "Mountain Lion",
        "A great mountain lion, its coat the colour of dried grass, crouched before a cave on a scrub-covered island. Its muscles ripple beneath its skin, and its eyes are wild with pain and fury. A deep wound — a gash from some other predator — weeps along its flank.",
        aliases=["lion", "beast", "mountain lion", "predator", "big cat"],
        dialogue={
            "greeting": (
                "The mountain lion roars — a raw, guttural sound that vibrates through your bones. "
                "It bares its fangs and crouches, ready to spring.\n\n"
                "But as it shifts its weight, you see the wound on its flank — a terrible gash, "
                "oozing and infected. The beast is in agony. Its attacks are born of pain, not malice.\n\n"
                "You could FIGHT it (with Magic Harpoon or Giant's Club), USE the Silver Bell to calm it, "
                "or TALK to it with the Speaking Feather to learn of its wound."
            ),
            "fight": (
                "You brandish your weapon. The lion charges.\n\n"
                "The battle is fierce — all claws and roars and blood. But your weapon finds its mark, "
                "and after a desperate struggle, the beast is driven off. It limps into the cave, "
                "growling, and does not emerge again.\n\n"
                "Your crew cheers. The island is safe. You find a LION'S CLAW on the ground — "
                "broken off in the fight. It is sharp and still warm.\n\n"
                "(+2 points. Gained: Lion's Claw)"
            ),
            "calm": (
                "You ring the Silver Bell. Its pure, clear tone cuts through the lion's fury.\n\n"
                "The lion stops mid-crouch. Its ears swivel. The growling subsides.\n\n"
                "It sits down heavily, blinking slowly. The pain is still in its eyes, but the rage "
                "has drained away. It mews — a pathetic, broken sound from so mighty a creature.\n\n"
                "You approach slowly. It lets you examine its wound. With gentle hands, "
                "you clean it and bind it with cloth from your tunic. The lion licks your hand once — "
                "a rough, warm thank you.\n\n"
                "It rises and pads into the cave, returning with a LION'S CLAW in its mouth — "
                "one it shed naturally. It drops it at your feet.\n\n"
                "(+2 points. Gained: Lion's Claw. The lion is calm.)"
            ),
            "talk": (
                "You hold up the Speaking Feather. The lion's ears flick forward. "
                "A voice — ragged, pained — enters your mind.\n\n"
                "'The feather-borne one... speaks. Few do. You are strange, little two-legs.'\n\n"
                "'I am hurt. A sea serpent — a young one, foolish — caught me unawares. "
                "Its venom festers in my blood. If you have something to heal me... "
                "I would be grateful.'\n\n"
                "The lion's eyes plead. If you have Fountain Water, you could USE it to heal the lion."
            ),
            "use": (
                "You pour the Fountain Water onto the lion's wound. "
                "The milky liquid sizzles, and the infection begins to recede. "
                "The torn flesh knits together, slowly but surely.\n\n"
                "The lion's eyes widen. It flexes its muscles, testing the healed limb. "
                "A deep, rumbling purr fills the air — the first sound of contentment "
                "the beast has made in weeks.\n\n"
                "The lion presses its head against your hand, then pads into the cave. "
                "It returns with a LION'S CLAW in its jaws — a gift, freely given.\n\n"
                "'You have my gratitude, feather-borne one. Go in peace.'\n\n"
                "(+3 points. Gained: Lion's Claw.)"
            ),
        },
        visible_if=lambda s: not (s.has_flag('lion_fought') or s.has_flag('lion_pacified')),
    )

    n["anchorite"] = NPC(
        "anchorite", "The Anchorite",
        "A gaunt, serene man in a simple grey robe, sitting cross-legged in the mouth of a cave on a lonely rock. His face is weathered by wind and wisdom, and his eyes hold the quiet certainty of someone who has found what he was looking for. A small wooden cross hangs around his neck. A single candle burns beside him, though no one has lit it.",
        aliases=["hermit", "anchorite", "holy man", "monk", "ascetic", "second hermit"],
        dialogue={
            "greeting": (
                "The Anchorite looks up as you approach, and a gentle smile spreads across his face. "
                "He gestures to a flat stone beside him.\n\n"
                "'Sit, Mael Duin. I have been expecting you. The gulls told me you were coming. "
                "They are terrible gossips, but their information is reliable.'\n\n"
                "His voice is warm, like a fire after a long voyage. The sea seems quieter here. "
                "The wind holds its breath.\n\n"
                "'You have travelled far — further than you know. The islands you have visited were not "
                "random specks on the sea. They were mirrors. Each one showed you a part of yourself. "
                "The giant's rage. The serpent's greed. The hound's loyalty. The lion's wounded pride. "
                "All of them were you. All of them were lessons.'\n\n"
                "He falls silent, letting the words settle like sediment in clear water."
            ),
            "trials": (
                "'Each island was a trial, yes. But not the kind you think. "
                "The giant did not test your strength — he tested your choice of how to use it. "
                "The serpent did not test your courage — she tested your compassion. "
                "The hound tested your patience. The lion tested your mercy.\n\n"
                "'And every time you chose wisely, you became more yourself.'\n\n"
                "He nods slowly, as if confirming something to himself."
            ),
            "forgiveness": (
                "The Anchorite's eyes grow deep and serious. He speaks slowly, choosing each word with care.\n\n"
                "'The men who killed your father were given to you as a test — not a target. "
                "The sea did not bring you to Garbh so you could spill his blood. "
                "It brought you to him so you could choose not to.\n\n"
                "'Forgiveness is not weakness, Mael Duin. It is the hardest kind of strength. "
                "It is easy to kill a man. It is nearly impossible to let him live — "
                "and to mean it when you say he is forgiven.\n\n"
                "'Your father does not want revenge. He wants you to be free. "
                "The chain that binds you is not made of iron. It is made of grief. "
                "And only you can unlink it.'\n\n"
                "The candle flickers, though there is no wind."
            ),
            "father": (
                "'Ailill is at peace. He crossed the great sea before you, and he waits on the far shore. "
                "He does not count the days. He does not hold a grudge. "
                "He watches you with love and hope, as any father watches his son.\n\n"
                "'The only one who is not at peace is you. And that peace is yours to claim — "
                "whenever you are ready.'"
            ),
            "home": (
                "'You will return when the wind is ready. And the wind is always ready — "
                "it is you who are not.'\n\n"
                "He smiles at your expression.\n\n"
                "'You have not yet finished your voyage. But you will. "
                "And when you do, you will find that home was never a place — "
                "it was a feeling. And that feeling has been with you all along.'"
            ),
            "sea": (
                "'The sea is God's breath upon the water,' he says softly. "
                "'It is older than the mountains, older than sin, older than memory. "
                "It carries prayers in its currents and secrets in its depths.\n\n"
                "'You have sailed upon it for three years, Mael Duin. "
                "You have learned its language — the rhythm of the tides, the warnings in the clouds, "
                "the songs in the creaking of your curragh's timbers.\n\n"
                "'The sea has changed you. It has washed away what was not essential. "
                "Look at your hands. They are the same hands that pushed off from the Aran shore. "
                "But the man they belong to is not the same.\n\n"
                "'That is what the sea does. It is a mirror, and it shows you who you truly are.'"
            ),
            "death": (
                "'Death is not the enemy, Mael Duin. It is the doorway. "
                "Your father walked through it before you. You will walk through it after. "
                "The only question is what you carry in your hands when you do.\n\n"
                "'Will you carry a sword? Or will you carry peace?'"
            ),
        }
    )

    npcs.update(n)



_make_npcs()

