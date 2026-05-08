"""Level files for The Voyage of Mael Duin.

Each level file exports a `register(items, npcs, locations)` function
that adds its content to the shared dictionaries.

Call `load_all()` to populate all items, NPCs, and locations.
"""

from ._shared import items, npcs, load_shared
from .level_prologue import register as reg_prologue
from .level_00_home import register as reg_00
from .level_01_sea1 import register as reg_01
from .level_02_sea2 import register as reg_02
from .level_03_sea3 import register as reg_03
from .level_04_homecoming import register as reg_04
from .level_05_missing_islands import register as reg_05
from .level_06_missing_islands_2 import register as reg_06


def load_all():
    """Load all items, NPCs, and locations into the shared dicts."""
    load_shared()
    reg_prologue(items, npcs)
    reg_00(items, npcs)
    reg_01(items, npcs)
    reg_02(items, npcs)
    reg_03(items, npcs)
    reg_04(items, npcs)
    reg_05(items, npcs)
    reg_06(items, npcs)


from ._shared import items, npcs
