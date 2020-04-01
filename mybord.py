import numpy as np
from sympy.core import alphabets
from bord import Bord
from bord import Bcolors
from notebook.notebookapp import raw_input

class MyBord(Bord):
    # generals
    my_cells = np.zeros((Bord.ROW_SIZE + 1, Bord.COLUMN_SIZE + 1), dtype=int)
    for i in range(Bord.ROW_SIZE + 1):
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

        #TODO: add some condition - when we want the user to fill the bord!!!
        for i in range(5, 1, -1):
            submarine_name = 'submarine_' + str(i)
            print(submarine_name)
            submarine_name = self.MySubmarine(i, submarine_name)
        print("my cells full  '\n' {} ".format(self.my_cells))

    class MySubmarine:
        submarine_length = 0
        submarine_name = ''

        def __init__(self, submarine_len, sub_name):
            self.submarine_length = submarine_len
            self.submarine_name = sub_name
            self.fill_submarine()
            print(MyBord.my_cells)

        def fill_submarine(self):

            self.filling_successful = True

            # 1. orientation
            submarine_orientation = raw_input(Bcolors.OKBLUE +'choose "V" to vertical submarine or "H" to horizontal submarine' + Bcolors.ENDC)
            submarine_orientation = Bord.orientation_validation(submarine_orientation)

            # 2. define stat point and end point
            # a. row start:
            submarine_row_start = raw_input(Bcolors.OKGREEN +
                'choose row for the {} size submarine starting point - the small number in the index'.format(
                    self.submarine_name)+ Bcolors.ENDC)
            submarine_row_start = Bord.check_input(submarine_row_start)

            # b. row end
            if (submarine_orientation == 'V'):
                submarine_row_end = raw_input(Bcolors.OKGREEN +
                    'choose row for the {} size submarine end point - the big number in the index'.format(
                        self.submarine_name) + Bcolors.ENDC)
                submarine_row_end = Bord.check_input(submarine_row_end)
                submarine_row_start, submarine_row_end = Bord.length_check(self.submarine_length,
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
                submarine_column_start, submarine_column_end = Bord.length_check(self.submarine_length,
                                                                            submarine_column_start,
                                                                            submarine_column_end)

            # filling lines:

            first_itaration = True
            if submarine_orientation == 'H':
                # checking
                for i in range(submarine_column_start, submarine_column_end):
                    self.collision_or_snap_check(submarine_row_start, i, submarine_orientation, first_itaration)
                # filling
                if self.filling_successful == True:
                    for i in range(submarine_column_start, submarine_column_end):
                        MyBord.my_cells[submarine_row_start, i] = 1
                        first_itaration = False
                else:
                    self.fill_submarine()


            if submarine_orientation == 'V':
                # checking
                for i in range(submarine_row_start, submarine_row_end):
                    self.collision_or_snap_check(i, submarine_column_start, submarine_orientation, first_itaration)
                # filling
                if self.filling_successful == True:
                    for i in range(submarine_row_start, submarine_row_end):
                        MyBord.my_cells[i, submarine_column_start] = 1
                        first_itaration = False
                else:
                    self.fill_submarine()
        # TODO: PASS TO BORD CALLS --> GENERAL METHOD (self.fill_submarine() from except, deflate false and became true if method get to te end )
        def collision_or_snap_check(self, row_x, row_y, oriantation, first_itaration):
                # collision
                try:
                    assert (MyBord.my_cells[row_x, row_y] == 0)
                except:
                    print(Bcolors.FAIL + 'cell already occupied try new position' + Bcolors.ENDC)
                    self.filling_successful == False

                # snap:
                try:
                    assert (MyBord.my_cells[row_x + 1, row_y + 1] == 0)
                    assert (MyBord.my_cells[row_x + 0, row_y + 1] == 0)
                    assert (MyBord.my_cells[row_x + 1, row_y + 0] == 0)

                    assert (MyBord.my_cells[row_x - 1, row_y - 1] == 0)

                    assert (MyBord.my_cells[row_x - 1, row_y + 1] == 0)
                    assert (MyBord.my_cells[row_x + 1, row_y - 1] == 0)

                    #print(MyBord.my_cells)
                    if first_itaration:
                        assert (MyBord.my_cells[row_x - 0, row_y - 1] == 0)
                        assert (MyBord.my_cells[row_x - 1, row_y - 0] == 0)
                    elif oriantation == 'V' and first_itaration == False:
                        assert (MyBord.my_cells[row_x - 0, row_y - 1] == 0)
                    elif oriantation == 'H' and first_itaration == False:
                        assert (MyBord.my_cells[row_x - 1, row_y - 0] == 0)
                    self.filling_successful = True
                except:
                    print(Bcolors.FAIL + 'The cell is adjacent to an existing submarine'+ Bcolors.ENDC)
                    self.filling_successful = False

