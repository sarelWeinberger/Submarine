import numpy as np
from sympy.core import alphabets
import string
from bord import Bord
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

    def fill_submarines(self):
        i = 5
        while i > 2:
            for j in i:
                submarine_row = raw_input('choose row for the {} size submarine'.format(i))
                submarine_column = raw_input('choose column for the {} size submarine'.format(i))
