"""Level: Prologue — The Wolf's Son
The full backstory: Ailill's death, Mael Duin's childhood, the taunting, the crew."""

from ..engine import Location, LOCATIONS
from ._shared import items, npcs


def register(items, npcs):
    """Register the epic prologue locations."""
    l = {}

    # ────────────────────────────────────────────────────────────
    # SCENE 1: AILILL'S KEEP — The Night of the Wolf
    # ────────────────────────────────────────────────────────────
    
    # Store reference to the keep location for runtime NPC management
    ailill_keep_ref = {}
    
    l["ailill_keep"] = Location(
        "ailill_keep", "Ailill's Keep — The Night of the Wolf",
        "The great hall of Ailill Ochair Ága, the Wolf of the Arans. Torchlight. Feasting. The last night of peace.",
        detailed_desc=(
            "The great hall of Ailill Ochair Ága blazes with torchlight. Warriors line the benches, "
            "their faces red with firelight and mead. A whole pig roasts on a spit the size of a small tree. "
            "The air smells of woodsmoke, roasted meat, and the salt of the sea.\n\n"
            "At the head of the hall sits AILILL himself — a giant of a man with a beard like rusted iron "
            "and arms thick as mast timbers. He is laughing, his head thrown back, a drinking horn "
            "in his fist. His sword — the famous 'Wolf's Fang' — leans against his throne.\n\n"
            '"Tonight we feast!" he roars, and the hall cheers. "Tomorrow we plan the next raid! '
            'But tonight — tonight we drink to the sea that gives us life, the earth that feeds us, '
            'and the enemies who make victory so sweet!"\n\n'
            "In a cradle near the fire, an INFANT sleeps — his newborn son, Mael Duin. "
            "Ailill's wife watches over him, her hand resting on the cradle. "
            "She does not laugh. She has not laughed all night.\n\n"
            "A DRUID sits in the shadows, his eyes on the flames. He has not touched his food.\n\n"
            "Outside, the wind howls. But it is not the wind. It is the sound of oars in the night."
        ),
        items=[],
        npcs=[npcs["ailill"], npcs["mother"], npcs["young_druid"]],
        exits={"west": "ailill_beach", "out": "ailill_beach", "door": "ailill_beach"},
        ambient=lambda s: (
            "The hall roars with laughter and song. A warrior is telling a joke about a sea serpent "
            "and a monk. It's not a very good joke. Everyone loves it."
            if s.turns < 5 else
            "The torches flicker. Someone has opened the door. A draft creeps across the floor."
        ),
        on_enter=lambda s: (
            "You are not Mael Duin. Not yet.\n\n"
            "You are a ghost in this hall — a witness to history. "
            "This is the story of how your father died, and how you came to be.\n\n"
            "Watch. Remember.\n\n"
            "(Type WEST or OUT to go to the beach to see what happens next.)"
            if not s.has_flag("started_prologue") else None
        ),
    )
    # Store reference for runtime NPC manipulation
    ailill_keep_ref["loc_id"] = "ailill_keep"

    # ────────────────────────────────────────────────────────────
    # SCENE 2: THE BEACH — Ailill's Last Stand
    # ────────────────────────────────────────────────────────────
    
    def _beach_enter(s):
        """Handle entering the beach: remove Ailill from both locations, set death witness flag."""
        if not s.has_flag("witnessed_death"):
            s.set_flag("witnessed_death")
            # Remove Ailill from the keep's NPC list (he's dead)
            keep_loc = LOCATIONS.get("ailill_keep")
            if keep_loc:
                keep_loc.npcs = [n for n in keep_loc.npcs if n.id != "ailill"]
            # Remove Ailill from beach NPCs too (he's a corpse, not an interactable NPC)
            beach_loc = LOCATIONS.get("ailill_beach")
            if beach_loc:
                beach_loc.npcs = [n for n in beach_loc.npcs if n.id != "ailill"]
            return (
                "The salt spray stings your eyes. Or perhaps it's something else.\n\n"
                "Ailill Ochair Ága, the Wolf of the Arans, is dead.\n\n"
                "You are one year old. You will not remember this. But it will shape everything."
            )
        return None

    l["ailill_beach"] = Location(
        "ailill_beach", "The Strand — Where the Wolf Fell",
        "A grey beach under a grey sky. The tide is coming in, washing over the body of a warrior.",
        detailed_desc=(
            "You step out of the hall and into a world that has changed.\n\n"
            "The raiders came in the night — men from the Northern Isles, their boats painted with the "
            "skulls of their enemies. They came not for plunder, but for blood. A blood feud, older "
            "than anyone remembers, older than the stones of this island.\n\n"
            "Ailill fought them on the beach, his back to the sea, Wolf's Fang singing in his hands. "
            "He took seven of them with him before they brought him down. The last raider — a grey-bearded "
            "man with one eye — drove a spear through his heart.\n\n"
            "Now Ailill lies on the strand, the tide washing his feet. His sword is still in his hand. "
            "His eyes are open, staring at the grey sky. He looks almost peaceful.\n\n"
            "A WOMAN kneels beside him — his wife, your mother. She does not weep. She is past weeping. "
            "She holds a lock of his hair in her hand.\n\n"
            "A DRUID stands nearby, holding the infant Mael Duin. The baby is crying. He doesn't know why.\n\n"
            "The druid looks at you — through you — and speaks to the ghost you are:\n\n"
            '"You will grow up not knowing this moment. But it will live in your blood. '
            "It will call you to the sea one day. And when it does, you will not return "
            "the same man who left.\"\n\n"
            "(Type EAST to return to the hall, or type ONWARD to move forward in time.)"
        ),
        items=[],
        npcs=[npcs["ailill"], npcs["beach_mother"], npcs["young_druid"]],
        exits={"east": "ailill_keep", "onward": "foster_village", "forward": "foster_village", "time": "foster_village"},
        on_enter=_beach_enter,
        ambient=lambda s: (
            "The tide continues its slow work. Waves erase footprints. The sea does not remember."
            if not s.has_flag("witnessed_death") else
            "The beach is empty now. Only the stones remember what happened here."
        ),
    )

    # ────────────────────────────────────────────────────────────
    # SCENE 3: THE FOSTER VILLAGE — Childhood
    # ────────────────────────────────────────────────────────────
    l["foster_village"] = Location(
        "foster_village", "The Foster Village — Ten Years Later",
        "A small village on the Aran Islands. Children play in the dirt. Goats wander freely. Life continues.",
        detailed_desc=(
            "Ten years have passed. The world has moved on.\n\n"
            "You stand at the edge of a small village — not the great keep of your father, "
            "but a humble cluster of stone huts. Goats wander the lanes. A dog sleeps in the sun. "
            "Children chase each other with sticks, pretending to be warriors.\n\n"
            "One of them is YOU — Mael Duin, aged ten. You are small for your age, but quick. "
            "You have your father's eyes and your mother's silence. You do not know about Ailill. "
            "You have been told your father was a fisherman who drowned.\n\n"
            'Your FOSTER MOTHER — the woman who found Ailill\'s body — watches from the door of her hut. '
            "She is kind, but her eyes hold a secret. She looks at you sometimes and her face twists "
            "with something you don't understand. Grief. Guilt. Love.\n\n"
            "An old DRUID visits the village often. He brings herbs and wisdom. He always stops to talk to you.\n\n"
            '"You have the look of a man who will cross the sea," he tells you. "You just don\'t know it yet."\n\n'
            "(Type ONWARD to grow older. Type TALK TO to speak with people.)"
        ),
        items=[items["childhood_toy"]],
        npcs=[npcs["foster_mother"], npcs["young_druid"]],
        exits={"onward": "training_field", "forward": "training_field", "grow": "training_field"},
        on_enter=lambda s: (
            "A dog barks. A child laughs. The world is simple when you're ten.\n\n"
            "You don't know that your father was a hero. You don't know about the blood on the beach. "
            "You only know that the sea is grey and the sky is grey and somewhere, "
            "out beyond the waves, there is something waiting for you."
            if not s.has_flag("childhood_seen") else None
        ),
        ambient=lambda s: (
            "Children shriek with laughter. A woman sings a lullaby. "
            "The smell of turf smoke hangs in the air."
            if s.turns % 3 == 0 else
            "A goat stares at you. It seems to know something you don't."
            if s.turns % 3 == 1 else
            "The druid is teaching a group of children to count. "
            "They are not very good at it. He is very patient."
        ),
    )

    # ────────────────────────────────────────────────────────────
    # SCENE 4: THE TRAINING FIELD — Becoming a Warrior
    # ────────────────────────────────────────────────────────────
    l["training_field"] = Location(
        "training_field", "The Training Field — Five Years Later",
        "A grassy field by the sea. Wooden swords lie scattered on the ground. Young men train here.",
        detailed_desc=(
            "Five more years have passed. Fifteen summers. Fifteen winters. You are no longer a child.\n\n"
            "The training field overlooks the sea. Here, the young men of the village learn to fight — "
            "not because they expect war, but because the sea is cruel and the world is crueler.\n\n"
            "You have grown tall. Your shoulders have broadened. When you pick up a practice sword, "
            "it feels natural in your hand — as if it remembers something your mind does not.\n\n"
            "You train with CONGANCHNES, a young warrior with a legendary gift: his skin cannot be cut. "
            "He is your best friend and your fiercest rival. He beats you every time, but you're getting closer.\n\n"
            '"You\'re improving," he says, knocking your sword out of your hand. "You only lasted five seconds '
            'longer than last week. Soon you\'ll last almost a minute." He grins.\n\n'
            "FERGUS, the navigator, sits on a rock, studying the stars even though it's daytime. "
            '"The stars say there\'s a storm coming," he mutters. "Also that I should have eaten less cheese."\n\n'
            "DIURÁN, the poet's apprentice, sits under a tree, composing verses about the battle "
            "he's imagining you'll have one day.\n\n"
            "Your foster mother watches from the edge of the field. She looks proud. And sad.\n\n"
            "(Type ONWARD to the next chapter. Type TALK TO to speak with your companions.)"
        ),
        items=[],
        npcs=[npcs["young_conganchnes"], npcs["young_fergus"], npcs["young_diuran"], npcs["foster_mother"]],
        exits={"onward": "feast_hall", "forward": "feast_hall", "grow": "feast_hall"},
        on_enter=lambda s: (
            "The sea glitters in the afternoon light. For a moment, everything is perfect.\n\n"
            "You have friends. You have a home. You have purpose.\n\n"
            "It will not last."
            if not s.has_flag("training_seen") else None
        ),
        ambient=lambda s: (
            "The crash of wooden swords. Grunts of effort. Conganchnes laughing as he wins again."
            if s.turns % 3 == 0 else
            "Fergus is arguing with a seagull about navigation. The seagull seems to be winning."
            if s.turns % 3 == 1 else
            "Diurán reads aloud his latest poem. It's about a warrior who fights a sea monster. "
            "It's not very good. You tell him it's excellent."
        ),
    )

    # ────────────────────────────────────────────────────────────
    # SCENE 5: THE FEAST HALL — The Taunting
    # ────────────────────────────────────────────────────────────
    l["feast_hall"] = Location(
        "feast_hall", "The Feast Hall — Twenty Years Old",
        "The same hall where Ailill once feasted. Different faces. Different songs. But the same silence beneath the laughter.",
        detailed_desc=(
            "Twenty years old. A man, by every measure that matters.\n\n"
            "You stand in the great hall of the Aran Islands — the same hall where your father "
            "drank and laughed on the last night of his life. You don't know that. But something "
            "about this place has always felt strange to you. Familiar. Haunted.\n\n"
            "The hall is full tonight. Warriors, farmers, their wives and children. "
            "A feast to celebrate the summer solstice. The mead flows freely. "
            "Stories are told. Songs are sung. You sit among your companions — Conganchnes, Fergus, Diurán — "
            "laughing at a joke that isn't very funny.\n\n"
            "And then a man speaks.\n\n"
            "He is a warrior from a neighboring territory — drunk, jealous, mean-spirited. "
            "His name is LORCÁN. He has been watching you all night.\n\n"
            '"So," he says, loud enough for the hall to hear, "here sits Mael Duin, the great warrior. '
            'The man with no father. The bastard of Inishmore."\n\n'
            "The hall goes silent.\n\n"
            "Your friends tense. Conganchnes reaches for his sword. Diurán stops writing.\n\n"
            '"You don\'t know, do you?" Lorcán grins. "They never told you. '
            'Your father wasn\'t a fisherman. Your father was Ailill Ochair Ága — the Wolf of the Arans. '
            'And he was murdered. Slain on the beach like a dog. While you slept in your cradle."\n\n'
            "The world stops.\n\n"
            "Your blood burns. Your hand finds your sword. The hall holds its breath."
        ),
        items=[],
        npcs=[npcs["lorcan"], npcs["young_diuran"], npcs["young_conganchnes"], npcs["young_fergus"]],
        exits={"out": "druid_sanctuary", "door": "druid_sanctuary", "north": "druid_sanctuary"},
        on_enter=lambda s: (
            "The fire crackles. The mead is sweet. But there is poison in this hall tonight.\n\n"
            "You are about to learn the truth. And once you learn it, nothing will ever be the same."
            if not s.has_flag("taunting_seen") else None
        ),
        ambient=lambda s: (
            "A harp plays softly. A woman laughs. The world continues, indifferent."
            if not s.has_flag("taunting_seen") else
            "The hall feels empty now. The laughter is gone. The fire has burned low."
        ),
    )

    # ────────────────────────────────────────────────────────────
    # SCENE 6: THE DRUID'S SANCTUARY — The Truth
    # ────────────────────────────────────────────────────────────
    def _druid_enter(s):
        """Auto-give the Magic Thread when entering the sanctuary for the first time."""
        if not s.has_flag("learned_truth"):
            s.set_flag("learned_truth")
            # Auto-add magic thread to inventory
            magic_thread = items.get("magic_thread")
            if magic_thread and magic_thread not in s.inventory:
                s.inventory.append(magic_thread)
            return (
                "The fire crackles. The druid's eyes are ancient — older than the hills, older than grief.\n\n"
                '"Sit," he says. "Eat. Listen. The truth is a heavy meal. You should not take it on an empty stomach."'
            )
        return None

    l["druid_sanctuary"] = Location(
        "druid_sanctuary", "The Druid's Sanctuary",
        "A hidden grove where an old druid lives. The air smells of herbs and old secrets.",
        detailed_desc=(
            "You burst into the druid's grove like a storm. The old man is sitting by his fire, "
            "stirring a pot. He does not look surprised to see you.\n\n"
            '"I was wondering when you\'d come," he says.\n\n'
            '"Is it true?" You can barely speak. Your hands are shaking. "Is Ailill Ochair Ága my father?"\n\n'
            "The druid is silent for a long time. Then he nods.\n\n"
            '"Yes. Ailill was your father. And he was murdered — by raiders from the Northern Isles, '
            'men who had a blood feud with his family stretching back three generations. '
            'They came in the night, burned his hall, and killed him on the beach."\n\n'
            '"Why didn\'t you tell me?"\n\n'
            '"Because I wanted you to live your own life," the druid says. "Not the life of a dead man\'s revenge. '
            'But I see now that the sea will call you, whether I wish it or not. '
            'The blood of the Wolf runs in your veins. And wolves do not stay in their dens when there is '
            'hunting to be done."\n\n'
            "He reaches into his robe and pulls out a shimmering SILKEN THREAD.\n\n"
            '"Take this. Tie it to your mast. It will guide you through the mists. '
            'And take exactly three times nine men — no more, no less. '
            'Twenty-seven souls. Not twenty-six. Not twenty-eight. Twenty-seven."\n\n'
            '"Is there anything else?" you ask.\n\n'
            '"Yes," the druid says. "When you find the men who killed your father... '
            'you may find that killing them is not what you truly want."\n\n'
            "He presses the thread into your hand. It glows faintly, warm as a living thing.\n\n"
            "(The Magic Thread has been added to your inventory.)"
        ),
        items=[],
        npcs=[npcs["druid"]],
        exits={"east": "village_harbor", "out": "village_harbor", "harbor": "village_harbor"},
        on_enter=_druid_enter,
        ambient=lambda s: (
            "The fire pops. An owl calls somewhere in the dark. "
            "The druid hums an old song — a lament, older than the Christian bells."
        ),
    )

    # ────────────────────────────────────────────────────────────
    # SCENE 7: THE VILLAGE HARBOR — Setting Sail
    # ────────────────────────────────────────────────────────────
    l["village_harbor"] = Location(
        "village_harbor", "The Harbor — The Day of Departure",
        "A grey morning. A curragh on the beach. Twenty-seven men. The start of the voyage.",
        detailed_desc=(
            "Three days later, you stand on the beach where your father died. "
            "The tide is low, and the sand is wet and hard beneath your feet.\n\n"
            "Before you, a CURRAGH — a boat of wicker and hide, built for the open sea. "
            "It is larger than any curragh you've ever seen, built by the village's best shipwrights "
            "in a fever of preparation. It will carry twenty-seven men. Not one more. Not one less.\n\n"
            "Your CREW assembles on the sand:\n\n"
            "DIURÁN, the poet, carrying more parchment than provisions. \"I will make this voyage "
            'into an epic that will be sung for a thousand years," he announces. "Assuming we survive it."\n\n'
            "CONGANCHNES, the invulnerable, sharpening his sword with slow, deliberate strokes. "
            '"I\'ve been waiting for a real fight," he says. "The practice field is getting boring."\n\n'
            "FERGUS, the navigator, staring at the sky. \"The stars say we'll have fair winds. "
            'They also say I should have brought a warmer cloak."\n\n'
            "Twenty-four other men — farmers, fishermen, warriors — each with their own reasons "
            "for following you across the edge of the world.\n\n"
            "Your FOSTER MOTHER stands apart from the crowd. She does not weep. She has done enough "
            "weeping for one lifetime. She holds out a small leather pouch — your father's signet ring, "
            "kept hidden all these years.\n\n"
            '"He would be proud of you," she says. "Now go. And come back alive."\n\n'
            "The druid raises his hand in blessing. The sun breaks through the clouds.\n\n"
            "The tide is turning. The sea is waiting.\n\n"
            "(Type WEST to set sail. Type TALK TO to speak with your crew.)"
        ),
        items=[items["fathers_ring"]],
        npcs=[npcs["foster_mother"], npcs["druid"], npcs["young_diuran"], npcs["young_conganchnes"], npcs["young_fergus"]],
        exits={"west": "sea1", "beach": "sea1", "sea": "sea1", "sail": "sea1"},
        on_enter=lambda s: (
            "The wind catches the sail. The curragh groans against the sand.\n\n"
            "Twenty-seven men. One boat. One quest.\n\n"
            "Ahead: the open sea, thirty islands, monsters, gods, wonders, and the men who killed your father.\n\n"
            "Behind: everything you've ever known.\n\n"
            "You take a breath. You give the order. The voyage of Mael Duin begins."
            if not s.has_flag("set_sail") else None
        ),
        ambient=lambda s: (
            "Gulls cry overhead. Waves hiss on the shingle. "
            "Somewhere, a woman begins to sing — a farewell song, old as the islands."
        ),
    )

    # ────────────────────────────────────────────────────────────
    # BONUS: THE FATHER'S TOMB (optional epilogue location)
    # ────────────────────────────────────────────────────────────
    l["fathers_tomb"] = Location(
        "fathers_tomb", "Ailill's Cairn",
        "A pile of stones on a windswept hill, overlooking the sea. A warrior's grave.",
        detailed_desc=(
            "Before you leave, you climb the hill alone.\n\n"
            "A cairn of grey stones marks the place where Ailill Ochair Ága was laid to rest. "
            "No inscription. No marker. Just stones. The sea wind whistles through the gaps.\n\n"
            "You place your hand on the cairn. The stones are cold. The wind is cold. "
            "But somewhere beneath the chill, you feel warmth — the last ember of a fire that "
            "burned brighter than most.\n\n"
            '"I will find them," you say. "And I will do what must be done."\n\n'
            "The wind answers with silence. The sea answers with waves. "
            "The stones answer with stillness.\n\n"
            "You turn and walk back to the harbor."
        ),
        items=[],
        npcs=[],
        exits={"down": "village_harbor", "back": "village_harbor"},
    )

    LOCATIONS.update(l)
