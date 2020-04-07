import numpy as np
from board import Board
from submarine import Submarine
from notebook.notebookapp import raw_input


class MyBorad():
    # generals
    is_praive = True
    my_cells = Board.board_cells

    def __init__(self, player_definition):

        self.player_definition = player_definition # define if the player is a client or a server
        # TODO: add some condition - when we want the user to fill the board!!!
        self.GetSubsFromPlayer()
        print("my cells full:  '\n' {} ".format(MyBorad.my_cells))

    def GetSubsFromPlayer(self):
        biggest_submarine = raw_input("define what is your bigger submarine")
        valid_size_for_the_bigger_submarine = Board.check_bigger_submarine_size_proportional_to_the_board(biggest_submarine)
        self.fill_board(valid_size_for_the_bigger_submarine)

    def fill_board(self,biggest_submarine):
        for i in range(biggest_submarine, 1, -1):
            num_of_submarines_of_that_size = ((biggest_submarine - i) + 1)
            for j in range(num_of_submarines_of_that_size):
                submarine_name = 'submarine_of_size_{}_number_{}'.format(i,j+1)
                print("fill {} length , current board: {}, rows \ columns {} {}".format(submarine_name, '\n', '\n',
                                                                                    self.my_cells))
                submarine_name = Submarine(i, submarine_name)
                filling_ok = None
                while not filling_ok:
                    submarine_name.fill_submarine_position()
                    filling_ok = MyBorad.checking_before_filling(submarine_name)

                if filling_ok:
                    submarine_name.define_all_cells_positive()
                    MyBorad.position_the_submarine_on_my_board(submarine_name)

    @classmethod
    def checking_before_filling(cls, submarine_name):
        if submarine_name.submarine_orientation == 'H':
            # checking
            for i in range(submarine_name.submarine_column_start, submarine_name.submarine_column_end):
                filling_successful = Board.checking_cells_occupied_or_adjacent_to_existing_submarine(cls.my_cells, submarine_name.submarine_row_start, i,
                                                                                                     submarine_name.submarine_orientation)
                if not filling_successful:
                   return False

        if submarine_name.submarine_orientation == 'V':
            # checking
            for i in range(submarine_name.submarine_row_start, submarine_name.submarine_row_end):
                filling_successful = Board.checking_cells_occupied_or_adjacent_to_existing_submarine(cls.my_cells, i, submarine_name.submarine_column_start,
                                                                                                     submarine_name.submarine_orientation)
                if not filling_successful:
                    return False

        return True


    @classmethod
    def position_the_submarine_on_my_board(cls, submarine_name):

        if submarine_name.submarine_orientation == 'H':
            for i in range(submarine_name.submarine_column_start, submarine_name.submarine_column_end):
                cls.my_cells[submarine_name.submarine_row_start, i] = 1

        if submarine_name.submarine_orientation == 'V':
            for i in range(submarine_name.submarine_row_start, submarine_name.submarine_row_end):
                cls.my_cells[i, submarine_name.submarine_column_start] = 1
                first_itaration = False
