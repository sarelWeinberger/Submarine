import numpy as np
from board import Board
from submarine import Submarine
from notebook.notebookapp import raw_input
from checkinput import check_input

class MyBorad(Board):
    # generals
    is_private = True
    basic_check = False

    def __init__(self, player_definition):
        self.cell_list = []
        self.all_subs_dead = False

        self.player_definition = player_definition # define if the player is a client or a server
        # TODO: add some condition - when we want the user to fill the board!!!
        self.GetSubsFromPlayer()
        print("my cells full:  '\n' {} ".format(self.board_cells))

    # stage 6, move to board?
    def GetSubsFromPlayer(self):
        biggest_submarine = input("define what is your bigger submarine")
        valid_size_for_the_bigger_submarine = check_input(biggest_submarine, 'proportional_to_the_board',MyBorad.basic_check)
        self.fill_board(valid_size_for_the_bigger_submarine)

    def fill_board(self,biggest_submarine):
        for i in range(biggest_submarine, 1, -1):
            num_of_submarines_of_that_size = ((biggest_submarine - i) + 1)
            for j in range(num_of_submarines_of_that_size):
                submarine_name = 'submarine_of_size_{}_number_{}'.format(i,j+1)
                print("fill {} length , current board: {}, rows \ columns {} {}".format(submarine_name, '\n', '\n',
                                                                                    self.board_cells))
                submarine_name = Submarine(i, submarine_name)
                filling_ok = None
                while not filling_ok:
                    submarine_name.fill_submarine_position()
                    filling_ok = MyBorad.checking_before_filling(submarine_name)

                if filling_ok:
                    self.cell_list = submarine_name.define_cells()
                    MyBorad.add_the_submarine_to_board(submarine_name, self.cell_list)
        print("filing complete successfully ")

    def hits(self,pos_x,pos_y):
        if self.board_cells[pos_x,pos_y] == 1:
            print('hit succeed')
            # connect to the sub-object and see if see destroyed
            self.board_cells[pos_x,pos_y] = 3
        else:
            print('you miss')
        if self.all_subs_dead == True:
            print('all subs destroys you won!')
            return True
