import numpy as np
from sympy.core import alphabets
from bord import Bord
from bord import Bcolors
from notebook.notebookapp import raw_input


def length_check(submarine_size, submarine_start, submarine_end):
    # checking length
    while True:
        try:
            assert ((submarine_end - submarine_start) == submarine_size)
            return submarine_start, submarine_end
        except:
            print("wrong size")
            submarine_start = raw_input(" try anther parameter set new start point")
            submarine_start = Bord.check_input(submarine_start)
            submarine_end = raw_input(" try anther parameter set new end point")
            submarine_end = Bord.check_input(submarine_end)
            return submarine_start, submarine_end
            continue
        else:
            break


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
        print('my bord: {} rows \ columns {} {}'.format('\n', '\n', self.my_cells))
        for i in range(5, 1, -1):
            submarine_name = 'submarine_' + str(i)
            print(submarine_name)
            submarine_name = self.MySubmarine(i, submarine_name)
            print(self.my_cells)
        print("my cells full  '\n' {} ".format(self.my_cells))

    class MySubmarine:
        submarine_length = 0
        submarine_name = ''

        def __init__(self, submarine_len, sub_name):
            self.submarine_length = submarine_len
            self.submarine_name = sub_name
            self.fill_submarine()

        def fill_submarine(self):
            # 1. orientation
            submarine_orientation = raw_input('choose "V" to vertical submarine or "H" to horizontal submarine')
            submarine_orientation.upper()

            # validation
            while True:
                try:
                    assert submarine_orientation == 'V' or submarine_orientation == 'H'
                except:
                    print("not valid input")
                    submarine_orientation = raw_input(
                        'choose "V" to vertical submarine or "H" to horizontal submarine')
                    continue
                else:
                    break

            # 2. define stat point and end point
            # a. row start:
            submarine_row_start = raw_input(
                'choose row for the {} size submarine starting point - the small number in the index'.format(
                    self.submarine_name))
            submarine_row_start = Bord.check_input(submarine_row_start)
            # bcolors.HEADER + submarine_row + bcolors.ENDC --> only for strings

            # b. row end
            submarine_row_end = 0
            if (submarine_orientation == 'V'):
                submarine_row_end = raw_input(
                    'choose row for the {} size submarine end point - the big number in the index'.format(
                        self.submarine_name))
                submarine_row_end = Bord.check_input(submarine_row_end)
                submarine_row_start, submarine_row_end = length_check(self.submarine_length,
                                                                      submarine_row_start, submarine_row_end)

            # c. column start
            submarine_column_start = raw_input(
                'choose column for the {} size submarine start point - the small number in the index'.format(
                    self.submarine_name))
            submarine_column_start = Bord.check_input(submarine_column_start)

            # d. column end
            if (submarine_orientation == 'H'):
                submarine_column_end = raw_input(
                    'choose column for the {} size submarine end point - the big number in the index'.format(
                        self.submarine_name))
                submarine_column_end = Bord.check_input(submarine_column_end)
                submarine_column_start, submarine_column_end = length_check(self.submarine_length,
                                                                            submarine_column_start,
                                                                            submarine_column_end)

            # filling lines:
            first_itaration = True
            if submarine_orientation == 'H':
                for i in range(submarine_column_start, submarine_column_end):
                    self.collision_or_snap_check(submarine_row_start, i, submarine_orientation, first_itaration)
                    MyBord.my_cells[submarine_row_start, i] = 1
                    first_itaration = False

            if submarine_orientation == 'V':
                for i in range(submarine_row_start, submarine_row_end):
                    self.collision_or_snap_check(i, submarine_column_start, submarine_orientation, first_itaration)
                    MyBord.my_cells[i, submarine_column_start] = 1
                    first_itaration = False

            # more fill checking
            # for i in range()
            #
            # self.my_cells[int(submarine_row), int(submarine_column)] = 1

        def collision_or_snap_check(self, row_x, row_y, oriantation, first_itaration):
            while True:
                try:
                    assert (MyBord.my_cells[row_x, row_y] == 0)
                except:
                    print('cell already occupied try new position')
                    self.fill_submarine()
                    continue
                else:
                    break

            while True:
                try:
                    assert (MyBord.my_cells[row_x + 1, row_y + 1] == 0)
                    assert (MyBord.my_cells[row_x + 0, row_y + 1] == 0)
                    assert (MyBord.my_cells[row_x + 1, row_y + 0] == 0)

                    assert (MyBord.my_cells[row_x - 1, row_y - 1] == 0)

                    assert (MyBord.my_cells[row_x - 1, row_y + 1] == 0)
                    assert (MyBord.my_cells[row_x + 1, row_y - 1] == 0)

                    print(MyBord.my_cells)
                    if first_itaration:
                        assert (MyBord.my_cells[row_x - 0, row_y - 1] == 0)
                        assert (MyBord.my_cells[row_x - 1, row_y - 0] == 0)
                    elif oriantation == 'V' and first_itaration == False:
                        assert (MyBord.my_cells[row_x - 0, row_y - 1] == 0)
                    elif oriantation == 'H' and first_itaration == False:
                        assert (MyBord.my_cells[row_x - 1, row_y - 0] == 0)

                except:
                    print('The cell is adjacent to an existing submarine')
                    self.fill_submarine()
                    continue
                else:
                    break
