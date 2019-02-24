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
from classes.arena import Arena
from classes.knight import Knight
from classes.items import Item


R = Knight('R', 0, 0)
B = Knight('B', 7, 0)
G = Knight('G', 7, 7)
Y = Knight('Y', 0, 7)

# Name, Starting Row, Starting Col, Attack, Defence, Importance
A = Item('A', 2, 2, 2, 0, 1)
D = Item('D', 2, 5, 1, 0, 2)
H = Item('H', 5, 2, 0, 1, 3)
M = Item('M', 5, 5, 1, 1, 4)

knights = [R, B, G, Y] 
items = [A, D, H, M]

arena = Arena(8, 8, '|_|')

def set_starting_board():
  for knight in knights:
    starting_row, starting_col = knight.get_starting_position()
    arena.add_knight(knight.get_name(), starting_row, starting_col)

  for item in items:
    starting_row, starting_col = item.get_starting_position()
    arena.add_item(item.get_name(), starting_row, starting_col)

def moving_arena_board():
  print(arena)
  f = open("moves.txt", "r")
  for i, x in enumerate(f):
    if "GAME-START" in x:
      continue
    elif "GAME-END" in x:
      break
    else:
      print("Iteration: ", i)
      
      knight_name = x.split(":")[0]
      #print(knight_name)
      direction = x.split(":")[1]
      row, col = arena.get_knight_position(knight_name)
      #print(row, col)
      
      if "S" in direction:
        arena.moving_knight(knight_name, row, row+1, col, col, '|_|')
        print(arena)
      elif "N" in direction:
        arena.moving_knight(knight_name, row, row-1, col, col, '|_|')
        print(arena)
      elif "E" in direction:
        arena.moving_knight(knight_name, row, row, col, col+1, '|_|')
        print(arena)
      elif "W" in direction:
        arena.moving_knight(knight_name, row, row, col, col-1, '|_|')
        print(arena)


set_starting_board()
moving_arena_board()



