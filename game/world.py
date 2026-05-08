"""The Voyage of Mael Duin - World data loader.

This module loads all levels, items, and NPCs from the levels/ package.
"""
from .levels import load_all, items, npcs

# Populate everything
load_all()
