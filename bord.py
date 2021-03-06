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


class Bord:
    ROW_SIZE = 10
    COLUMN_SIZE = 10
    cells = np.arange(ROW_SIZE, COLUMN_SIZE)

    def check_input(input_index, filling_bord=False, hitting_competitor=False):
        """checking if the input is relevant to the game"""
        while True:
            try:
                in_index = int(input_index)
                assert (int(in_index) > 0 and (int(in_index) <= 10)), "Incorrect input, not an int between 0-10 "
                return in_index
            except Exception as e:
                print(Bcolors.FAIL + str(e.args) + Bcolors.ENDC)
                new_input = raw_input('try new input')
                return int(new_input)
                continue
            else:
                break

        # if filling_bord:
        #     check_filling(in_index)
        # def check_filling(in_index):
        #     pass

    def length_check(submarine_size, submarine_start, submarine_end):
        # checking length
        while True:
            try:
                assert ((submarine_end - submarine_start) == submarine_size)
                return submarine_start, submarine_end
            except:
                print(Bcolors.FAIL +"wrong size" + Bcolors.ENDC)
                submarine_start = raw_input(" try anther parameter set new start point")
                submarine_start = Bord.check_input(submarine_start)
                submarine_end = raw_input(" try anther parameter set new end point")
                submarine_end = Bord.check_input(submarine_end)
                return submarine_start, submarine_end
                continue
            else:
                break

    def orientation_validation(submarine_orientation):
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
                return submarine_orientation
                continue
            else:
                break