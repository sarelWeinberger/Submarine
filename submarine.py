from bcolors import Bcolors
#from board import Board
import numpy as np
from checkinput import check_input
from coordinate import get_coordinate


class Submarine:
    basic_check = False

    def __init__(self, submarine_len, sub_name):
        self.checking_ok = False
        self.submarine_length = submarine_len
        self.submarine_name = sub_name
        self.cells_list = np.zeros(submarine_len)
        self.submarine_orientation = ''
        self.submarine_row_start = 0
        self.submarine_row_end = 0
        self.submarine_column_start = 0
        self.submarine_column_end = 0
        self.is_dead = False
        self.cells_list = []

    def fill_submarine_position(self):
        self.__init__(self.submarine_length, self.submarine_name)
        # 1. orientation
        self.submarine_orientation = input(
            Bcolors.OKBLUE + 'choose "V" to vertical submarine or "H" to horizontal ' + self.submarine_name + Bcolors.ENDC)
        self.submarine_orientation = check_input(self.submarine_orientation, 'orientation')

        # 2. define stat point and end point
        # a. row and column start point:
        self.submarine_row_start, self.submarine_column_start = get_coordinate(self.submarine_name,
                                                                               Submarine.basic_check)

        # b. row end
        if self.submarine_orientation == 'V':
            self.submarine_row_end = self.submarine_row_start + self.submarine_length

        # c. column end
        if self.submarine_orientation == 'H':
            self.submarine_column_end = self.submarine_column_start + self.submarine_length

    def define_cells(self):
        self.cells_list = [SubCell() for i in range(self.submarine_length)]
        for i, cell in enumerate(self.cells_list):
            cell.cell_status = 1
            cell.oriantation = self.submarine_orientation
            cell.submarine_name = self.submarine_name
            cell.submarine_lenght = self.submarine_length
            cell.cell_pos_in_sub = i

        return self.cells_list

    #stage 8:
    def hit(self, pos):
        self.cells_list[pos] = 0
        if self.cells_list.sum() == 0:
            self.is_dead = True


# stage 7:
class SubCell:
    def __init__(self):
        self.oriantation = ''
        self.x = 0
        self.y = 0
        self.cell_status = 0
        self.submarine_name = ''
        self.submarine_lenght = 0
        self.cell_pos_in_sub = 0
        self.legal_cell = not(self.isAdjacent())
        self.hit = False

    def SetSub(self, new_status):
        self.cell_status = new_status

    def get_and_return_sub_pos(self, x, y):
        self.x = x
        self.y = y

    def cell_hit(self, hit):
        if hit:
            self.cell_status = 0
            self.hit = True

    def isAdjacent(self):
        #this method is not relvant to the subcell obj bat to the board.
        return False
