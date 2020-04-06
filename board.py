import numpy as np
from notebook.notebookapp import raw_input
from bcolors import Bcolors
import re


class Board:
    ROW_SIZE = 10
    COLUMN_SIZE = 10

    @staticmethod
    def check_bigger_submarine_size_proportional_to_the_board(size):
        size = Board.check_if_the_input_is_int(size)
        valid_size_for_the_bigger_submarin = None
        while not valid_size_for_the_bigger_submarin:
            if size <= 5 and size >= 2:
                valid_size_for_the_bigger_submarin = True
                return size
        else:
                valid_size_for_the_bigger_submarin = False
                size = raw_input(Bcolors.FAIL + "not valid size, choose size between 2 to 5")
        #TODO: create eqesion for any size of board

    @staticmethod
    def cell_position_char(submarine, i_pos, j_pos, is_praive):

        if submarine[i_pos][j_pos] == 0:  # empty / unchecked
            return '.'
        elif submarine[i_pos][j_pos] == 1:
            if is_praive:
                return 0
            else:  # the competitor board
                return '.'
        elif submarine[i_pos][j_pos] == 2:
            return '*'
        elif submarine[i_pos][j_pos] == 3:
            return '@'
        elif submarine[i_pos][j_pos] == 4:
            return '#'
        else:
            print('not a legal number')
            return 1

    @staticmethod
    def check_if_the_input_is_int(input):
        input_valid = None
        while not input_valid:
            try:
                input = int(input)
                input_valid = True
                return input
            except:
                input_valid = False
                print(Bcolors.FAIL + 'input is not a number try new input' + Bcolors.ENDC)
                input = raw_input(' try new int - input')

    @staticmethod
    def check_input_define_in_the_board(input_index, hitting_competitor=False):
        """checking if the input is relevant to the game"""
        input_on_board = None
        int_input = Board.check_if_the_input_is_int(input_index)
        while not input_on_board:
            if (int(int_input) > 0 and (int(int_input) <= Board.ROW_SIZE)) and (
                    int(int_input) > 0 and (int(int_input) <= Board.COLUMN_SIZE)):
                input_on_board = True
                return int_input
            else:
                input_on_board = False
                print(Bcolors.FAIL + "Incorrect input, not an int between 0 and {}".format(
                    Board.ROW_SIZE) + Bcolors.ENDC)
                int_input = raw_input('try new input')

    @staticmethod
    def submarine_legal_length_check(submarine_size, submarine_start, submarine_end):
        # checking length
        legal_length = None
        while not legal_length:
            if ((submarine_end - submarine_start) == submarine_size):
                legal_length = True
                return submarine_start, submarine_end
            else:
                legal_length = False
                print(Bcolors.FAIL + "wrong submarine size should be size of {}".format(submarine_size) + Bcolors.ENDC)
                submarine_start = raw_input(" try anther parameter set new start point")
                submarine_start = Board.check_input_define_in_the_board(submarine_start)
                submarine_end = raw_input(" try anther parameter set new end point")
                submarine_end = Board.check_input_define_in_the_board(submarine_end)

    @staticmethod
    def submarine_orientation_input_validation(submarine_orientation):
        valid_orientation_input = None
        while not valid_orientation_input:
            pattern = re.compile(r'(H|V)', re.IGNORECASE)
            match = pattern.match(submarine_orientation)
            if match:
                valid_orientation_input = True
                submarine_orientation = submarine_orientation.upper()
                return submarine_orientation
            else:
                valid_orientation_input = False
                print("not valid input")
                submarine_orientation = raw_input(Bcolors.OKBLUE +
                                                  'choose "V" to vertical submarine or "H" to horizontal submarine' + Bcolors.ENDC)

    @staticmethod
    def checking_cells_occupied_or_adjacent_to_existing_submarine(cells, row_x, row_y, orientation):
        # occupied_checking
        filling_successful = None
        if cells[row_x, row_y] == 0:
            filling_successful = True
        else:
            print(Bcolors.FAIL + "cell already occupied try new position{} {}".format('\n', cells) + Bcolors.ENDC)
            filling_successful = False

        if filling_successful:
            # adjacent_checking:
            if         ((cells[row_x + 1, row_y + 1] == 0)
                    and (cells[row_x + 0, row_y + 1] == 0)
                    and (cells[row_x + 1, row_y + 0] == 0)
                    and (cells[row_x - 1, row_y - 1] == 0)
                    and (cells[row_x - 1, row_y + 1] == 0)
                    and (cells[row_x + 1, row_y - 1] == 0)
                    and (cells[row_x - 0, row_y - 1] == 0)
                    and (cells[row_x - 1, row_y - 0] == 0)):
                filling_successful = True
            else:
                print(Bcolors.FAIL + "The cell is adjacent to an existing submarine {} {}".format('\n',cells) + Bcolors.ENDC)
                filling_successful = False

        return filling_successful
