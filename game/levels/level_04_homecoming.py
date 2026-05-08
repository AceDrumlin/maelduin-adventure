"""Level: 04 Homecoming — The Final Confrontation

Expanded into a multi-scene emotional climax with three distinct endings.
Scenes: Beach (arrival + druid) → Hill (Ailill's cairn) → Choice (final moment)
"""

from ..engine import Location
from ._shared import items, npcs


def _format_islands_visited(state):
    """Generate a list of notable islands the player visited."""
    visited = [k.replace("_visited", "") for k in state.flags if k.endswith("_visited")]
    return visited


def register(items, npcs):
    """Register this level's locations."""
    from ..engine import LOCATIONS
    l = {}

    # ═══════════════════════════════════════════════════════════════
    # SCENE 1: BEACH — Arrival at the Aran Islands
    # ═══════════════════════════════════════════════════════════════
    l["homecoming_beach"] = Location(
        "homecoming_beach", "The Coast of Ireland — Home at Last",
        "The familiar grey strand where your father fell. The tide murmurs like an old storyteller.",
        detailed_desc=(
            "After countless islands and wonders — after giant ants and talking cats, "
            "after laughing kings and weeping monks, after glass bridges and silver bells — "
            "your curragh finally scrapes onto a familiar shore.\n\n"
            "This is the strand where your father was murdered. You recognise the black rocks, "
            "the twisted tree that has grown a little more twisted in your absence, "
            "the exact spot where Ailill Ochair Ága drew his last breath.\n\n"
            "The tide is coming in. It sounds different now — less like water, more like time. "
            "Three years of voyaging, and you have returned to the same patch of sand.\n\n"
            "Your crew steps onto the beach behind you. Diurán's hand is on his sword — "
            "he's a poet, not a fighter, but he'll fight. "
            "Conganchnes stands at your shoulder, his unbreakable skin gleaming. "
            "Fergus hangs back, watching the sky for omens.\n\n"
            "And there — by a driftwood fire — sits someone you recognise.\n\n"
            "The DRUID from your village. The same old man who gave you the Magic Thread "
            "and told you to take three times nine men. He is stirring a small pot, "
            "the same pot he was stirring three years ago, as if no time has passed at all."
        ),
        items=[],
        npcs=[],
        exits={"up": "homecoming_hill", "hill": "homecoming_hill",
               "inland": "homecoming_hill", "north": "homecoming_hill"},
        on_enter=lambda s: (
            s.set_flag("homecoming_reached") or
            _druid_arrival_speech(s)
            if not s.has_flag("homecoming_beach_visited") else
            "The druid is still by the fire, watching you with patient eyes.\n\n"
            "Your curragh rests on the strand. The hill path rises to the east."
        ),
        on_look=lambda s: (
            "The druid catches your eye. He is waiting to speak with you."
            if not s.has_flag("druid_arrival_spoken") else
            "The druid nods at you from his place by the fire. "
            "The path up to the hill — where Ailill's cairn stands — is to the east."
        ),
        ambient=lambda s: (
            "The fire crackles softly. A curlew calls across the strand. "
            "The sea, which has been your home for three years, now sounds strange and foreign."
        ),
    )

    # ═══════════════════════════════════════════════════════════════
    # SCENE 2: HILL — Ailill's Cairn
    # ═══════════════════════════════════════════════════════════════
    l["homecoming_hill"] = Location(
        "homecoming_hill", "The Hill of Ailill Ochair Ága",
        "A windswept hill overlooking the Aran Islands. A cairn of grey stones marks where the Wolf fell.",
        detailed_desc=(
            "You climb the hill above the strand, following the path your father walked "
            "a thousand times before. The wind is stronger up here — it whips your hair "
            "and tugs at your cloak.\n\n"
            "At the summit stands a CAIRN of grey stones, each one stacked with care. "
            "This is where your father's body was laid to rest. "
            "The stones are weathered now — three years of Atlantic wind and rain "
            "have softened their edges, but the cairn stands firm.\n\n"
            "From here you can see the whole island: the stone huts of your village, "
            "the grey thread of the road, the endless sea that carried you to the edge of the world "
            "and brought you back.\n\n"
            "A small offering lies at the base of the cairn: a few wildflowers, "
            "a crust of bread, a half-full cup of mead. Someone still remembers."
        ),
        items=[],
        npcs=[],
        exits={"down": "homecoming_beach", "back": "homecoming_beach",
               "beach": "homecoming_beach", "south": "homecoming_beach",
               "east": "homecoming_choice", "forward": "homecoming_choice",
               "onward": "homecoming_choice"},
        on_enter=_on_hill_enter,
        on_look=lambda s: (
            "At the base of the cairn, you notice something you missed before: "
            "a small carving in the stone. A wolf's head, howling at a crescent moon. "
            "Ailill's sign. Someone — the druid, perhaps — left it here.\n\n"
            "To the east, a narrow path leads to a rocky point overlooking the sea. "
            "Something waits there."
        ),
        ambient=lambda s: (
            "The wind whistles through the cairn stones — a sound almost like laughter. "
            "Your father's laughter, perhaps."
        ),
    )

    # ═══════════════════════════════════════════════════════════════
    # SCENE 3: CHOICE — The Final Moment
    # ═══════════════════════════════════════════════════════════════
    l["homecoming_choice"] = Location(
        "homecoming_choice", "The Point of Decision",
        "A rocky promontory overlooking the sea. This is where it ends.",
        detailed_desc=(
            "You walk the narrow path to the edge of the cliff. The sea crashes below, "
            "the same sea that carried you to thirty islands and thirty wonders.\n\n"
            "Ahead, the sun is setting over the Atlantic — gold and crimson bleeding "
            "into the water like a wound, like a blessing, like the end of a story."
        ),
        items=[],
        npcs=[],
        exits={"back": "homecoming_hill", "west": "homecoming_hill",
               "down": "homecoming_beach"},
        on_enter=_on_choice_enter,
        on_look=lambda s: _choice_look_text(s),
    )

    LOCATIONS.update(l)


# ─────────────────────────────────────────────────────────────
# DYNAMIC TEXT GENERATORS
# ─────────────────────────────────────────────────────────────

def _crew_status(state):
    """Describe the crew's state after the voyage."""
    alive = sum(1 for c in state.crew if c.alive)
    total = len(state.crew)
    if alive == total:
        return "Your crew is whole — all three foster-brothers stand with you, scarred but alive."
    lost = state.dead_crew
    names = [c.name for c in lost]
    if len(names) == 1:
        return f"One of your crew did not survive the voyage. {names[0]} is gone. Their absence is a silence you carry."
    elif len(names) == 2:
        return f"Two of your crew fell along the way — {names[0]} and {names[1]}. You carry their memory."
    else:
        return f"Only you remain. The others are lost to the sea. You carry their memory like stones in your chest."


def _count_notable_islands(state):
    """Count known islands for flavor text."""
    count = sum(1 for k in state.flags if k.endswith("_visited"))
    return count


def _druid_arrival_speech(state):
    """Generate the druid's arrival speech based on game state."""
    lines = []
    lines.append("The druid looks up as you approach. His milky eyes find you immediately.")
    lines.append("")
    lines.append('"Mael Duin," he says. His voice is the same — like rustling leaves, like wind through stones. "You have returned."')
    lines.append("")
    lines.append("He gestures to the fire. 'Sit. The stew is thin but warm. There is bread.'")

    if state.has_flag("confronted_murderer"):
        lines.append("")
        lines.append('He studies your face for a long moment. "Ah. I see it in your eyes. You found him. ')
        lines.append('You stood face to face with the man who killed your father. And yet here you sit, ')
        lines.append('still whole — still yourself. That took more courage than any battle."')
    else:
        lines.append("")
        lines.append('"You have sailed to the edge of the world and back," the druid says. "I see the sea in your bones. ')
        lines.append('The question is: did you find what you were looking for?"')
        lines.append("")
        lines.append('He pauses, stirring the pot. "Or did you find something else?"')

    if state.has_flag("otter_pelt_returned"):
        lines.append("")
        lines.append('"I see you met the hermit," the druid adds with a faint smile. "That old soul has been praying ')
        lines.append('for you since before you left. His blessing carries weight in the Otherworld."')

    if state.has_flag("king_pacified"):
        lines.append("")
        lines.append('"You made the Laughing King laugh," he chuckles. "That is no small feat. He has not laughed ')
        lines.append('since the Silver Age ended. You brought joy to a god. Remember that."')

    if state.has_flag("cat_pacified"):
        lines.append("")
        lines.append('"And the Cat — you satisfied the Cat. That creature has judged a hundred warriors and found them wanting. ')
        lines.append('It found you... acceptable." He almost smiles.')

    if state.has_flag("prophecy_scroll") or any(i.id == "prophecy_scroll" for i in state.inventory):
        lines.append("")
        lines.append('"You still carry the prophecy scroll," he notes. "Good. Read it again tonight. ')
        lines.append('The words have changed, as I promised they would. They always do."')

    lines.append("")
    lines.append('He looks past you, towards the hill. "Your father\'s cairn is up there. ')
    lines.append('He has been waiting for you. Go. Speak with him. Then come back and tell me what you decide."')

    state.set_flag("druid_arrival_spoken")
    return "\n".join(lines)


def _hill_travel_reflection(state):
    """Generate reflection text referencing specific journeys."""
    visited = _count_notable_islands(state)
    addl = []
    addl.append("")

    # Build a reflective paragraph referencing player's journey
    if visited > 15:
        addl.append("You have visited over a dozen islands — more than any Irishman has ever seen. "
                     "The druid was right: the sea held mysteries beyond counting.")
    elif visited > 8:
        addl.append("You have seen wonders that will fill songs for generations. "
                     "The druid was right: the sea is a living thing with stories to tell.")
    else:
        addl.append("You have seen enough to know that the world is larger "
                     "than you ever imagined. The druid was right: the sea teaches what cannot be spoken.")

    # Reference specific items
    if any(i.id == "prophecy_scroll" for i in state.inventory):
        addl.append("")
        addl.append("The Prophecy Scroll rustles in your pack. You unroll it and read: "
                     "'The truth of your voyage lies not at the end of your spear, "
                     "but at the beginning of your heart.'")

    if state.has_flag("otter_pelt_returned"):
        addl.append("")
        addl.append("You think of the Hermit on his bare rock, the otter at his feet. "
                     "He gave you his blessing, and you gave him peace. "
                     "Some debts are paid not with gold, but with grace.")

    if state.has_flag("king_pacified"):
        addl.append("")
        addl.append("You remember the Laughing King — his infinite, exhausting mirth, "
                     "and how, when you finally made him truly laugh, he wept with relief. "
                     "Joy and sorrow are the same tide, rising and falling.")

    if state.has_flag("stayed_with_queen"):
        addl.append("")
        addl.append("The memory of the Queen's Island haunts you still. "
                     "You lost time there — and a crew member. The price of pleasure is always paid in pain.")

    if state.has_flag("resisted_queen"):
        addl.append("")
        addl.append("You resisted the Queen's enchantment. Not all who leave are free, she said. "
                     "But you left anyway. That took strength.")

    # Crew status
    addl.append("")
    addl.append(_crew_status(state))

    return "\n".join(addl)


def _final_moment_text(state):
    """Generate text for the final choice scene."""
    lines = []

    if state.has_flag("confronted_murderer"):
        lines.append("You stood before Garbh, the one-eyed raider who killed your father. "
                     "You looked into the face of the man who took everything from you — "
                     "and he looked back with an old man's tired eyes. He did not beg. "
                     "He did not fight. He simply... waited.")
        lines.append("")
        if state.has_flag("forgave_garbh"):
            lines.append("And you forgave him. Let him live. Let the cycle end. "
                         "His hand in yours — the hand that held the blade — and you let it go.")
        elif state.has_flag("killed_garbh"):
            lines.append("And you killed him. The blood of Garbh mixed with the dust of the castle floor. "
                         "His one eye stared at nothing. You got your revenge.")
        else:
            lines.append("You spoke with him and left him alive, unsure whether to strike or stay your hand. "
                         "The question followed you across the sea, unanswered.")
    else:
        lines.append("You never found him. The one-eyed raider who killed your father — "
                     "Garbh of the Northern Isles — remains somewhere out in the world. "
                     "Your quest is incomplete. The stone in your chest has not been lifted.")

    lines.append("")
    lines.append("The sun descends. The sea glows like molten gold. "
                 "Your crew waits behind you in silence. They have followed you across the world. "
                 "They will follow you into whatever comes next.")
    lines.append("")
    lines.append("This is the moment. The voyage was never about finding your father's killers. "
                 "It was about finding yourself — and deciding who that person would be.")

    return "\n".join(lines)


def _on_hill_enter(state):
    """Handle first entry to the hill location."""
    if state.has_flag("hill_visited"):
        return "The cairn stands silent against the sky. The wind sings through the stones."

    state.set_flag("hill_visited")

    text = [
        "You climb the hill alone. Your crew understands — this is not a moment for company.",
        "",
        "The cairn is smaller than you remember. Or perhaps you are larger. "
        "Three years at sea changes a man. It changes how he sees things.",
        "",
        "You kneel before the stones. The wind drops, as if the world is holding its breath.",
        "",
        '"Father," you whisper. "I have come home."',
        "",
        "There is no answer. The cairn does not speak. But something shifts in your chest — "
        "a tightness you have carried since the day you learned of his death. It loosens, just slightly.",
        "",
        "You place your hand on the cold stones. Somewhere, across the sea and beyond the veil, "
        "the Wolf of the Arans knows his son has returned.",
    ]

    # Add player-specific item reflection
    if any(i.id == "fathers_ring" for i in state.inventory):
        text.append("")
        text.append("You take your father's signet ring from your finger and press it against the cairn stone. "
                     "The wolf's head matches the carving. For a moment, stone and silver are one.")
        text.append("You put the ring back on. It feels warmer now.")

    if any(i.id == "childhood_toy" for i in state.inventory):
        text.append("")
        text.append("You take out the wooden horse your father carved for you before you were born. "
                     "You set it on the ground. It rocks on its uneven legs. "
                     "You realise: he made it imperfect on purpose. So it would always move, never settle.")

    # Reference the druid wisdom
    text.append("")
    text.append("You stand and look out at the sea — the same grey immensity that swallowed three years of your life.")
    text.append("The druid's words echo: 'The path of revenge is a twisted one.'")
    text.append("The hermit's words echo: 'Your father does not ask for revenge. He asks that you live.'")
    text.append("The prophecy scroll's words echo: 'Vengeance is a cup that empties the drinker.'")
    text.append("")
    text.append("The sun is setting. To the east, a narrow path leads to a rocky point. "
                "Something waits for you there.")

    return "\n".join(text)


def _on_choice_enter(state):
    """Handle first entry to the choice scene."""
    if state.has_flag("homecoming_ending_shown"):
        return None

    state.set_flag("homecoming_ending_shown")

    text = [
        "You stand at the edge of the cliff, the wind in your hair, "
        "the sea below, the sky above, the past behind you, the future unwritten.",
    ]

    # Check for pre-determined outcome
    if state.has_flag("forgave_garbh"):
        text.append("")
        text.append("But the choice has already been made. "
                     "You forgave Garbh in the red-lit chamber of the Revolving Castle. "
                     "His hand, the hand that killed your father, clasped yours. "
                     "You are not the same man who sailed away three years ago.")
        text.append("")
        text.append("The druid appears on the path behind you, leaning on his staff. "
                     "He does not speak. He simply nods — once — and his milky eyes glisten.")
        text.append("")
        text.append('"You have made your choice, Mael Duin. The sea has given you back to yourself."')
        text.append("")
        text.append("The wind changes. It is blowing east — towards home.")
        state.awaiting_choice = "ending_forgiven"
        state.set_flag("ending_decided")
        return "\n".join(text)

    elif state.has_flag("killed_garbh"):
        text.append("")
        text.append("But the choice has already been made. "
                     "Garbh lies dead in the Revolving Castle. "
                     "His one eye — the eye that watched your father die — is closed forever. "
                     "You got your revenge. You got exactly what you sailed for.")
        text.append("")
        text.append("The druid appears on the path behind you. His face is grey. "
                     "He does not meet your eyes.")
        text.append("")
        text.append('"So," he says quietly, "you have become what you hunted."')
        text.append("")
        text.append("He turns and walks back down the hill, his staff leaving no mark on the earth.")
        state.awaiting_choice = "ending_vengeance"
        state.set_flag("ending_decided")
        return "\n".join(text)

    # Open choice — player must decide now
    text.append("")
    text.append("Three years. Thirty islands. Wonders and horrors beyond telling. "
                "And it all comes down to this: a sunset, a cliff, and a question.")
    text.append("")
    text.append("Your father's murderers are not here. The sea did not bring you to them. "
                "It brought you to yourself. The question was never 'Will you forgive them?' "
                "It was always 'Can you forgive yourself?'")
    text.append("")
    text.append("The druid's voice comes from behind you — he has followed you up the hill.")
    text.append("")

    if state.has_flag("confronted_murderer"):
        text.append('"You have seen his face. You have heard his story. '
                     'He killed your father in a blood feud — a cycle as old as Ireland. '
                     'Your father killed his brother. His father killed your grandfather\'s man. '
                     'The chain stretches back into darkness.\n\n')
        text.append('You can add another link. Or you can break it."')
    else:
        text.append('"You sailed the world and did not find him. Perhaps that is the sea\'s way of telling you '
                     'that the man you were looking for was never Garbh. It was the man you could become."')

    text.append("")
    text.append("He falls silent. The sea crashes below. The sky burns gold and red.")
    text.append("")
    text.append("Type YES to forgive — to let go of vengeance and end the cycle.")
    text.append("Type NO to take your vengeance — to honour the old ways and the memory of your father.")

    state.awaiting_choice = "ending"
    return "\n".join(text)


def _choice_look_text(state):
    """Generate look text for the choice scene."""
    if not state.has_flag("homecoming_ending_shown"):
        return None

    text = "You stand at the Point of Decision. The sea stretches before you, endless and eternal."

    if state.awaiting_choice == "ending_forgiven":
        text += (
            "\n\nYour choice is made. You have forgiven Garbh. "
            "The wind has changed. Your crew is waiting. "
            "It is time to go home."
        )
    elif state.awaiting_choice == "ending_vengeance":
        text += (
            "\n\nYour choice is made. You have taken your vengeance. "
            "The wind carries a strange chill. Your crew is silent. "
            "You have won, but the victory tastes of ash."
        )
    elif state.awaiting_choice == "ending":
        text += (
            "\n\nThe moment hangs. Type YES to forgive. Type NO for vengeance."
        )

    return text
