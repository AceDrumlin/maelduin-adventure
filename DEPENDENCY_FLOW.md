# The Voyage of Mael Duin — Item Dependency Flow
# Optimal route with item gates marked with [NEED]
#
# HOME → druid gives THREAD
#   → ANTS → take FRUIT (free)
#   → BIRDS → GIVE FRUIT → get FEATHER [NEED: fruit]
#   → ANTS GROVE → USE FEATHER → enter [NEED: feather]
#   → CAT → take MILK → GIVE to cat → PEARL
#   → LAUGHING → JOKE to king → POTION
#   → GLASS BRIDGE → cross (risk) or use OTTER PELT (safe) → SHARD
#   → SMITHY → GIVE PEARL/COIN → HARPOON [NEED: trade item]
#   → WOMEN → talk queen → choice → RING (if refuse)
#   → MONSTERS → FIGHT with HARPOON/Conganchnes
#   → DEEPER to sea2
#     → CULDEES → take BELL
#     → PROPHECY → take SCROLL
#     → HERMIT → take PELT → get BLESSING
#     → FOUR FENCES → choose COPPER → KEY [wrong choices: penalties]
#     → SALMON → USE NET → catch fish [NEED: silver net]
#     → DEEPER to sea3
#       → SERPENT → USE BELL → calm → enter [NEED: silver bell]
#       → PIG → take APPLE (pig chases) or USE POTION → calm
#       → SKULL → talk → hint
#       → WATER HORSE → USE RING or POTION → safe
#       → FIERY PIGS → USE BELL → calm [NEED: silver bell]
#       → CASTLE → USE KEY → enter [NEED: key]
#       → TRUMPET → USE EARPLUGS → safe → take MUFFLER
#       → DEMON → GIVE FISH or PEARL → COIN + clue
#       → GOLDEN PILLAR → USE NET → catch FISH [NEED: net]
#       → HOME → HOMECOMING → YES/NO ending
