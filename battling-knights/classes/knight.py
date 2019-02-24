
class Knight:
  
  base_attack = 1
  base_defence = 1

  
  def __init__(self, name, start_row, start_col):
    self.name = name
    self.start_row = start_row
    self.start_col = start_col

  def get_name(self):
    return self.name

  def add_item(self, name, attack, defence, importance):
    self.base_attack += attack
    self.base_defence += defence


  def set_current_position(self, current_row, current_col):
    self.current_row = current_row
    self.current_col = current_col

  def get_starting_position(self):
    return self.start_row, self.start_col