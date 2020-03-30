import numpy as np

class Bord:
  ROW_SIZE = 10
  COLUMN_SIZE = 10
  cells = np.arange(ROW_SIZE, COLUMN_SIZE)

  def check_input(self, input_index, filling_bord = False, hitting_competitor = False):
    """checking if the input is relevant to the game"""
    try:
        in_index = int(input_index)
    except Exception as e:
        print(e.args)
    try:
        assert (int(in_index) >= 0 and (int(in_index) < 10)), "Incorrect input, not an int between 0-9 "
    except Exception as e:
        print(e.args)
    # if filling_bord:
    #     check_filling(in_index)
    # def check_filling(in_index):
    #     pass