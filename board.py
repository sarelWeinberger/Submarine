import numpy as np
from notebook.notebookapp import raw_input



class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Board:
    ROW_SIZE = 10
    COLUMN_SIZE = 10

    @staticmethod
    def check_input_define_in_the_board(input_index, hitting_competitor=False):
        """checking if the input is relevant to the game"""
        new_input = None
        while True:
            try:
                if new_input is None:
                    in_index = int(input_index)
                else:
                    in_index = int(new_input)
                assert (int(in_index) > 0 and (int(in_index) <= Board.ROW_SIZE))
                return in_index
            except Exception as e:
                print(Bcolors.FAIL + str(e.args) + "Incorrect input, not an int between 0 and {}".format(
                    Board.ROW_SIZE) + Bcolors.ENDC)
                new_input = raw_input('try new input')
                continue
            else:
                break

    @staticmethod
    def submarine_legal_length_check(submarine_size, submarine_start, submarine_end):
        # checking length
        while True:
            try:
                assert ((submarine_end - submarine_start) == submarine_size)
                return submarine_start, submarine_end
            except:
                print(Bcolors.FAIL + "wrong submarine size should be size of {}".format(submarine_size) + Bcolors.ENDC)
                submarine_start = raw_input(" try anther parameter set new start point")
                submarine_start = Board.check_input_define_in_the_board(submarine_start)
                submarine_end = raw_input(" try anther parameter set new end point")
                submarine_end = Board.check_input_define_in_the_board(submarine_end)
                continue
            else:
                break

    @staticmethod
    def submarine_orientation_input_validation(submarine_orientation):
        submarine_orientation = submarine_orientation.upper()
        while True:
            try:
                assert submarine_orientation == 'V' or submarine_orientation == 'H'
                return submarine_orientation
            except:
                print("not valid input")
                submarine_orientation = raw_input(Bcolors.OKBLUE +
                                                  'choose "V" to vertical submarine or "H" to horizontal submarine' + Bcolors.ENDC)
                submarine_orientation = submarine_orientation.upper()
                continue
            else:
                break

    @staticmethod
    def checking_cells_occupied_or_adjacent_to_existing_submarine(cells, row_x, row_y, orientation):
        # occupied_checking
        filling_successful = False
        try:
            assert (cells[row_x, row_y] == 0)
            filling_successful = True
        except Exception as e:
            print(Bcolors.FAIL + "cell already occupied try new position{} {}, {}".format('\n', cells, e.args) + Bcolors.ENDC)

        if filling_successful:
            # adjacent_checking:
            try:
                assert (cells[row_x + 1, row_y + 1] == 0)
                assert (cells[row_x + 0, row_y + 1] == 0)
                assert (cells[row_x + 1, row_y + 0] == 0)

                assert (cells[row_x - 1, row_y - 1] == 0)

                assert (cells[row_x - 1, row_y + 1] == 0)
                assert (cells[row_x + 1, row_y - 1] == 0)

                assert (cells[row_x - 0, row_y - 1] == 0)
                assert (cells[row_x - 1, row_y - 0] == 0)

                filling_successful = True
            except Exception as e:
                print(
                    Bcolors.FAIL + "The cell is adjacent to an existing submarine {} {}, {}".format('\n',
                                                                                                cells, e.args) + Bcolors.ENDC)
                filling_successful = False

        return filling_successful
