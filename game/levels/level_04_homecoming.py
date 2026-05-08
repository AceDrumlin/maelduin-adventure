"""Level: 04 Homecoming — The Final Confrontation"""

from ..engine import Location
from ._shared import items, npcs


def register(items, npcs):
    """Register this level's locations."""
    from ..engine import LOCATIONS
    l = {}

    l["homecoming"] = Location(
        "homecoming", "The Coast of Ireland — Home at Last",
        "The familiar coast of Ireland. But nothing will ever be the same.",
        detailed_desc=(
            "After countless islands and wonders — after giant ants and talking cats, "
            "after laughing kings and weeping monks, after glass bridges and silver bells — "
            "your curragh finally scrapes onto a familiar shore.\n\n"
            "This is the coast where your father was murdered. You recognize the strand, "
            "the black rocks, the twisted tree that has grown a little more twisted in your absence. "
            "The tide is coming in. It sounds different now — less like water, more like time.\n\n"
            "Your crew steps onto the sand behind you. Diurán's hand is on his sword — "
            "he's a poet, not a fighter, but he'll fight. "
            "Conganchnes stands at your shoulder, his unbreakable skin gleaming. "
            "Fergus hangs back, watching the sky for omens.\n\n"
            "And there — by a fire — sit three men. They are the raiders who killed Ailill Ochair Ága. "
            "They are the reason you left. The reason you crossed the edge of the world.\n\n"
            "They see you. They reach for their weapons — old, rusted blades, not well cared for. "
            "They haven't been warriors in a long time.\n\n"
            "But there is something in their eyes — not defiance, but weariness. "
            "They are old now. The firelight shows grey in their beards, deep lines in their faces. "
            "They look like men who have been waiting for this moment for years. Dreading it.\n\n"
            "One of them speaks. His voice is cracked, uncertain:\n\n"
            '"We knew you would come, son of Ailill. We have been waiting. '
            "We've been waiting for a long time.\"\n\n"
            "The prophecy scroll whispers in your pack: 'Vengeance is a cup that empties the drinker.'\n\n"
            "The wind carries the smell of home. Your crew stands behind you, weapons drawn.\n\n"
            "This is the moment your voyage was meant to end. But how?"
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

    LOCATIONS.update(l)
