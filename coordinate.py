from bcolors import Bcolors
from checkinput import check_input
#from board import Board


# stage 5:
class Size(): # TODO: IMPORT BOARD SIZE when size can change wihout cirular
    ROW_SIZE = 10
    COLUMN_SIZE = 10

def get_coordinate(name='', basic_check=False):
    pos_x = input(
        Bcolors.OKGREEN + f'choose row for the {name} size submarine starting point - the small number in the index' + Bcolors.ENDC)
    pos_x = check_input(pos_x, 'define_in_board', basic_check,Size)
    pos_y = input(f'choose column for the {name} size submarine start point - the small number in the index')
    pos_y = check_input(pos_y, 'define_in_board', basic_check,Size)

    return pos_x, pos_y
