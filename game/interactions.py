"""Everything-with-everything interaction system for The Voyage of Mael Duin.

Provides three functions:
  - get_give_response(state, item, npc)  → string
  - get_use_response(state, item, target) → string
  - get_talk_topic_response(state, npc, topic) → string

Each checks for specific combinations first, then falls back to
contextual / humorous defaults based on item categories and NPC personalities.
"""

import random

# ---------------------------------------------------------------------------
# Categorisation helpers
# ---------------------------------------------------------------------------

FOOD_ITEMS = {
    "everlasting_fruit", "wisdom_salmon", "crew_provisions",
    "talking_cat_tribute",
}

WEAPON_ITEMS = {
    "magic_harpoon", "glass_shard",
}

TREASURE_ITEMS = {
    "golden_apple", "pearl", "demon_coin", "crystal_pillar_fish",
}

TOOL_ITEMS = {
    "silver_bell", "silver_net", "earplugs", "trumpet_muffler",
    "revolving_key",
}

MAGICAL_ITEMS = {
    "magic_thread", "speaking_feather", "laughing_potion", "truth_ring",
    "hermit_blessing", "prophecy_scroll", "antidote_herb",
}

MATERIAL_ITEMS = {
    "otter_pelt", "fiery_ash",
}

# NPC personality groups
WISE_NPCS = {"druid", "hermit", "prophet_boy"}
DANGEROUS_NPCS = {"cat", "laughing_king", "water_horse", "demon_smith", "skull", "black_pig", "serpent"}
SOCIAL_NPCS = {"queen", "smith", "diuran_npc", "conganchnes_npc", "fergus_npc"}
NEUTRAL_NPCS = set()  # any not in the above


def _item_category(item_id):
    if item_id in FOOD_ITEMS:
        return "food"
    if item_id in WEAPON_ITEMS:
        return "weapon"
    if item_id in TREASURE_ITEMS:
        return "treasure"
    if item_id in TOOL_ITEMS:
        return "tool"
    if item_id in MAGICAL_ITEMS:
        return "magical"
    if item_id in MATERIAL_ITEMS:
        return "material"
    return "misc"


def _npc_personality(npc_id):
    if npc_id in WISE_NPCS:
        return "wise"
    if npc_id in DANGEROUS_NPCS:
        return "dangerous"
    if npc_id in SOCIAL_NPCS:
        return "social"
    return "neutral"


# ---------------------------------------------------------------------------
# SPECIFIC GIVE combinations  (item → NPC)
# ---------------------------------------------------------------------------

_SPECIFIC_GIVE = {}

# Helper to register
def _register_give(item_id, npc_id, fn):
    _SPECIFIC_GIVE.setdefault(item_id, {})[npc_id] = fn


# ---- Story-canonical give responses ----

def _give_laughing_potion_to_king(state, item, npc):
    state.set_flag("king_pacified")
    state.score += 2
    return (
        'You offer the Laughing Potion back to the king. His eyes light up — well, '
        'they were already lit up, but now they sparkle like exploding stars.\n\n'
        '"OH! My own potion! I lost it ages ago! I\'ve been trying to laugh without it '
        'and let me tell you — it\'s EXHAUSTING!"\n\n'
        'He uncorks it and takes a sip. Instantly, his laughter changes pitch — '
        'it\'s now a perfect harmonised duet with itself. The entire island joins in.\n\n'
        '"Take ANYTHING you want!" he wheezes. "Except my stool. I need the stool."\n\n'
        "(+2 points. The king is eternally grateful.)"
    )


def _give_prophecy_scroll_to_druid(state, item, npc):
    state.score += 3
    return (
        'The druid reads the scroll and nods slowly. His milky eyes seem to focus '
        'on something far beyond the parchment.\n\n'
        '"So... the prophetic boy confirms what the wind has been whispering. '
        'Your father\'s murderers are not the true quarry, Mael Duin. The real '
        'treasure lies in what you become along the way."\n\n'
        'He hands the scroll back to you. "Keep it. Read it again when you reach '
        'the end of your journey. The words will have changed by then."\n\n'
        "(+3 points. The druid's cryptic wisdom intensifies.)"
    )


def _give_pearl_to_queen(state, item, npc):
    state.score += 3
    state.set_flag("pearl_given_to_queen")
    return (
        'The queen examines the pearl with cold interest. She holds it up to the '
        'light, and for a moment the entire room glows with an inner luminescence.\n\n'
        '"A sea pearl from the Cat\'s Island. How... thoughtful. The cat must have '
        'liked you. It doesn\'t give these to just anyone."\n\n'
        'She slips it into a hidden pocket in her gown. "You may stay another night '
        'if you wish. Or you may leave. The pearl has bought you freedom either way."\n\n'
        'There is something sad in her voice now, as if the pearl reminded her of '
        'a life she once had before the island.\n\n'
        "(+3 points. The queen is slightly less ominous now.)"
    )


def _give_magic_harpoon_to_smith(state, item, npc):
    state.score += 2
    return (
        'The smith admires his own work with the pride of a parent whose child just '
        'won a footrace.\n\n'
        '"Ah, the Magic Harpoon! I remember forging this. The trick was the quenching '
        '— I used the tears of a sea monster. Gives it that... zing."\n\n'
        'He tosses it back to you. "Keep it, little man. A weapon should be used, '
        'not admired. Though I do admire it. It\'s beautiful. Look at those spirals. '
        'Perfection."\n\n'
        'He wipes a tear from his soot-streaked cheek.\n\n'
        "(+2 points. The smith is emotionally moved by his own craftsmanship.)"
    )


def _give_silver_bell_to_hermit(state, item, npc):
    state.score += 2
    return (
        'The hermit rings the bell softly. A pure, clear tone washes across the '
        'rock, and for a moment even the waves seem to hold their breath.\n\n'
        '"This bell was forged in the Island of the Culdees. Its ring carries the '
        'prayers of a hundred holy men. It calms not storms, but the heart that '
        'braves them."\n\n'
        'He hands it back. "Keep it. Ring it when the despair of your quest '
        'threatens to drown you. The sound will remind you that you are not alone."\n\n'
        'The otter at his feet chirps in agreement.\n\n'
        "(+2 points. A moment of peace washes over you.)"
    )


def _give_glass_shard_to_cat(state, item, npc):
    state.score += 1
    return (
        'The cat bats at the shard like a toy, rolling it across the floor '
        'with a massive paw. The shard catches the light and throws rainbows '
        'across the walls.\n\n'
        '"Ooooh. Shiny. Moving. Dangerous. This is the best thing a human has ever '
        'given me. I shall treasure it until I get bored, which will be in '
        'approximately three minutes."\n\n'
        'The cat stares at the shard, mesmerised. You take the opportunity to '
        'back away slowly.\n\n'
        "(+1 point. The cat is entertained. For now.)"
    )


def _give_golden_apple_to_pig(state, item, npc):
    state.score += 3
    state.set_flag("pig_pacified")
    return (
        'The pig wakes up and snorts, its massive nostrils flaring. It fixes '
        'its beady eyes on the golden apple in your hand.\n\n'
        'For a moment, nothing happens. Then the pig charges — not at you, '
        'but past you, circling back with surprising grace for a creature of its bulk. '
        'It comes to a halt in front of you and sits, like a very large, very '
        'menacing dog waiting for a treat.\n\n'
        'You toss the apple. The pig catches it in mid-air with a crunch that '
        'sounds like a tree falling. It chews happily, and golden juice drips '
        'from its jowls.\n\n'
        'When it finishes, it lies down and goes back to sleep, blocking nothing.\n\n'
        "(+3 points. The pig is content. You may pass freely.)"
    )


def _give_antidote_herb_to_serpent(state, item, npc):
    state.score += 3
    state.set_flag("serpent_calmed")
    return (
        'The serpent tastes the herb and relaxes. Its massive coiled body '
        'unwinds slowly, like a rope being unravelled by a very careful god.\n\n'
        'The serpent\'s forked tongue flicks out, sampling the air. Its eyes, '
        'which were slits of pure menace, soften into something almost resembling '
        'gratitude.\n\n'
        '"The herb," it hisses, "is the only thing that grows on this island that '
        'I cannot digest. It is my weakness. You have shown me mercy. I will '
        'remember this."\n\n'
        'It slithers aside, clearing the path ahead.\n\n'
        "(+3 points. The great serpent is no longer your enemy.)"
    )


def _give_otter_pelt_to_hermit(state, item, npc):
    state.score += 2
    state.set_flag("otter_pelt_returned")
    return (
        'The hermit sadly accepts his otter\'s pelt, his hands trembling. '
        'He holds it to his chest and closes his eyes.\n\n'
        '"My companion... my friend. I thought I had lost him to the sea, '
        'but it seems he simply... shed his old skin and moved on."\n\n'
        'He looks at you with wet eyes. "You have brought me closure, Mael Duin. '
        'It is a gift more precious than gold. The otter is in a better place now — '
        'probably chasing fish in the Great Stream beyond the sky."\n\n'
        'He wraps the pelt around his shoulders. It fits perfectly.\n\n'
        '(The hermit looks a little warmer now. And a little more at peace.)'
    )


def _give_everlasting_fruit_to_any(state, item, npc):
    """Everlasting fruit to ANY NPC — always the same gag."""
    return (
        f'You offer the Everlasting Fruit to {npc.name}. They take a bite. '
        'Nothing happens. They take another bite. Still nothing. '
        f'They look at the fruit, then at you. "{npc.name} looks unimpressed."\n\n'
        'They take a third bite. The fruit looks exactly the same as when you '
        'offered it. They sigh and hand it back.\n\n'
        '"It tastes like nothing," they say. "And yet, also like disappointment."'
    )


# Register all specific give combos
# The ones explicitly requested:
_register_give("laughing_potion", "laughing_king", _give_laughing_potion_to_king)
_register_give("prophecy_scroll", "druid", _give_prophecy_scroll_to_druid)
_register_give("pearl", "queen", _give_pearl_to_queen)
_register_give("magic_harpoon", "smith", _give_magic_harpoon_to_smith)
_register_give("silver_bell", "hermit", _give_silver_bell_to_hermit)
_register_give("glass_shard", "cat", _give_glass_shard_to_cat)
_register_give("golden_apple", "black_pig", _give_golden_apple_to_pig)
_register_give("antidote_herb", "treasure_serpent", _give_antidote_herb_to_serpent)
_register_give("otter_pelt", "hermit", _give_otter_pelt_to_hermit)
# everlasting_fruit gets special per-NPC handling below
_register_give("everlasting_fruit", "__any__", _give_everlasting_fruit_to_any)

# ---- LEVEL 07 GIVE HANDLERS ----
def _give_food_to_giant(state, item, npc):
    state.set_flag("giant_mollified")
    state.score += 1
    return (
        f'You offer {item.name} to the giant. He squints at it, sniffs suspiciously, '
        "then snatches it from your hand and stuffs it into his mouth.\n\n"
        "'Hmph,' he grunts, chewing noisily. 'Not bad. You may pass, little man. "
        "But tell your friends to bring better food next time.'\n\n"
        "The giant settles back onto his cliff, patting his belly with satisfaction. "
        "He does not throw any more stones.\n\n"
        "(+1 point. No crew lost.)"
    )

def _give_treasure_to_serpent(state, item, npc):
    return (
        "The serpent eyes the treasure with ancient hunger. "
        "Its coils shift, allowing you a glimpse deeper into the cave.\n\n"
        "'Mine,' it hisses. 'But... you have brought me gold. Shiny gold. "
        "I am... satisfied. Take what you need from the cave. "
        "Leave the gold, and we are even.'\n\n"
        "The serpent's coils part just enough for one person to slip through.\n\n"
        "(+2 points.)"
    )

def _give_antidote_herb_to_treasure_serpent(state, item, npc):
    state.set_flag("serpent_passed")
    state.score += 3
    from .levels._shared import items as shared_items
    gold = shared_items.get("treasure_gold")
    loc = state.get_location()
    if gold and loc:
        loc.items.append(gold)
    return (
        'You offer the Antidote Herb to the serpent. It recoils at first, hissing, '
        "but then its forked tongue flicks out, tasting the herb.\n\n"
        "It takes the herb into its mouth and swallows. Almost immediately, "
        "the sickly green hue fades from its scales, replaced by a healthy emerald.\n\n"
        "'The herb... it heals the poison that has been eating at me for decades.' "
        "The serpent's voice is softer now, almost grateful.\n\n"
        "It uncoils from the cave entrance and slithers aside. Beyond, you see "
        "the gleam of ANCIENT GOLD.\n\n"
        "(+3 points. The serpent is healed and grateful.)"
    )

def _give_food_to_hound(state, item, npc):
    state.set_flag("dog_pacified")
    state.score += 2
    return (
        f'You offer {item.name} to the Great Hound. It sniffs cautiously, '
        "then takes it gently from your hand with surprising delicacy for a creature its size.\n\n"
        "The hound wolfs it down in two bites, then licks its chops and lies down, "
        "its head on its paws. It watches you with soft, grateful eyes.\n\n"
        "It does not stir as you take the Silver Torc from the pedestal. "
        "Its tail thumps once on the ground.\n\n"
        "(+2 points. The Great Hound has accepted you.)"
    )

def _give_food_to_lion(state, item, npc):
    state.score += 1
    return (
        f'You offer {item.name} to the wounded lion. It snarls weakly at first, '
        "but the scent of food is too much. It takes the offering and eats ravenously.\n\n"
        "When it finishes, it licks its wounded flank and looks at you with slightly less hostility. "
        "It does not move aside, but it does not attack either.\n\n"
        "The lion still blocks the cave, but it is no longer actively hostile. "
        "You may need to do more to earn its trust."
    )

_register_give("crew_provisions", "giant", _give_food_to_giant)
_register_give("everlasting_fruit", "giant", _give_food_to_giant)
_register_give("demon_coin", "treasure_serpent", _give_treasure_to_serpent)
_register_give("golden_apple", "treasure_serpent", _give_treasure_to_serpent)
_register_give("antidote_herb", "treasure_serpent", _give_antidote_herb_to_treasure_serpent)
_register_give("everlasting_fruit", "great_hound", _give_food_to_hound)
_register_give("crew_provisions", "great_hound", _give_food_to_hound)
_register_give("talking_cat_tribute", "great_hound", _give_food_to_hound)
_register_give("everlasting_fruit", "mountain_lion", _give_food_to_lion)
_register_give("crew_provisions", "mountain_lion", _give_food_to_lion)


# ---------------------------------------------------------------------------
# FALLBACK give responses by category × personality
# ---------------------------------------------------------------------------

_GIVE_FALLBACKS = {}

def _r(variants):
    """Pick a random response from a list of variants."""
    return random.choice(variants) if isinstance(variants, (list, tuple)) else variants


# --- food to wise ---
_GIVE_FALLBACKS[("food", "wise")] = lambda s, i, n: _r([
    f'{n.name} accepts the {i.name} with a serene nod. "All nourishment is sacred," '
    'they intone, and take a single, deliberate bite. "Thank you, traveler."',
    f'{n.name} examines the {i.name} as if reading its entire life story. '
    '"This was grown under a full moon," they murmur. "I can tell." '
    'They take a small bite and smile enigmatically.',
])

# --- food to dangerous ---
_GIVE_FALLBACKS[("food", "dangerous")] = lambda s, i, n: _r([
    f'{n.name} sniffs the {i.name} suspiciously. "Is this a trick?" they growl. '
    'After a long, uncomfortable pause, they snatch it from your hand and '
    'gulp it down in one go. "Acceptable."',
    f'You offer the {i.name}. {n.name} stares at it, then at you, then back at '
    'the food. "You know," they say, "the last person who offered me food '
    'is now a decorative shrub." They eat it anyway.',
])

# --- food to social ---
_GIVE_FALLBACKS[("food", "social")] = lambda s, i, n: _r([
    f'{n.name} beams. "How thoughtful!" They accept the {i.name} and '
    'take a gracious bite. "You know, hospitality is the cornerstone of '
    'civilisation. Would you like some salt?"',
    f'{n.name} examines the {i.name} with the eye of a connoisseur. '
    '"Hmm. Not bad. A bit... travel-worn, but the flavour profile holds up." '
    'They eat it with surprising delicacy.',
])

# --- weapon to wise ---
_GIVE_FALLBACKS[("weapon", "wise")] = lambda s, i, n: _r([
    f'{n.name} holds the {i.name} up to the light. "A weapon is a tool, '
    'no different from a plough. It is the hand that wields it that makes it '
    'good or evil." They hand it back with a sad smile.',
    f'{n.name} runs a finger along the edge of the {i.name}. "Sharp. '
    'Like grief. Be careful what you cut with it."',
])

# --- weapon to dangerous ---
_GIVE_FALLBACKS[("weapon", "dangerous")] = lambda s, i, n: _r([
    f'{n.name} grabs the {i.name} and test-swings it through the air. '
    '"Nice balance. Good weight. Did you make this yourself, or did you '
    'take it from someone who no longer needed it?"',
    f'{n.name} laughs at the {i.name}. "You think this will protect you '
    'from ME? That\'s adorable." They toss it back with unnecessary force.',
])

# --- weapon to social ---
_GIVE_FALLBACKS[("weapon", "social")] = lambda s, i, n: _r([
    f'{n.name} accepts the {i.name} politely, clearly not a warrior. '
    '"It\'s very... stabby. I\'ll put it with the others." They set it aside '
    'with the same reverence one might give a piece of abstract art.',
    f'{n.name} hefts the {i.name}. "Not bad. Not the best I\'ve seen, '
    'but it\'ll kill a man well enough. Or a fish. Whatever you\'re after."',
])

# --- treasure to wise ---
_GIVE_FALLBACKS[("treasure", "wise")] = lambda s, i, n: _r([
    f'{n.name} looks at the {i.name} without touching it. "Shiny. Valuable. '
    'And utterly meaningless. You cannot eat gold, you cannot drink jewels, '
    'and you cannot take them with you to the next world." They push it gently back.',
    f'{n.name} weighs the {i.name} in their palm. "This represents someone\'s '
    'greed, someone\'s loss, and someone\'s regret. Which one are you?"',
])

# --- treasure to dangerous ---
_GIVE_FALLBACKS[("treasure", "dangerous")] = lambda s, i, n: _r([
    f'{n.name} snatches the {i.name} greedily. "MINE. ...I mean, thank you for this '
    'generous offering. You may live. For now."',
    f'{n.name} stares at the {i.name} with undisguised avarice. "Ooooh. Shiny. '
    'Give. Now. Please. With sugar on top. Actually, skip the sugar, just give."',
])

# --- treasure to social ---
_GIVE_FALLBACKS[("treasure", "social")] = lambda s, i, n: _r([
    f'{n.name} admires the {i.name} with genuine delight. "Exquisite craftsmanship! '
    'Where did you find this? I must know the story behind it." They listen intently '
    'as you explain, nodding thoughtfully.',
    f'{n.name} holds the {i.name} up to the light. "This would fetch a fine price '
    'in any market. Are you sure you want to give it away? Well, far be it from me '
    'to refuse such a gift."',
])

# --- tool to wise ---
_GIVE_FALLBACKS[("tool", "wise")] = lambda s, i, n: _r([
    f'{n.name} examines the {i.name} with quiet reverence. "A tool is a bridge '
    'between intention and reality. This one... has been well used." '
    'They hand it back with a knowing look.',
    f'{n.name} tests the {i.name}. "Clever. A simple solution to a complex '
    'problem. That is the mark of true wisdom." They nod approvingly.',
])

# --- tool to dangerous ---
_GIVE_FALLBACKS[("tool", "dangerous")] = lambda s, i, n: _r([
    f'{n.name} turns the {i.name} over in their hands. "What does it DO? '
    'Is it a weapon? It looks like it could be a weapon if you tried hard enough. '
    'Everything is a weapon if you\'re creative."',
    f'{n.name} fiddles with the {i.name} until it breaks. "Oops. '
    'Anyway." They hand the pieces back.',
])

# --- tool to social ---
_GIVE_FALLBACKS[("tool", "social")] = lambda s, i, n: _r([
    f'{n.name} accepts the {i.name} with interest. "Oh, I\'ve always wanted '
    'one of these! Not this specific one, but the general concept. Thank you!"',
    f'{n.name} tries to use the {i.name} for its intended purpose, fails, '
    'and then uses it as a conversation piece instead. "Fascinating!"',
])

# --- magical to wise ---
_GIVE_FALLBACKS[("magical", "wise")] = lambda s, i, n: _r([
    f'{n.name} holds the {i.name} and closes their eyes. "I can feel the '
    'weave of destiny around this object. It has touched many hands and will '
    'touch many more. You are but one thread in its tapestry."',
    f'{n.name} touches the {i.name} and shivers. "Old magic. Very old. '
    'Be careful with this — it remembers things that people have forgotten."',
])

# --- magical to dangerous ---
_GIVE_FALLBACKS[("magical", "dangerous")] = lambda s, i, n: _r([
    f'{n.name} recoils from the {i.name}. "Get that THING away from me! '
    'I can smell the enchantment on it. It smells like... like a library."',
    f'{n.name} pokes the {i.name} with a stick. "Magic? I don\'t trust magic. '
    'Magic is just cheating with extra steps."',
])

# --- magical to social ---
_GIVE_FALLBACKS[("magical", "social")] = lambda s, i, n: _r([
    f'{n.name} gasps at the {i.name}. "Is this... is this MAGIC? I\'ve never '
    'seen real magic before! Well, except that one time with the goat. But '
    'that might have been indigestion."',
    f'{n.name} accepts the {i.name} carefully, as if it might explode. '
    '"Thank you. I shall treasure it. Or maybe I\'ll sell it. I haven\'t decided."',
])

# --- material to wise ---
_GIVE_FALLBACKS[("material", "wise")] = lambda s, i, n: _r([
    f'{n.name} touches the {i.name} gently. "From the earth, to the craftsman, '
    'to your hands, to mine. Everything is connected." They nod sagely.',
    f'{n.name} examines the {i.name}. "This has potential. Like a seed, '
    'it could become many things. Or it could remain exactly what it is. '
    'The choice is not in the object, but in the hands that hold it."',
])

# --- material to dangerous ---
_GIVE_FALLBACKS[("material", "dangerous")] = lambda s, i, n: _r([
    f'{n.name} sniffs the {i.name}. "Smells like... stuff. I like stuff. '
    'I\'ll put it with my other stuff." They add it to a pile of miscellaneous '
    'objects that looks like a dragon\'s hoard curated by a raccoon.',
    f'{n.name} grabs the {i.name} and adds it to their collection. '
    '"One day," they say, "all of this will be worth something. Or it will '
    'burn. Either way, it\'ll be spectacular."',
])

# --- material to social ---
_GIVE_FALLBACKS[("material", "social")] = lambda s, i, n: _r([
    f'{n.name} accepts the {i.name} politely. "Raw materials! The building '
    'blocks of civilisation. I\'ll have my artisans turn this into something '
    'beautiful."',
    f'{n.name} looks at the {i.name} with the eye of a craftsman. "Good quality. '
    'Needs work, but the potential is there. Thank you."',
])

# --- misc fallback for anything not covered ---
_GIVE_FALLBACKS[("misc", "wise")] = lambda s, i, n: _r([
    f'{n.name} looks at the {i.name} with quiet curiosity. "Everything has '
    'a story. What is this one\'s?"',
    f'{n.name} accepts the {i.name}. "I don\'t know what this is, but I sense '
    'it is important to someone, somewhere. Perhaps that someone is you."',
])

_GIVE_FALLBACKS[("misc", "dangerous")] = lambda s, i, n: _r([
    f'{n.name} glares at the {i.name}. "What am I supposed to do with this? '
    'I can\'t eat it, I can\'t fight with it, I can\'t even sit on it properly."',
    f'{n.name} stares at the {i.name} blankly. "Is this a joke? Because if '
    'it is, it\'s not funny. If it\'s not a joke, it\'s even less funny."',
])

_GIVE_FALLBACKS[("misc", "social")] = lambda s, i, n: _r([
    f'{n.name} accepts the {i.name} graciously. "How... unconventional. '
    'I\'ll treasure it always. Or at least until the next interesting thing '
    'comes along."',
    f'{n.name} turns the {i.name} over in their hands. "Well, this is certainly '
    'a thing. And it is certainly being given to me. I suppose I should say thank you?"',
])


def _get_fallback_give(item, npc):
    cat = _item_category(item.id)
    pers = _npc_personality(npc.id)
    key = (cat, pers)
    if key in _GIVE_FALLBACKS:
        return _GIVE_FALLBACKS[key]
    # If we somehow missed, return generic
    return lambda s, i, n: _r([
        f'You offer the {i.name} to {n.name}. They take it, look at it, '
        'and say, "Huh. Thanks, I guess."',
        f'You give the {i.name} to {n.name}. They accept it without comment, '
        'which is somehow more insulting than if they had commented.',
        f'{n.name} accepts the {i.name}. "Right. This exists. So do I. '
        'We\'re both here. Accepting this moment."',
    ])


# ---------------------------------------------------------------------------
# SPECIFIC USE combinations  (item × target)
# ---------------------------------------------------------------------------

_SPECIFIC_USE = {}

def _register_use(item_id, target_id, fn):
    _SPECIFIC_USE.setdefault(item_id, {})[target_id] = fn


def _use_earplugs_on_trumpet(state, item, target):
    state.set_flag("earplugs_used")
    state.score += 3
    return (
        'You stuff the earplugs into your ears just as the giant trumpet '
        'blasts at full volume. The sound is still earth-shaking, but your '
        'eardrums remain intact. The ground trembles, trees sway, and a '
        'nearby bird turns inside out from the sheer force of the note.\n\n'
        'When the blast subsides, you remove the earplugs. Your ears are ringing, '
        'but you can still hear. The trumpet has sounded \u2014 but you survived.\n\n'
        "WARNING: The bellows are filling again. You can leave safely now, "
        "but the next visitor won't be so lucky."
        " (+3 points. Not deaf. That's a win.)"
    )


def _use_trumpet_muffler_on_trumpet(state, item, target):
    state.set_flag("trumpet_muffled")
    state.score += 4
    return (
        'You take the Trumpet Muffler \u2014 that strange cloth of layered otter fur and waxed linen \u2014 '
        'and stuff it deep into the trumpet\'s bell. It fits perfectly, as if it was made for this purpose.\n\n'
        'The trumpet groans. A low, bassy note tries to escape but dies in the cloth, '
        'emerging as little more than a flatulent whisper. The mechanism behind the bellows '
        'winds down with a sad sigh.\n\n'
        '"Well," says Diur\u00e1n, "that\'s the least dramatic defeat of a magical instrument I\'ve ever seen."\n\n'
        'The trumpet is permanently muffled. Your crew can come and go safely.\n\n'
        "(+4 points. The trumpet is silenced for good.)"
    )


def _use_silver_net_on_salmon(state, item, target):
    state.set_flag("caught_salmon")
    state.score += 4
    from .levels._shared import items as shared_items
    salmon = shared_items.get("wisdom_salmon")
    if salmon and salmon not in state.inventory:
        state.inventory.append(salmon)
    return (
        'You cast the Silver Net into the crystal stream. It shimmers as it sinks, glowing '
        'like moonlight trapped in water.\n\n'
        'The salmon are not fooled. They dart away, laughing \u2014 actually laughing \u2014 '
        'as the net descends.\n\n'
        'But one salmon \u2014 the oldest, the wisest, the one with eyes that hold the age of the world \u2014 '
        'swims directly into the net. It does not struggle.\n\n'
        '"Finally," it says. "I was wondering when someone would bring the right tool. '
        'Being the wisest fish in the sea is exhausting. Every other fish asks me for advice. '
        'Constant questions. \'Is this current safe?\' \'Should I swim upstream or downstream?\' '
        '\'Do I look fat in these scales?\' I need a vacation."\n\n'
        'You pull the net up. The Wisdom Salmon flops into your hands, sighs deeply, '
        'and says: "Fine. Eat me. Gain all knowledge. Just... let me finish my thought first. '
        'I was composing a poem about the meaning of existence. It was going to be magnificent."\n\n'
        'The Salmon of Wisdom is now in your inventory. You feel smarter just holding it.\n\n'
        '(+4 points. The Wisdom Salmon is yours.)'
    )


def _use_silver_net_on_fish(state, item, target):
    state.score += 2
    state.set_flag("golden_fish_caught")
    return (
        'You cast the Silver Net into the water, and it shimmers as it descends — '
        'not sinking, but floating downward like a ghost made of moonlight.\n\n'
        'The net catches the golden fish. It doesn\'t struggle. In fact, it '
        'seems almost relieved, as if being caught was the only thing it had '
        'been waiting for.\n\n'
        'You pull it up. The golden fish gleams in the sunlight, its scales '
        'catching every colour of the rainbow. It\'s solid gold. Very, very heavy.\n\n'
        "(+2 points. The Golden Fish is yours! It's probably worth something.)"
    )


def _use_glass_shard_on_bridge(state, item, target):
    state.set_flag("bridge_tested")
    state.score += 2
    return (
        'You use the shard to test the glass bridge. Tapping it gently, you hear '
        'a clear, resonant ping that echoes across the chasm. The bridge seems solid.\n\n'
        'But as you watch, the shard suddenly vibrates in your hand and emits a '
        'single word in a voice like breaking ice: "SAFE."\n\n'
        'Then it goes quiet. The glass bridge glitters innocently.\n\n'
        "(+2 points. The bridge is safe to cross. The shard has spoken.)"
    )


def _use_laughing_potion_on_water_horse(state, item, target):
    state.set_flag("horse_laughing")
    state.score += 4
    return (
        'The kelpie drinks the potion and starts laughing. At first it\'s a '
        'horse laugh — a whinnying, snorting thing. But then it grows deeper, '
        'more human, more unhinged. The Water Horse rolls onto its back, '
        'hooves kicking the air, absolutely losing its equine mind.\n\n'
        '"I CAN\'T STOP! HA HA HA! I WAS GOING TO DROWN YOU AND EAT YOUR SOUL '
        'BUT NOW I CAN\'T STOP LAUGHING! THIS IS THE BEST DAY OF MY AFTERLIFE!"\n\n'
        'It laughs so hard that it can\'t maintain its magical footing and '
        'sinks into the sea, still cackling. The waters quiet down.\n\n'
        "The danger has passed — drowned in giggles.\n\n"
        "(+4 points. The Water Horse is neutralised by comedy.)"
    )


def _use_fiery_ash_on_pigs(state, item, target):
    state.set_flag("fiery_pigs_pacified")
    state.score += 3
    return (
        'The pigs snort at the ash. They sniff it, snuffle it, and then — '
        'impossibly — they start rolling in it like dogs finding a particularly '
        'delicious patch of mud.\n\n'
        'The Fiery Ash extinguishes their flaming bristles with a sizzle. '
        'One by one, the pigs go from "raging inferno" to "slightly warm pig" '
        'to "confused, naked-looking pig."\n\n'
        'They grunt contentedly and wander off to find a real mud puddle.\n\n'
        "(+3 points. The pigs are no longer on fire. They seem grateful."
        " Or indifferent. It's hard to tell with pigs.)"
    )


def _use_silver_bell_on_storm(state, item, target):
    state.set_flag("storm_calmed")
    state.score += 3
    # Also works on sea monsters
    if hasattr(target, 'id') and target.id == "sea_monsters" or (isinstance(target, str) and "monster" in target.lower()):
        state.set_flag("sea_monster_defeated")
        return (
            'You ring the Silver Bell. Its pure, clear tone rings across the water. '
            'The monstrous hand pauses. The creature beneath the surface stirs, '
            'then slowly, impossibly, releases the boat.\n\n'
            'A massive head surfaces \u2014 a face of ancient scales and sorrowful eyes. '
            'It looks at you, blinks once, and sinks back into the depths without a sound.\n\n'
            'The sea is calm. The monster is gone. Your crew exhales as one.\n\n'
            "(+3 points. The sea monster was soothed by the bell's tone.)"
        )
    return (
        'You ring the Silver Bell. Its pure tone cuts through the howling wind '
        'like a blade through butter. The storm clouds part. The waves subside. '
        'The wind drops to a gentle breeze.\n\n'
        'Your crew stares at you in amazement. Conganchnes mutters, "Wish I\'d '
        'had one of those in the great storm of \'82."\n\n'
        'The sea is calm. For now.\n\n'
        "(+3 points. You have temporarily befriended the weather.)"
    )


def _use_magic_thread_on_mast(state, item, target):
    state.set_flag("thread_tied")
    state.score += 3
    return (
        'You tie the Magic Thread to the mast, just as the druid instructed. '
        'It glows softly and begins to hum — a low, resonant note that seems '
        'to harmonise with the wind itself.\n\n'
        'The thread tightens, then points forward, like a compass needle made '
        'of silk and starlight. Fergus whistles. "That\'s not normal navigation, '
        'Captain. That\'s... well, that\'s magic."\n\n'
        'The ship glides forward as if guided by an invisible hand.\n\n'
        "(+3 points. The Magic Thread will guide you through the mists.)"
    )


def _use_truth_ring_on_queen(state, item, target):
    state.set_flag("queen_truth_revealed")
    state.score += 4
    return (
        'You present the Truth Ring to the Queen. The moment her finger touches '
        'the silver band, her eyes go wide. Her perfect composure cracks — '
        'no, shatters.\n\n'
        '"I... I can\'t... the ring forces me to speak truth. I know not what '
        'I say!"\n\n'
        'She tries to pull it off, but it won\'t budge. She takes a deep breath.\n\n'
        '"Fine. You want the truth? This island is a prison. I am not a queen — '
        'I am a guardian. I keep travelers here because the sea beyond is '
        'more dangerous than any enchantment I could weave. The men who killed '
        'your father... they are not the monsters you seek. The real monsters '
        'lie where the sun sets."\n\n'
        'She collapses into her throne, exhausted. The ring falls from her '
        'finger, its work done.\n\n'
        "(+4 points. The truth is rarely pretty, but it's always useful.)"
    )


def _use_speaking_feather_on_sea_monster(state, item, target):
    state.set_flag("sea_monster_defeated")
    state.score += 5
    return (
        'You hold the Speaking Feather above the water and speak the words it whispers to you.\n\n'
        'The feather translates your speech into the ancient tongue of the deep ones. '
        'The monstrous hand pauses mid-grab. A huge, ancient face rises from the depths '
        '\u2014 eyes the size of shields, barnacles like old scars.\n\n'
        '"You speak?" it rumbles. The voice is like boulders rolling in an underwater cave. '
        '"No sailor has spoken to me in centuries. They always try to stab me first. '
        'It is... refreshing."\n\n'
        'You negotiate. The creature reveals it was driven here by a larger predator. '
        'You promise to ring the Silver Bell \u2014 if you had one \u2014 to mark safe passage. '
        'The monster agrees to let you pass.\n\n'
        '"Go, little speaker. The deep knows your name now. That is a rare thing."\n\n'
        'The creature sinks into the depths. The sea is calm once more.\n\n'
        "(+5 points. You spoke the language of the deep. The monster remembers you.)"
    )


def _use_speaking_feather_on_skull(state, item, target):
    state.set_flag("skull_questioned")
    state.score += 2
    return (
        'You hold the Speaking Feather to the Talking Skull\'s ear-hole. '
        'The feather whispers something \u2014 a sound so faint you can\'t quite catch it.\n\n'
        'But the skull can. Its jaw drops open.\n\n'
        '"By the gods! That\'s the password! I\'VE BEEN WAITING CENTURIES FOR SOMEONE '
        'TO SAY THAT!"\n\n'
        'The skull clatters its teeth in what might be a grin. "Ask me about your FATHER, '
        'about REVENGE, or about HOME. I\'ll answer truthfully. Then I can finally rest."\n\n'
        '(Try: TALK TO SKULL ABOUT FATHER, TALK TO SKULL ABOUT REVENGE, '
        'or TALK TO SKULL ABOUT HOME)'
    )


def _use_hermit_blessing_on_serpent(state, item, target):
    state.set_flag("serpent_blessed")
    state.score += 3
    return (
        'You hold the Hermit\'s Blessing before the great serpent. It recoils '
        'at first, hissing, but then — impossibly — it lowers its head.\n\n'
        'The wooden cross glows with a soft, warm light. The serpent\'s '
        'venomous fangs retract. Its scales change from poisonous green to a '
        'peaceful blue.\n\n'
        '"The blessing of the holy man," the serpent whispers. "I have not felt '
        'its warmth since I was but a hatchling. Thank you, Mael Duin."\n\n'
        'It coils peacefully and allows you to pass.\n\n'
        "(+3 points. Even serpents need blessings sometimes.)"
    )


# --- Register specific use combos ---

_register_use("earplugs", "trumpet", _use_earplugs_on_trumpet)
_register_use("trumpet_muffler", "trumpet", _use_trumpet_muffler_on_trumpet)
_register_use("trumpet_muffler", "giant trumpet", _use_trumpet_muffler_on_trumpet)
_register_use("silver_net", "crystal_pillar_fish", _use_silver_net_on_fish)
_register_use("silver_net", "salmon", _use_silver_net_on_salmon)
_register_use("silver_net", "wisdom salmon", _use_silver_net_on_salmon)
_register_use("glass_shard", "glass_bridge", _use_glass_shard_on_bridge)
_register_use("laughing_potion", "water_horse", _use_laughing_potion_on_water_horse)
_register_use("fiery_ash", "fiery_pigs", _use_fiery_ash_on_pigs)
_register_use("fiery_ash", "pigs", _use_fiery_ash_on_pigs)
_register_use("fiery_ash", "pig", _use_fiery_ash_on_pigs)
_register_use("silver_bell", "storm", _use_silver_bell_on_storm)
_register_use("magic_thread", "mast", _use_magic_thread_on_mast)
_register_use("truth_ring", "queen", _use_truth_ring_on_queen)
_register_use("speaking_feather", "skull", _use_speaking_feather_on_skull)
_register_use("hermit_blessing", "serpent", _use_hermit_blessing_on_serpent)
_register_use("silver_bell", "sea_monsters", _use_silver_bell_on_storm)
_register_use("silver_bell", "sea monster", _use_silver_bell_on_storm)
_register_use("speaking_feather", "sea_monsters", _use_speaking_feather_on_sea_monster)
_register_use("speaking_feather", "sea monster", _use_speaking_feather_on_sea_monster)

# Also allow use by display name
_register_use("earplugs", "giant trumpet", _use_earplugs_on_trumpet)
_register_use("silver_net", "golden fish", _use_silver_net_on_fish)
_register_use("silver_net", "golden pillar fish", _use_silver_net_on_fish)
_register_use("silver_bell", "stormy weather", _use_silver_bell_on_storm)
_register_use("silver_bell", "waves", _use_silver_bell_on_storm)
_register_use("magic_thread", "ship", _use_magic_thread_on_mast)
_register_use("magic_thread", "curragh", _use_magic_thread_on_mast)
_register_use("truth_ring", "the queen", _use_truth_ring_on_queen)
_register_use("speaking_feather", "the talking skull", _use_speaking_feather_on_skull)
_register_use("hermit_blessing", "the great serpent", _use_hermit_blessing_on_serpent)
_register_use("hermit_blessing", "giant serpent", _use_hermit_blessing_on_serpent)

# ---- MISSING ISLANDS USE HANDLERS ----


def _use_heavy_item_on_gears(state, item, target):
    """Stop the Mill of the Sea by jamming a heavy item into the gears."""
    if state.has_flag("mill_stopped"):
        return "The mill is already stopped. The gears are frozen in place, a heavy object wedged between their teeth."

    # Heavy items that can jam the gears
    heavy_items = {"millstone_fragment", "fiery_ash", "golden_apple", "crystal_pillar_fish", "dragon_tooth", "demon_coin"}
    if item.id not in heavy_items:
        return (
            f"You throw the {item.name} into the gears. The great wheels chew it up "
            f"and grind on, unperturbed. Your item is destroyed.\n\n"
            "You need something heavier — something that can actually jam the mechanism."
        )

    state.set_flag("mill_stopped")
    state.score += 5
    from .levels._shared import items as shared_items
    grain = shared_items.get("ever_grinding_grain")
    if grain and grain not in state.inventory:
        state.inventory.append(grain)
    return (
        f"You hurl the {item.name} into the massive gears! It strikes with a deafening CRUNCH.\n\n"
        "The mill shudders. The great wheels grind to a halt, metal screaming against metal. "
        "With a final, groaning sigh, the mill falls silent.\n\n"
        "The silence is profound. Your crew cheers. The old guardian emerges from the shadows, "
        "tears streaming down his flour-dusted face.\n\n"
        "'Sixty years,' he whispers. 'Sixty years of grinding. And now... silence.'\n\n"
        "Where the millstone was grinding, a hidden compartment has been revealed — "
        "a small alcove filled with golden grain. It glows with a soft, warm light.\n\n"
        "You take a handful of the Ever-Grinding Grain — a grain that multiplies endlessly.\n\n"
        f"(+5 points. Gained: Ever-Grinding Grain)"
    )


def _use_magic_thread_on_mast_wall(state, item, target):
    """Use the Magic Thread on the mast to calm the Wall of Water."""
    if state.has_flag("wall_crossed"):
        return "The wall has already collapsed. The sea is calm."
    if state.current_location != "wall_of_water":
        return "You are not at the Wall of Water."
    state.set_flag("wall_crossed")
    state.score += 3
    return (
        "You untie the Magic Thread from the mast and hold it before the Wall of Water.\n\n"
        "The thread glows with sudden, brilliant light — a silver fire that pulses in rhythm with your heartbeat. "
        "It stretches toward the wall, touching it gently.\n\n"
        "For a moment, nothing happens. Then the wall begins to sing — a deep, resonant note "
        "that vibrates in your chest. The water parts, drawing aside like a curtain.\n\n"
        "A path opens through the wall. On the other side, the sea is calm and clear.\n\n"
        "Your crew stares in awe. Fergus crosses himself. 'The druid's thread... it was meant for this.'\n\n"
        "(+3 points. The Wall of Water is parted. You may now pass.)"
    )


def _use_silver_bell_on_wall(state, item, target):
    """Use the Silver Bell to calm the Wall of Water."""
    if state.has_flag("wall_crossed"):
        return "The wall has already collapsed. The sea is calm."
    if state.current_location != "wall_of_water":
        return "You are not at the Wall of Water."
    state.set_flag("wall_crossed")
    state.score += 3
    return (
        "You ring the Silver Bell before the Wall of Water. A pure, clear note rings out across the sea.\n\n"
        "The wall shivers. Ripples race across its surface — thousands of them — like a struck gong made of water. "
        "The humming changes pitch, rising higher and higher, until...\n\n"
        "The wall collapses. Not violently — but gently, gracefully, like a dancer bowing at the end of a performance. "
        "Millions of tons of water fall into the sea, creating a wave that lifts your curragh and sets it down gently.\n\n"
        "The sea is calm once more. The way is clear.\n\n"
        "Diurán wipes his brow. 'I'll put that in the poem. Definitely.'\n\n"
        "(+3 points. The Wall of Water is calmed.)"
    )


def _use_speaking_feather_on_oxen(state, item, target):
    """Use the Speaking Feather to communicate with the Sacred Oxen."""
    if state.has_flag("oxen_peaceful") or state.has_flag("oxen_slaughtered"):
        return "The oxen have already given their answer."
    state.set_flag("oxen_peaceful")
    state.score += 3
    from .levels._shared import items as shared_items
    horn = shared_items.get("golden_horn")
    if horn and horn not in state.inventory:
        state.inventory.append(horn)
    return (
        "You hold the Speaking Feather before the Sacred Oxen. It whispers — "
        "and the oxen's ears pivot forward.\n\n"
        "The larger ox lows, and the feather translates:\n\n"
        "'You carry the voice of the ancient birds. You are welcome here, Mael Duin. "
        "We have guarded this horn since before your people learned to sail. "
        "But the time of guarding is over. Take it — use it wisely. When you blow the Golden Horn, "
        "we will hear it, even across the sea.'\n\n"
        "The ox lowers its head, and the golden horn slides free — a gift, willingly given.\n\n"
        "(+3 points. Gained: Golden Horn)"
    )


def _use_silver_bell_on_horses(state, item, target):
    """Use the Silver Bell to calm the Giant Horses."""
    if state.has_flag("horses_pacified"):
        return "The horses are already calm."
    if state.current_location != "island_horses":
        return "There are no giant horses here."
    state.set_flag("horses_pacified")
    state.score += 3
    return (
        "You ring the Silver Bell. A pure, clear note rings out across the island.\n\n"
        "The giant horses freeze. Their ears swivel toward the sound. The Stallion King "
        "turns his massive head, and for a long moment, there is silence.\n\n"
        "Then the Stallion King walks toward you — not aggressively, but curiously. "
        "He stops before you and bows his head. The herd follows suit, lowering their heads in unison.\n\n"
        "The Stallion King nuzzles your hand. You reach up and touch his mane — "
        "and a single strand of it comes away in your hand, weaving itself into a bridle.\n\n"
        "The Stallion King meets your eyes. His meaning is clear: 'Ride well, little one. "
        "This bridle will carry you across the waves faster than any wind.'\n\n"
        "(+3 points. Gained: Horsehair Bridle)"
    )


def _use_otter_pelt_on_horses(state, item, target):
    """Use the Otter Pelt to earn the trust of the Giant Horses."""
    if state.has_flag("horses_pacified"):
        return "The horses are already calm."
    if state.current_location != "island_horses":
        return "There are no giant horses here."
    state.set_flag("horses_pacified")
    state.score += 3
    from .levels._shared import items as shared_items
    bridle = shared_items.get("horsehair_bridle")
    if bridle and bridle not in state.inventory:
        state.inventory.append(bridle)
    return (
        "You hold out the Otter Pelt. The smell of sea and animal reaches the Stallion King's nostrils.\n\n"
        "He snorts — a sound that might be surprise, might be recognition. He walks toward you "
        "and sniffs the pelt thoroughly. His ears relax. His stance softens.\n\n"
        "He lowers his head and, with surprising gentleness, rubs his cheek against the pelt. "
        "The herd follows, snorting and stamping in what seems like approval.\n\n"
        "A single strand of the Stallion King's mane drifts down and weaves itself into a bridle "
        "at your feet. A gift — freely given.\n\n"
        "The Stallion King meets your eyes: 'You understand the old ways. This bridle is yours.'\n\n"
        "(+3 points. Gained: Horsehair Bridle)"
    )


# ---- MISSING ISLANDS USE REGISTRATIONS ----
# Mill of the Sea — heavy items on gears
_register_use("millstone_fragment", "gears", _use_heavy_item_on_gears)
_register_use("fiery_ash", "gears", _use_heavy_item_on_gears)
_register_use("golden_apple", "gears", _use_heavy_item_on_gears)
_register_use("crystal_pillar_fish", "gears", _use_heavy_item_on_gears)
_register_use("dragon_tooth", "gears", _use_heavy_item_on_gears)
_register_use("demon_coin", "gears", _use_heavy_item_on_gears)
_register_use("millstone_fragment", "mill", _use_heavy_item_on_gears)
_register_use("millstone_fragment", "wheel", _use_heavy_item_on_gears)
_register_use("millstone_fragment", "millstone", _use_heavy_item_on_gears)
# Also use on the millstone by name
_register_use("fiery_ash", "mill", _use_heavy_item_on_gears)
_register_use("golden_apple", "mill", _use_heavy_item_on_gears)

# ---- REVOLVING CASTLE PUZZLE ----
def _use_revolving_key_on_castle(state, item, target):
    if state.current_location != "island_revolving_castle":
        return "You're not at the Revolving Castle."
    if state.has_flag("castle_unlocked"):
        return "The castle is already unlocked. The doors have frozen in place."
    state.set_flag("castle_unlocked")
    state.score += 3
    return (
        "You insert the Revolving Key into the lock of the Red Door just as it aligns with the platform.\n\n"
        "The key turns with a satisfying CLICK. The castle shudders — a deep, groaning sound — "
        "and slowly, ponderously, it stops revolving.\n\n"
        "The Red Door swings open, revealing a dark entrance hallway beyond. The other doors freeze mid-position.\n\n"
        "The castle is still. For the first time in centuries, the turning world has stopped.\n\n"
        "Diurán whispers: 'You stopped a castle. That\\'s going in the poem.'\n\n"
        "(+3 points. The Revolving Castle is now open.)"
    )
_register_use("revolving_key", "door", _use_revolving_key_on_castle)
_register_use("revolving_key", "castle", _use_revolving_key_on_castle)
_register_use("revolving_key", "gate", _use_revolving_key_on_castle)
_register_use("revolving_key", "red door", _use_revolving_key_on_castle)
_register_use("revolving_key", "keyhole", _use_revolving_key_on_castle)

# Wall of Water — magic thread or silver bell
_register_use("magic_thread", "mast", _use_magic_thread_on_mast_wall)
_register_use("magic_thread", "wall", _use_magic_thread_on_mast_wall)
_register_use("magic_thread", "water", _use_magic_thread_on_mast_wall)
_register_use("silver_bell", "wall", _use_silver_bell_on_wall)
_register_use("silver_bell", "water", _use_silver_bell_on_wall)
_register_use("magic_thread", "curragh", _use_magic_thread_on_mast_wall)
_register_use("magic_thread", "ship", _use_magic_thread_on_mast_wall)

# Giant Horses — silver bell or otter pelt
_register_use("silver_bell", "horses", _use_silver_bell_on_horses)
_register_use("silver_bell", "stallion", _use_silver_bell_on_horses)
_register_use("silver_bell", "king", _use_silver_bell_on_horses)
_register_use("silver_bell", "horse", _use_silver_bell_on_horses)
_register_use("otter_pelt", "horses", _use_otter_pelt_on_horses)
_register_use("otter_pelt", "stallion", _use_otter_pelt_on_horses)
_register_use("otter_pelt", "horse", _use_otter_pelt_on_horses)

# Sacred Oxen — speaking feather
_register_use("speaking_feather", "oxen", _use_speaking_feather_on_oxen)
_register_use("speaking_feather", "ox", _use_speaking_feather_on_oxen)
_register_use("speaking_feather", "bull", _use_speaking_feather_on_oxen)
_register_use("speaking_feather", "sacred oxen", _use_speaking_feather_on_oxen)

# ---- MISSING ISLANDS 2 USE HANDLERS ----


def _use_sharp_item_on_fish_belly(state, item, target):
    """Cut your way out of the Great Fish using a sharp item."""
    if state.has_flag("escaped_fish"):
        return "You are already free of the Great Fish."
    if state.current_location != "great_fish_belly":
        return "There is no fish belly here to cut through."
    state.set_flag("escaped_fish")
    state.score += 4
    state.current_location = "great_fish_carcass"
    from .levels._shared import items as shared_items
    tooth = shared_items.get("fish_tooth")
    if tooth and tooth not in state.inventory:
        state.inventory.append(tooth)
    return (
        "You take the sharp item and drive it deep into the pulsing wall of the fish's belly!\\\n\\\n"
        "The creature convulses. The walls contract around you, squeezing — but you hold on, "
        "cutting, slashing, tearing through flesh and sinew.\\\n\\\n"
        "Light pours through the wound — pale, grey, beautiful light. The sea. The sky. Freedom.\\\n\\\n"
        "You tumble out onto the fish's back, gasping for air. Your crew follows, one by one, "
        "covered in slime but alive.\\\n\\\n"
        "Between the fish's gaping jaws, you spot a massive serrated tooth. You prise it free.\\\n\\\n"
        "(+4 points. Gained: Fish Tooth. The Great Fish is dead; you are free.)"
    )


def _use_fiery_ash_on_fish_belly(state, item, target):
    """Burn your way out of the Great Fish."""
    if state.has_flag("escaped_fish"):
        return "You are already free of the Great Fish."
    if state.current_location != "great_fish_belly":
        return "There is no fish belly here to burn."
    state.set_flag("escaped_fish")
    state.score += 4
    state.current_location = "great_fish_carcass"
    from .levels._shared import items as shared_items
    tooth = shared_items.get("fish_tooth")
    if tooth and tooth not in state.inventory:
        state.inventory.append(tooth)
    return (
        "You scatter the Fiery Ash against the fish's inner wall. The embers catch — "
        "the wet flesh sizzles and blackens, then bursts into flame.\\\n\\\n"
        "The fish shudders violently. The fire spreads, eating through the blubber and muscle. "
        "Your crew presses against the far wall as the heat intensifies.\\\n\\\n"
        "Then — a roar, a shudder, and the wall collapses outward. You fall through into daylight, "
        "landing on the fish's smoldering back.\\\n\\\n"
        "The Great Fish is dead, roasted from the inside. Its jaws hang open, revealing "
        "a single massive tooth. You take it as a trophy.\\\n\\\n"
        "(+4 points. Gained: Fish Tooth. You burned your way to freedom.)"
    )


def _use_fountain_water_on_crew(state, item, target):
    """Heal a crew member using Fountain Water."""
    if not state.total_crew_alive() == 3:
        # Check if there are injured/dying crew to heal
        pass
    state.score += 3
    state.set_flag("fountain_water_used")
    return (
        "You pour the milk-white Fountain Water onto the crew member's wounds. "
        "The water glows brightly, and the injuries seal themselves — cuts close, "
        "bruises fade, and the color returns to their face.\\\n\\\n"
        "They sit up, blinking. 'What... what was that? I feel like I just slept "
        "for a week. And had a really good dream about a cow.'\\\n\\\n"
        "The Fountain Water has done its work. Your crew member is healed.\\\n\\\n"
        "(+3 points. The Fountain Water works its healing magic.)"
    )


def _use_silent_bell_on_creature(state, item, target):
    """Calm any creature with the Silent Bell."""
    state.set_flag("bell_rang_silently")
    state.score += 3
    return (
        "You ring the Silent Bell. No sound emerges — but everything around you STILLS.\\\n\\\n"
        "The creature before you freezes mid-motion. Its eyes go wide, then soften. "
        "Its aggression drains away like water from a cracked vessel.\\\n\\\n"
        "It sits down, docile and calm, as if the very concept of violence has been "
        "removed from its mind. It looks at you with something like gratitude.\\\n\\\n"
        "The Silent Bell's power is strange — it does not silence sound, but silence "
        "the will to fight.\\\n\\\n"
        "(+3 points. The creature is calmed by the silent ringing.)"
    )


def _use_wind_of_return_on_ship(state, item, target):
    """Trigger the homecoming with the Wind of Return."""
    if state.has_flag("wind_used"):
        return "The Wind of Return has already carried you home."
    state.set_flag("wind_used")
    state.score += 5
    # Change location to the homecoming location
    from .engine import LOCATIONS
    if "homecoming" in LOCATIONS:
        state.current_location = "homecoming"
    return (
        "You unseal the Wind of Return. The bottle's wax seal breaks with a soft pop, "
        "and a warm, steady wind fills your sails. It carries a scent of turf smoke, "
        "fresh bread, and rain on green grass.\\\n\\\n"
        "The curragh leaps forward as if eager to be home. The grey sea blurs beneath you. "
        "The islands of wonder and terror shrink behind you.\\\n\\\n"
        "Your crew stands together at the prow, watching the horizon. Diurán is weeping. "
        "Fergus is laughing. Conganchnes is trying to look stoic but failing.\\\n\\\n"
        "The wind knows the way. The wind has always known the way.\\\n\\\n"
        "You are going home.\\\n\\\n"
        "(+5 points. The Wind of Return carries you homeward.)"
    )


# Register Level 06 USE combos
_register_use("glass_shard", "fish_belly", _use_sharp_item_on_fish_belly)
_register_use("glass_shard", "belly", _use_sharp_item_on_fish_belly)
_register_use("glass_shard", "fish", _use_sharp_item_on_fish_belly)
_register_use("magic_harpoon", "fish_belly", _use_sharp_item_on_fish_belly)
_register_use("magic_harpoon", "belly", _use_sharp_item_on_fish_belly)
_register_use("magic_harpoon", "fish", _use_sharp_item_on_fish_belly)
_register_use("fiery_ash", "fish_belly", _use_fiery_ash_on_fish_belly)
_register_use("fiery_ash", "belly", _use_fiery_ash_on_fish_belly)
_register_use("fiery_ash", "fish", _use_fiery_ash_on_fish_belly)
_register_use("fountain_water", "crew", _use_fountain_water_on_crew)
_register_use("fountain_water", "diuran", _use_fountain_water_on_crew)
_register_use("fountain_water", "conganchnes", _use_fountain_water_on_crew)
_register_use("fountain_water", "fergus", _use_fountain_water_on_crew)
_register_use("silent_bell", "sea_monsters", _use_silent_bell_on_creature)
_register_use("silent_bell", "sea monster", _use_silent_bell_on_creature)
_register_use("silent_bell", "monster", _use_silent_bell_on_creature)
_register_use("silent_bell", "creature", _use_silent_bell_on_creature)
_register_use("silent_bell", "beast", _use_silent_bell_on_creature)
_register_use("silent_bell", "horse", _use_silent_bell_on_creature)
_register_use("silent_bell", "horses", _use_silent_bell_on_creature)
_register_use("silent_bell", "stallion", _use_silent_bell_on_creature)
_register_use("silent_bell", "oxen", _use_silent_bell_on_creature)
_register_use("silent_bell", "ox", _use_silent_bell_on_creature)
_register_use("silent_bell", "serpent", _use_silent_bell_on_creature)
_register_use("silent_bell", "snake", _use_silent_bell_on_creature)
_register_use("silent_bell", "cat", _use_silent_bell_on_creature)
_register_use("silent_bell", "pig", _use_silent_bell_on_creature)
_register_use("wind_of_return", "ship", _use_wind_of_return_on_ship)
_register_use("wind_of_return", "curragh", _use_wind_of_return_on_ship)
_register_use("wind_of_return", "boat", _use_wind_of_return_on_ship)
_register_use("wind_of_return", "mast", _use_wind_of_return_on_ship)


# ---------------------------------------------------------------------------
# FALLBACK use responses  (item category × target type)
# ---------------------------------------------------------------------------

_USE_FALLBACKS = {}


def _use_item_on_self_fallback(state, item, target):
    cat = _item_category(item.id)
    texts = {
        "food": _r([
            "You consume the edible item. It tastes like adventure, with a "
            "slight aftertaste of regret. You feel slightly more alive.",
            "You eat it. It's... okay. Not great. But okay. Your stomach thanks you.",
        ]),
        "weapon": _r([
            "You wave the weapon around. Nothing happens. You look cool, though. "
            "At least, you think you look cool. Your crew is politely avoiding eye contact.",
            "You brandish the weapon heroically. A nearby seagull applauds sarcastically.",
        ]),
        "treasure": _r([
            "You admire the treasure. It's shiny. That's about it. "
            "You feel a brief moment of happiness that economists call 'the joy of acquisition.'",
            "You hold the treasure up. It gleams. You gleam back. It's a gleam-off.",
        ]),
        "tool": _r([
            "You use the tool on yourself. It doesn't seem designed for this purpose. "
            "You feel silly.",
            "You fidget with the tool. It doesn't do anything useful, but it keeps "
            "your hands busy while you think.",
        ]),
        "magical": _r([
            "You activate the magical item. It glows, flickers, and then... "
            "nothing. Maybe it needs a specific target?",
            "Magic surges through you! ...Or was that just static electricity? "
            "Hard to tell with Celtic magic.",
        ]),
        "material": _r([
            "You hold the raw material. It's very... material. You feel connected "
            "to the earth. And slightly dusty.",
            "You examine the material closely. It's exactly what it looks like. "
            "No hidden properties. Just stuff.",
        ]),
    }
    return texts.get(cat, "You use the item on yourself. Nothing happens. You feel foolish.")


def _use_item_on_npc_fallback(state, item, target):
    npc_id = getattr(target, 'id', 'unknown')
    pers = _npc_personality(npc_id)
    cat = _item_category(item.id)

    if pers == "wise":
        return _r([
            f'{target.name} watches you use the {item.name} with detached curiosity. '
            '"Fascinating. The mundane made ritual."',
            f'You show the {item.name} to {target.name}. They nod slowly. '
            '"Yes, yes. That is exactly what that does. Well done."',
        ])
    elif pers == "dangerous":
        return _r([
            f'You try to use the {item.name} on {target.name}. '
            f'{target.name} does not appreciate this. "Keep your {item.name} to yourself," they growl.',
            f'{target.name} backs away. "I don\'t know what you\'re doing, but stop it."',
        ])
    elif pers == "social":
        return _r([
            f'{target.name} observes your attempt to use the {item.name}. '
            '"Oh, I see! You\'re doing the thing. With the item. Very clever."',
            f'{target.name} politely ignores your use of the {item.name}. '
            'They\'ve clearly seen stranger things.',
        ])
    else:
        return _r([
            f'You use the {item.name} near {target.name}. They blink. '
            '"Was that supposed to impress me?"',
            f'{target.name} watches you. "Huh. I\'ve seen better."',
        ])


def _generic_use_fallback(state, item, target_name):
    cat = _item_category(item.id)
    target_str = target_name if isinstance(target_name, str) else getattr(target_name, 'name', 'it')
    return _r([
        f'You use the {item.name} on {target_str}. Nothing obvious happens. '
        'But the universe has taken note.',
        f'The {item.name} doesn\'t seem to work on {target_str}. '
        'Maybe try something else?',
        f'You attempt to use {item.name} with {target_str}. '
        'The result is... anticlimactic. The result is nothing.',
        f'{item.name} meets {target_str}. They do not get along. '
        'Nothing happens. Awkward silence ensues.',
    ])


# ---------------------------------------------------------------------------
# TALK TOPIC responses
# ---------------------------------------------------------------------------

_TOPIC_FALLBACKS = {}


def _topic_response_for_npc(npc_id, topic):
    """Return a string response for an NPC asked about a topic."""
    topic_lower = topic.lower().strip()

    # General topic categories
    topic_category = None
    if topic_lower in ("father", "dad", "ailill", "parent", "family"):
        topic_category = "father"
    elif topic_lower in ("vengeance", "revenge", "blood feud", "kill", "murder"):
        topic_category = "vengeance"
    elif topic_lower in ("sea", "ocean", "wave", "water", "sail", "voyage", "journey"):
        topic_category = "sea"
    elif topic_lower in ("home", "ireland", "return", "village"):
        topic_category = "home"
    elif topic_lower in ("forgiveness", "mercy", "peace", "let go"):
        topic_category = "forgiveness"
    elif topic_lower in ("death", "die", "dead", "afterlife"):
        topic_category = "death"
    elif topic_lower in ("advice", "wisdom", "help", "guidance"):
        topic_category = "advice"
    elif topic_lower in ("love", "woman", "women", "romance"):
        topic_category = "love"
    elif topic_lower in ("god", "gods", "prayer", "faith", "belief"):
        topic_category = "god"
    elif topic_lower in ("monster", "monsters", "creature", "beast"):
        topic_category = "monster"
    elif topic_lower in ("treasure", "gold", "wealth", "riches"):
        topic_category = "treasure"
    elif topic_lower in ("story", "tale", "legend", "myth"):
        topic_category = "story"

    # Check NPC-specific topic overrides
    npc_pers = _npc_personality(npc_id)
    key = (npc_id, topic_category)
    if key in _TOPIC_FALLBACKS:
        return _TOPIC_FALLBACKS[key]

    # Generic personality-based topic responses
    pers_key = (npc_pers, topic_category)
    if pers_key in _TOPIC_FALLBACKS:
        return _TOPIC_FALLBACKS[pers_key]

    # Ultra-generic
    return None


# Wise NPC topic responses
def _wise_on_advice():
    return _r([
        '"The best advice I can give is free: breathe. The second best advice '
        'will cost you a goat."',
        '"Advice is like a stone — heavy, plentiful, and useful only if you '
        'know where to place it."',
        '"Listen to the wind. It knows things that people have forgotten."',
    ])


def _wise_on_forgiveness():
    return _r([
        '"Forgiveness is not for them. It is for you. Carrying a grudge is '
        'like drinking poison and expecting the other person to die."',
        '"The tree that bends in the storm survives. The tree that refuses '
        'to bend... makes excellent firewood."',
    ])


def _wise_on_father():
    return _r([
        '"Your father was a man, as you are a man. He made choices, as you '
        'make choices. The difference is that his story has ended, and yours '
        'is still being written."',
        '"A father is not the sum of his death, but the sum of his life. '
        'Remember him for his laugh, not his last breath."',
    ])


def _wise_on_sea():
    return _r([
        '"The sea is a mirror. It reflects not your face, but your soul. '
        'Look into it carefully."',
        '"Every wave is a moment. Every tide is a lifetime. The sea teaches '
        'patience by taking everything and giving it back on its own schedule."',
    ])


# Dangerous NPC topic responses
def _dangerous_on_vengeance():
    return _r([
        '"Vengeance? Oh, I LOVE vengeance. It\'s like a warm meal you eat cold '
        '— still satisfying, but you kind of wish you\'d eaten it sooner."',
        '"Revenge is great. I do it every Tuesday. Tuesdays are vengeance days. '
        'Followed by leftovers on Wednesday."',
    ])


def _dangerous_on_death():
    return _r([
        '"Death? I\'m not afraid of death. I\'m afraid of dying BORED. They\'re '
        'very different things."',
        '"Death comes for everyone. I plan to make it work for it."',
    ])


def _dangerous_on_advice():
    return _r([
        '"My advice? Don\'t die. That\'s it. That\'s all the advice I have. '
        'Everything else is negotiable."',
        '"Advice? Sure. Never trust a horse that offers you a ride. '
        'Especially if it smiles."',
    ])


# Social NPC topic responses
def _social_on_love():
    return _r([
        '"Love is like a good stew — it takes time, patience, and the right '
        'ingredients. Also, too many cooks spoil it."',
        '"Love? I married mine. Best decision I ever made. Second best was '
        'buying a bigger bed."',
    ])


def _social_on_treasure():
    return _r([
        '"Treasure is lovely, but it can\'t hug you back. Unless it\'s a '
        'very specific kind of treasure, in which case you should probably '
        'put it down."',
        '"Gold? Overrated. Now, a good cheese plate — THAT\'S treasure."',
    ])


def _social_on_story():
    return _r([
        '"Every person is a story. Some are epics. Some are limericks. '
        'Some are shopping lists that accidentally became interesting."',
        '"I love a good story. The best ones have dragons. Or at least '
        'a dragon-adjacent creature."',
    ])


# Register topic fallbacks

# Wise NPCs
for npc_id in WISE_NPCS:
    _TOPIC_FALLBACKS[(npc_id, "advice")] = _wise_on_advice
    _TOPIC_FALLBACKS[(npc_id, "forgiveness")] = _wise_on_forgiveness
    _TOPIC_FALLBACKS[(npc_id, "father")] = _wise_on_father
    _TOPIC_FALLBACKS[(npc_id, "sea")] = _wise_on_sea
    _TOPIC_FALLBACKS[(npc_id, "death")] = lambda: _r([
        '"Death is but a door. And doors can be opened from both sides — '
        'though most people only try it once."',
        '"The dead are not gone. They are just fishing on a different river."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "home")] = lambda: _r([
        '"Home is not a place. It is a feeling. You carry it with you."',
        '"You can never go home again. But you can find a new one."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "god")] = lambda: _r([
        '"The gods are real. I\'ve met a few. They\'re just as confused as we are."',
        '"Pray if it helps. The universe listens, even if it doesn\'t always reply."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "monster")] = lambda: _r([
        '"The greatest monsters are the ones we carry inside us. '
        'The ones outside are just... practice."',
        '"Monsters are just misunderstood creatures. Except the ones that '
        'eat people. Those are correctly understood."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "vengeance")] = lambda: _r([
        '"Vengeance is a cup that empties the drinker. I have seen strong '
        'men drink from it and become hollow shells."',
        '"The path of revenge is a spiral. The further you walk, the further '
        'you are from where you started."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "treasure")] = lambda: _r([
        '"The greatest treasure is not gold or jewels. It is a clear conscience '
        'and a warm fire."',
        '"Treasure? I have all I need. The rest is just clutter."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "story")] = lambda: _r([
        '"Every journey is a story. Every story is a journey. You are writing yours with every step."',
        '"The best stories are the ones that change the teller."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "love")] = lambda: _r([
        '"Love is the one magic that requires no ingredients, no spells, '
        'and no permission."',
        '"Love and wisdom are the same thing, seen from different angles."',
    ])

# Dangerous NPCs
for npc_id in DANGEROUS_NPCS:
    _TOPIC_FALLBACKS[(npc_id, "vengeance")] = _dangerous_on_vengeance
    _TOPIC_FALLBACKS[(npc_id, "death")] = _dangerous_on_death
    _TOPIC_FALLBACKS[(npc_id, "advice")] = _dangerous_on_advice
    _TOPIC_FALLBACKS[(npc_id, "monster")] = lambda: _r([
        '"Monsters? I\'m standing right here, pal."',
        '"I know a thing or two about monsters. Rule one: don\'t make eye contact. '
        'Rule two: if you do, make sure you\'re the scarier one."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "treasure")] = lambda: _r([
        '"Treasure? I have treasure. It\'s MINE. You can look at it from over there."',
        '"Shiny things. I like shiny things. Give me your shiny things. '
        'Now."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "forgiveness")] = lambda: _r([
        '"Forgiveness? I don\'t forgive. I forget. There\'s a difference."',
        '"You want forgiveness? Ask someone who isn\'t me. I hold grudges '
        'like a dragon holds gold."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "sea")] = lambda: _r([
        '"The sea is cold, wet, and full of things that want to eat you. '
        'What more do you need to know?"',
        '"I don\'t trust the sea. It moves too much. Solid ground is where '
        'it\'s at."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "father")] = lambda: _r([
        '"My father? Dead. Killed by a man who asked too many questions. '
        'I\'m the man who asked too many questions."',
        '"Fathers. Can\'t live with them, can\'t bury them without a proper ceremony."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "home")] = lambda: _r([
        '"Home is where the hoard is."',
        '"Home? I ate my home. It was delicious."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "story")] = lambda: _r([
        '"I have a story. It involves blood, fire, and a very confused bard. '
        'I\'ll charge you for the full version."',
        '"Stories are like teeth — best when sharp and few."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "love")] = lambda: _r([
        '"Love is a weakness. But so is not loving. Can\'t win either way."',
        '"I loved once. Then I ate them. True story."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "god")] = lambda: _r([
        '"The gods fear me. Or they would, if they knew where I lived."',
        '"Gods? Overrated. I could take a god in a fight. Maybe. On a good day."',
    ])

# Social NPCs
for npc_id in SOCIAL_NPCS:
    _TOPIC_FALLBACKS[(npc_id, "love")] = _social_on_love
    _TOPIC_FALLBACKS[(npc_id, "treasure")] = _social_on_treasure
    _TOPIC_FALLBACKS[(npc_id, "story")] = _social_on_story
    _TOPIC_FALLBACKS[(npc_id, "advice")] = lambda: _r([
        '"My advice? Always carry a spare pair of socks. And a knife. '
        'You never know which one you\'ll need first."',
        '"The secret to a happy life is low expectations and a good sense '
        'of humour."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "sea")] = lambda: _r([
        '"The sea? It\'s big. It\'s wet. It\'s full of fish. What else is there to say?"',
        '"I prefer dry land. Land doesn\'t try to drown you."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "father")] = lambda: _r([
        '"My father told me: \'Son, if you\'re going to do something stupid, '
        'at least make it a good story.\' Best advice he ever gave me."',
        '"Family is complicated. Like a stew with too many ingredients. '
        'Still edible, but you question every bite."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "forgiveness")] = lambda: _r([
        '"Forgiveness is free. But it costs you your pride. Some people aren\'t willing to pay."',
        '"I forgive easily. I forget even faster. It\'s a blessing and a curse."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "home")] = lambda: _r([
        '"Home is where they have to take you in. It\'s in the rules."',
        '"I miss home. But the adventure is worth the homesickness."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "death")] = lambda: _r([
        '"Death is a part of life. Like taxes. Or bad poetry."',
        '"I plan to live forever. So far, so good."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "vengeance")] = lambda: _r([
        '"Vengeance is a young man\'s game. I prefer a good nap."',
        '"Revenge? Too much effort. I\'d rather just outlive my enemies."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "monster")] = lambda: _r([
        '"Monsters are just people with bad reputations. And extra teeth."',
        '"I\'ve met monsters. Most of them are just lonely."',
    ])
    _TOPIC_FALLBACKS[(npc_id, "god")] = lambda: _r([
        '"I pray to the gods of good weather and full bellies. '
        'They\'ve never let me down."',
        '"The gods? I\'m on speaking terms with a few. They owe me money."',
    ])

# Neutral NPC topic responses (fallback for any NPC not in wise/dangerous/social)
_TOPIC_FALLBACKS[("neutral", "advice")] = lambda: _r([
    '"I don\'t give advice. I give opinions. They\'re worth what you "'
    "paid for them.",
    '"My advice? Don\'t take advice from strangers. Unless the stranger "'
    "is me. In which case, definitely take my advice.",
])
_TOPIC_FALLBACKS[("neutral", "father")] = lambda: _r([
    '"I knew a man once. He had a son. The son went on a voyage. "'
    'That\'s all I know."',
    '"Fathers are like lighthouses. They guide you, but you still have "'
    "to steer the ship yourself.",
])
_TOPIC_FALLBACKS[("neutral", "sea")] = lambda: _r([
    '"The sea is salty. Like my mood after a long voyage."',
    '"The sea doesn\'t care about your plans. It has its own."',
])
_TOPIC_FALLBACKS[("neutral", "home")] = lambda: _r([
    '"They say you can\'t go home again. I say you can, but the door '
    'might be locked."',
    '"Home. Where the heart is. Or where the food is. One of those."',
])
_TOPIC_FALLBACKS[("neutral", "forgiveness")] = lambda: _r([
    '"Forgiveness is like cleaning a wound. It hurts, but it heals."',
    '"I forgive, but I have a very good memory."',
])
_TOPIC_FALLBACKS[("neutral", "death")] = lambda: _r([
    '"Death is the final frontier. Or the final nap. I forget which."',
    '"Everyone dies. The trick is to do it at the very end."',
])
_TOPIC_FALLBACKS[("neutral", "vengeance")] = lambda: _r([
    '"Vengeance is a dish best served cold. But I prefer my dishes hot. '
    'Decision-making crisis."',
    '"Revenge is a circle. Best not to step into it."',
])
_TOPIC_FALLBACKS[("neutral", "treasure")] = lambda: _r([
    '"Treasure is nice. But try spending it when you\'re stranded on a rock."',
    '"I\'d rather have a full belly than a full purse."',
])
_TOPIC_FALLBACKS[("neutral", "story")] = lambda: _r([
    '"Every person has a story. Most are boring. Yours seems okay so far."',
    '"I like stories with happy endings. Or at least endings that involve pie."',
])
_TOPIC_FALLBACKS[("neutral", "love")] = lambda: _r([
    '"Love is like the sea. It can be calm and beautiful, or it can "'
    "drown you.",
    '"I loved once. Then they ate the last piece of bread. It was over."',
])
_TOPIC_FALLBACKS[("neutral", "god")] = lambda: _r([
    '"I believe in the god of getting through the day without dying. "'
    'So far, so good."',
    '"The gods work in mysterious ways. Mostly by not showing up when '
    'you need them."',
])
_TOPIC_FALLBACKS[("neutral", "monster")] = lambda: _r([
    '"Monsters are real. But so are heroes. The ratio is what matters."',
    '"I\'ve seen things that would make your hair stand on end. '
    'Fortunately, I\'m bald."',
])


# ---------------------------------------------------------------------------
# PUBLIC API
# ---------------------------------------------------------------------------


def get_give_response(state, item, npc):
    """Return a string describing what happens when item is given to npc.

    Checks:
      1. Specific (item_id, npc_id) combo.
      2. "everlasting_fruit" → any NPC (special universal handler).
      3. Category × personality fallback.
    """
    # 1. Specific combo
    item_specifics = _SPECIFIC_GIVE.get(item.id, {})
    if npc.id in item_specifics:
        return item_specifics[npc.id](state, item, npc)

    # 1b. "any NPC" wildcard handler for this item
    if "__any__" in item_specifics:
        return item_specifics["__any__"](state, item, npc)

    # 2. Everlasting fruit to any NPC
    if item.id == "everlasting_fruit":
        return _give_everlasting_fruit_to_any(state, item, npc)

    # 3. Fallback by category × personality
    fallback_fn = _get_fallback_give(item, npc)
    return fallback_fn(state, item, npc)


def get_use_response(state, item, target):
    """Return a string describing what happens when item is used with target.

    target can be an Item, an NPC, or a plain string (for environmental targets).
    """
    target_id = None
    target_name = None

    if hasattr(target, 'id'):
        target_id = target.id
        target_name = getattr(target, 'name', target.id)
    elif isinstance(target, str):
        target_id = target
        target_name = target
    else:
        target_name = str(target)

    # 1. Specific combo (by id)
    item_specifics = _SPECIFIC_USE.get(item.id, {})
    if target_id and target_id in item_specifics:
        return item_specifics[target_id](state, item, target)

    # 2. Specific combo (by name/alias match)
    if target_name and target_name in item_specifics:
        return item_specifics[target_name](state, item, target)

    # 3. Using on self (no target, or target is the same as user)
    if target_id is None or target_id == "self":
        return _use_item_on_self_fallback(state, item, target)

    # 4. Using on an NPC
    if hasattr(target, 'dialogue'):
        return _use_item_on_npc_fallback(state, item, target)

    # 5. Using on an item
    if hasattr(target, 'description'):
        cat = _item_category(item.id)
        return _r([
            f'You use the {item.name} with the {target_name}. '
            'They touch. They separate. Nothing changes. '
            'Some connections are not meant to be.',
            f'You try to combine the {item.name} with the {target_name}. '
            'The universe shrugs collectively.',
            f'The {item.name} and the {target_name} do not react to each other. '
            'It\'s not you. It\'s them.',
        ])

    # 6. Generic environmental target
    return _generic_use_fallback(state, item, target_name if target_name else "the void")


def get_talk_topic_response(state, npc, topic):
    """Return a string describing what the NPC says about a given topic.

    Checks:
      1. NPC's own dialogue dict (topic key).
      2. Specific (npc_id, topic_category) in _TOPIC_FALLBACKS.
      3. Personality-based fallback.

    Returns None if there's no topic-based response (caller should fall back to
    the NPC's default greeting or the engine's default behaviour).
    """
    topic_lower = topic.lower().strip()

    # 1. Check NPC's own dialogue for a direct topic match
    if topic_lower in npc.dialogue:
        result = npc.dialogue[topic_lower]
        if callable(result):
            return result(state, None)
        return result

    # 2. Check the topic categorisation system
    result = _topic_response_for_npc(npc.id, topic)
    if result is not None:
        if callable(result):
            return result()
        return result
    return None
