"""

Challenge: Battling Knights
--------------

The game starts with four knights:

    RED = 'R'
    BLUE = 'B'
    GREEN = 'G'
    YELLOW = 'Y'

The worlds consists on an 8x8 2D array||arena, if one of the knights moves out of this array it will drown.

Knights starting positions:

    'R' = arena[0,0]
    'B' = arena[7,0]
    'G' = arena[7,7]
    'Y' = arena[0,7]

Knights can only move 1 tile at a time in any of the four directions:

    'N' = UP
    'S' = DOWN
    'E' = RIGHT
    'W' = LEFT

Each knight base attack and defense of 1.

Around the board you have four items:

    Axe('A') gives +2 Attack. Starting position = arena[2,2]
    Dagger('D') gives +1 Attack. Starting position = arena[2,5]
    Helmet('H') gives +1 Defence. Starting position = arena[5,2]
    MagicStaff('M') gives +1 Attack, +1 Defense. Starting position = arena[5,5]

Knights will pick up an item on the tile(if any) before fighting enemies

If a knight dies: Drop item

If knight drowns AND knight has item: Drop the item to the tile where he stood before drowning

If knight moves onto a tile with an item and knight does not have any item equipped: Equip that item immediatly gaining its bonus

If knight already has item and moves onto a tile with an item: Ignore it

If knight moves onto a tile with 2 items: Equip only the best one in the following order: (1:A, 2:M, 3:D, 4:H)



"""


import numpy as np


class Knight:
  RED = 'R'
  BLUE = 'B'
  GREEN = 'G'
  YELLOW = 'Y'


arena = np.full((8, 8), '|_|')
arena[0,0] = 'R' 
arena[7,0] = 'B' 
arena[7,7] = 'G' 
arena[0,7] = 'Y' 

print(arena)