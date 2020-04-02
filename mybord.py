import numpy as np
from bord import Bord
from submarine import Submarine


class MyBord():
    # generals
    my_cells = np.zeros((Bord.ROW_SIZE + 1, Bord.COLUMN_SIZE + 1), dtype=int)
    for i in range(Bord.ROW_SIZE + 1):
        my_cells[i, 0] = i
        my_cells[0, i] = i

    def __init__(self):

        # TODO: add some condition - when we want the user to fill the bord!!!
        for i in range(5, 1, -1):
            submarine_name = 'submarine_' + str(i)
            print("fill {} length , current bord: {}, rows \ columns {} {}".format(submarine_name,'\n', '\n',self.my_cells))
            submarine_name = Submarine(i, submarine_name)
            submarine_name.fill_submarine_request()
            MyBord.checking_before_filling(submarine_name)
            if submarine_name.checking_ok:
                MyBord.position_the_submarine(submarine_name)

        print("my cells full:  '\n' {} ".format(MyBord.my_cells))

    @classmethod
    def checking_before_filling(cls, submarine_name):
        if submarine_name.submarine_orientation == 'H':
            # checking
            for i in range(submarine_name.submarine_column_start, submarine_name.submarine_column_end):
                filling_successful = Bord.collision_or_snap_check(cls.my_cells, submarine_name.submarine_row_start, i,
                                                                  submarine_name.submarine_orientation)
                while not filling_successful:
                    submarine_name.fill_submarine_request()
                    filling_successful = MyBord.checking_before_filling(submarine_name)
                    if filling_successful:
                        submarine_name.checking_ok = True
                        return filling_successful
                        break


        if submarine_name.submarine_orientation == 'V':
            # checking
            for i in range(submarine_name.submarine_row_start, submarine_name.submarine_row_end):
                filling_successful = Bord.collision_or_snap_check(cls.my_cells, i, submarine_name.submarine_column_start,
                                                                  submarine_name.submarine_orientation)
                while not filling_successful:
                    submarine_name.fill_submarine_request()
                    filling_successful = MyBord.checking_before_filling(submarine_name)
                    if filling_successful:
                        submarine_name.checking_ok = True
                        return filling_successful
                        break

        if filling_successful:
            submarine_name.checking_ok = True
            return filling_successful

    @classmethod
    def position_the_submarine(cls, submarine_name):

        if submarine_name.submarine_orientation == 'H':
            for i in range(submarine_name.submarine_column_start, submarine_name.submarine_column_end):
                cls.my_cells[submarine_name.submarine_row_start, i] = 1

        if submarine_name.submarine_orientation == 'V':
            for i in range(submarine_name.submarine_row_start, submarine_name.submarine_row_end):
                cls.my_cells[i, submarine_name.submarine_column_start] = 1
                first_itaration = False
