import numpy as np

class Arena:

  def __init__(self, row_size, col_size, fill):
    self.arena = np.full((row_size, col_size), fill)

  def add_knight(self, name, start_row, start_col):
    self.arena[start_row, start_col] = name

  def get_knight_position(self, name):
    
    return np.where(self.arena == name)

  def moving_knight(self, name, current_row, next_row, current_col, next_col, fill_previous):
    print("Name:", name, "Current row:", current_row, "Next row:", next_row)
    self.arena[current_row, current_col] = fill_previous
    self.arena[next_row, next_col] = name
    

  def __str__(self):
    return str(self.arena)

  def add_item(self, name, row, col, attack, defence):
    pass