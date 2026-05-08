"""Drink utility handler for The Voyage of Mael Duin."""

def handle_drink(state, args):
    """Handle DRINK command - primarily for the Freshwater Well."""
    loc = state.get_location()
    if not loc:
        return "There is nothing to drink here."
    if loc.id == "freshwater_well" and not state.has_flag("well_drunk"):
        state.set_flag("well_drunk")
        state.set_flag("well_visited")
        state.score += 2
        msg = (
            "You cup your hands and drink from the shimmering well.\n\n"
            "The water is cold and impossibly clear. As it passes your lips, "
            "the world shifts.\n\n"
            "For a moment, you see everything clearly: your father's face, "
            "the faces of your crew, the islands you have visited and those yet to come.\n\n"
            "You understand -- briefly, profoundly -- that every island was a mirror, "
            "every monster a part of yourself, every storm a lesson you needed to learn.\n\n"
            "The vision fades. You are standing at the well, your hands wet, "
            "your heart strangely light.\n\n"
            "(+2 points. The Water of Seeing has shown you a glimpse of the truth.)"
        )
        return msg
    elif loc.id == "freshwater_well" and state.has_flag("well_drunk"):
        return "You have already drunk from the well. The water is still there, but the vision will not come twice."
    return "There is nothing to drink here."
