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


class Arena:

  def __init__(self, row_size, col_size, fill):
    self.arena = np.full((row_size, col_size), fill)

  def add_knight(self, name, start_row, start_col):
    self.arena[start_row, start_col] = name

  
  def __str__(self):
    return str(self.arena)

  def add_item(self, name, row, col, attack, defence):
    pass



class Knight:
  
  base_attack = 1
  base_defense = 1

  def __init__(self, name, start_row, start_col):

    self.name = name
    self.start_row = start_row
    self.start_col = start_col
    
  def get_name(self):
    return self.name

  def set_current_position(self, current_row, current_col):
    self.current_row = current_row
    self.current_col = current_col

  def get_starting_position(self):
    return self.start_row, self.start_col



R = Knight('R', 0, 0)
B = Knight('B', 7, 0)
G = Knight('G', 7, 7)
Y = Knight('Y', 0, 7)

# Name, Attack, Defence, Importance
A = ['A', 2, 0, 1]
D = ['D', 1, 0, 2]
H = ['H', 0, 1, 3]
M = ['M', 1, 1, 4]

knights = [R, B, G, Y] 
items = [A, D, H, M]

arena = Arena(8, 8, '|_|')

for knight in knights:
  starting_row, starting_col = knight.get_starting_position()
  arena.add_knight(knight.get_name(), starting_row, starting_col)


print(arena)