import numpy as np

class Arena:
  knights = []
  items = []

  def __init__(self, row_size, col_size, fill):
    self.arena = np.full((row_size, col_size), fill)

  def add_knight(self, name, start_row, start_col):
    """ Add knight to the board """
    self.knights.append(name) # Add a Knight to the knights list
    self.arena[start_row, start_col] = name


  def get_knight_position(self, name):

    if name in self.knights:
      return np.where(self.arena == name)
    else:
      print("Please do type a name of a knight, not an item or anything else")
      return

  def get_item_position(self, name):
    """ Get item position according its name """

    if name in self.items:
      return np.where(self.arena == name)
    else:
      print("Please do type a name of aa item, not a knight or anything else")
      return

  def moving_knight(self, name, current_row, next_row, current_col, next_col, fill_previous):
    """ Moves the Knight according the name and its current location """
    print(("Knight {} current row {} next row {} current col {} next col {}"
    .format(name, current_row, next_row, current_col, next_col)))

    # Check if Knight next tile is gonna throw him off the board (Drowning him)
    if (next_row == (-1) or next_row == (8) or next_col == (-1) or next_col == (8)):
      self.arena[current_row, current_col] = fill_previous
      print("Knight {} drowned".format(name))
    #print("Name:", name, "Current row:", current_row, "Next row:", next_row)

    # Check if a Knight is is on the next tile
    elif self.knights in self.arena[current_row, current_col]:
      pass
    else:
      self.arena[current_row, current_col] = fill_previous
      self.arena[next_row, next_col] = name
    
  def add_item(self, name, start_row, start_col):
    """ Add item to the board according its name and its position """

    self.items.append(name) # Add an item to the items list
    self.arena[start_row, start_col] = name


  def __str__(self):
    return str(self.arena)

  