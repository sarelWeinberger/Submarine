import numpy as np
from notebook.notebookapp import raw_input

ROW_SIZE = 10
COLUMN_SIZE = 10

cells = np.arange(ROW_SIZE, COLUMN_SIZE)  # need to initialize whit zero


class MyBord:

    my_cells = np.zeros((ROW_SIZE + 1 ,COLUMN_SIZE + 1), dtype=int)
    for i in range(ROW_SIZE + 1):
        if i == 0:
            continue
        else:
            my_cells[i,0] = i
            my_cells[0,i] = i # because the game bord is a square they have the i

    def __init__(self):
        print(self.my_cells)
        raw_input()


class CompetitorBord:
    # globals:
    hit_i_index = None
    hit_j_index = None

    def geuss_submarine(self):
        i_index = raw_input('enter row  num for guessing  submarine position - int between 0-9')
        self.check_hit_input(i_index)

        j_index = raw_input('enter column num for guessing  submarine position - int between 0-9')
        self.check_hit_input(j_index)

    def check_hit_input(self, input_index):
        """checking if the input is relevant to the game"""
        try:
            in_index = int(input_index)
        except Exception as e:
            print(e.args)
        assert (int(in_index) >= 0 and (int(in_index) < 10)), "Incorrect input, not an int between 0-9 "

    def guess_position(self, i_pos, j_pos, is_praive):

        if is_praive:
            pass

        if (submarine[i_pos][j_pos] == 0):  # empty
            print('empty')
            submarine[i_pos][j_pos] == '.'
        elif (submarine[i_pos][j_pos] == 1):  # hit submarine
            print('hit submarine')
            submarine[i_pos][j_pos] == '0'
        elif (submarine[i_pos][j_pos] == 2):  # submarine
            submarine[i_pos][j_pos] == '0'
        # elif (submarine[i][j] == 3):  # submarine
        # elif (submarine[i][j] == 4):  # submarine
        else:
            print('not a legal number')
            return 1


if __name__ == '__main__':
    submarine = cells  # get zeros

    my_bord = MyBord()

    competitor_bord = CompetitorBord()

    # input for the player


    # guess_position(i_index,j_index)
