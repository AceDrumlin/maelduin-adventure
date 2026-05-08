"""Level: 00 Home — The Aran Islands"""

from ..engine import Location
from ._shared import items, npcs


def register(items, npcs):
    """Register this level's locations."""
    from ..engine import LOCATIONS
    l = {}

    l["home"] = Location(
        "home", "Your Village — The Aran Islands",
        "Your village on the Aran Islands. The stone huts huddle against the wind, and the grey Atlantic stretches to the horizon.",
        detailed_desc=(
            "You stand at the edge of your village on Inishmore, the largest of the Aran Islands. "
            "The stone walls of your people's huts are worn smooth by centuries of Atlantic wind. "
            "Salt-spray hangs in the air. Somewhere, a dog barks. A child laughs.\n\n"
            "To the west, the endless grey ocean stretches toward the edge of the known world. "
            "To the east, the fields of Ireland are a distant green smudge.\n\n"
            "Your CURRAGH — a sturdy boat of wicker and hide — is pulled up on the beach, ready to sail. "
            "It smells of fish, salt, and adventure.\n\n"
            "The memory of your father's murder burns in your chest like a hot coal. "
            "Your hand drifts to your sword-hilt before you catch yourself.\n\n"
            "An old DRUID sits by a fire near the village center. He is stirring a pot that "
            "smells like boiled nettles and regret."
        ),
        items=[items["crew_provisions"], items["magic_thread"]],
        npcs=[npcs["druid"]],
        exits={"west": "sea1", "beach": "sea1", "sea": "sea1"},
        ambient=lambda s: (
            "A seabird cries overhead. The wind whispers through the grass. "
            "Somewhere, a blacksmith's hammer rings against iron."
            if s.turns < 3 else
            "Your crew is gathered by the curragh, ready to depart. "
            "Diurán is adjusting his quill. Conganchnes is already sharpening his sword."
        ),
        on_look=lambda s: (
            "The druid catches your eye and beckons. He seems to know why you're here."
            if not s.has_flag("talked_to_druid") else
            "Your curragh bobs impatiently in the surf. The crew is waiting for your orders."
        ),
    )

    LOCATIONS.update(l)
