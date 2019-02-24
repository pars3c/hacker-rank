
class Item:
  
  def __init__(self, name, start_row, start_col, base_attack, base_defence, importance):
    self.name = name
    self.start_row = start_row
    self.start_col = start_col
    self.base_attack = base_attack
    self.base_defence = base_defence
    self.importance = importance

  def get_name(self):
    return self.name

  def set_current_position(self, current_row, current_col):
    self.current_row = current_row
    self.current_col = current_col

  def get_starting_position(self):
    return self.start_row, self.start_col

  def get_item_stats(self):
    return base_attack, base_defence, importance