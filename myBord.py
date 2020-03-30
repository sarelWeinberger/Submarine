import numpy as np
from sympy.core import alphabets
import string
from bord import Bord
from bord import bcolors
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
            submarine_row_start = raw_input('choose row for the {} size submarine starting point'.format(i))
            submarine_row_start = self.check_input(submarine_row_start)
            # more fill checking
            # bcolors.HEADER + submarine_row + bcolors.ENDC --> only for strings

            submarine_row_end = 0
            if (submarine_orientation == 'H'):
                submarine_row_end = raw_input('choose row for the {} size submarine end point'.format(i))
                submarine_row_end = self.check_input(submarine_row_end)

            submarine_column_start = raw_input('choose column for the {} size submarine end point'.format(i))
            submarine_column_start = self.check_input(submarine_column_start)
            # more fill checking
            self.check_filling(i, submarine_row_start, submarine_row_end )

            if (submarine_orientation == 'v'):
                submarine_column_end = raw_input('choose column for the {} size submarine end point'.format(i))
                submarine_column_end = self.check_input(submarine_column_end)

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

    def check_filling(self, sibmarine_size, submarine_row_start, submarine_row_end):
        self.check_input_size()


        def check_input_size():
            try:
              assert( abs(submarine_row_start - submarine_row_end) > sibmarine_size)
            except:
                new_end_point = raw_input("rong size try anther parameter set new end point")
            return new_end_point
