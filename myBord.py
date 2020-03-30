import numpy as np
from sympy.core import alphabets
import string
from bord import Bord
from bord import Bcolors
from notebook.notebookapp import raw_input


class MyBord(Bord):
    # generals
    my_cells = np.zeros((Bord.ROW_SIZE + 1, Bord.COLUMN_SIZE + 1), dtype=int)
    for i in range(Bord.ROW_SIZE + 1):
        if i == 0:
            continue
        else:
            my_cells[i, 0] = i
            my_cells[0, i] = i

    # alphabets = string.ascii_lowercase
    # for i in alphabets:
    #         if i >= 'k':
    #             break
    #         print(ord(i) - 96)
    #         my_cells[0, (ord(i)-96)] = i # use np.einsum() to fill np in letters

    def __init__(self):
        print('my bord' '\n', + self.my_cells)
        self.fill_submarines()
        print("my cells full  '\n' {} ".format(self.my_cells))

    def fill_submarines(self):
        for i in range(5, 2, -1):
            # 1. orientatiom
            submarine_orientation = raw_input('choose "V" to vertical submarine or "H" to horizontal submarine')
            submarine_orientation.upper()
            while True:
                try:
                    assert submarine_orientation == 'V' or submarine_orientation == 'H'
                except:
                    print("not valid input ")
                    submarine_orientation = raw_input('choose "V" to vertical submarine or "H" to horizontal submarine')
                    continue
                else:
                    break
            # 2. define stat point and end point
            # a. row start:
            submarine_row_start = raw_input('choose row for the {} size submarine starting point'.format(i))
            submarine_row_start = self.check_input(submarine_row_start)
            # bcolors.HEADER + submarine_row + bcolors.ENDC --> only for strings

            # b. row end
            submarine_row_end = 0
            if (submarine_orientation == 'H'):
                submarine_row_end = raw_input('choose row for the {} size submarine end point'.format(i))
                submarine_row_end = self.check_input(submarine_row_end)

            # checking:
            submarine_row_end = self.length_check(i, submarine_row_start, submarine_row_end)
            submarine_row_start, submarine_row_end = self.collision_or_snap_check(submarine_row_start, submarine_row_end)

            # c. column start
            submarine_column_start = raw_input('choose column for the {} size submarine start point'.format(i))
            submarine_column_start = self.check_input(submarine_column_start)

            # d. column end
            if (submarine_orientation == 'v'):
                submarine_column_end = raw_input('choose column for the {} size submarine end point'.format(i))
                submarine_column_end = self.check_input(submarine_column_end)

            # filling lines:
            if submarine_orientation == 'H':
                for i in range(submarine_row_start, submarine_row_end):
                    self.my_cells[i, submarine_column_start] = 1

            if submarine_orientation == 'V':
                for i in range(submarine_column_start, submarine_column_end):
                    self.my_cells[submarine_row_start, i] = 1

            # more fill checking
            # for i in range()
            #
            # self.my_cells[int(submarine_row), int(submarine_column)] = 1

    def length_check(self, sibmarine_size, submarine_start, submarine_end):
        # checking length
        while True:
            try:
                assert (abs(submarine_start - submarine_end) > sibmarine_size)
                return submarine_end
            except:
                submarine_end = raw_input("rong size try anther parameter set new end point")
                return submarine_end
                continue
            else:
                break

    def collision_or_snap_check(self, row_x, row_y):
        #while True:
        try:
            assert (self.my_cells[row_x,row_y] == 0)
        except:
            print('cell already occupied try new position')
            self.fill_submarines()
            #     continue
            # else:
            #     break
        try:
            assert (self.my_cells[row_x + 1, row_y + 1] == 0)
            assert (self.my_cells[row_x + 0, row_y + 1] == 0)
            assert (self.my_cells[row_x + 1, row_y + 0] == 0)

            assert (self.my_cells[row_x - 1, row_y - 1] == 0)
            assert (self.my_cells[row_x - 0, row_y - 1] == 0)
            assert (self.my_cells[row_x - 1, row_y - 0] == 0)

            assert (self.my_cells[row_x - 1, row_y + 1] == 0)
            assert (self.my_cells[row_x + 1, row_y - 1] == 0)

        except:
            self.fill_submarines()
        return  row_x, row_y