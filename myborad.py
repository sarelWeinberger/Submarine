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
        self.submarine_list = []

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
                    submarine_name.define_cells()
                    self.submarine_list.append(submarine_name)
                    MyBorad.add_the_submarine_to_board(submarine_name)
        print("filing complete successfully ")

    def hits(self, pos_x_hit, pos_y_hit):
        if self.board_grafic_cells == 0:
            #print('you miss')
            self.board_grafic_cells = 2
            return 'you miss'

        if self.board_cells[pos_x_hit, pos_y_hit] == 1:
            #print('hit succeed')
            sub_destroyed = self.updating_submarine_and_check_if_destroyed(pos_x_hit, pos_y_hit)
            if self.all_subs_dead == True:
                return ('all subs destroys you won!')
            if sub_destroyed:
                return 'sub_destroyed!!!'
            else:
                return 'hit submarine'

            # connect to the sub-object and see if see destroyed
            self.board_cells[pos_x_hit, pos_y_hit] = 3
            return 'hit succeed'
        if self.board_grafic_cells == 2:
            return ('you already miss this point')

        if self.board_grafic_cells == 3 or 4:
            return ('you already shout and hit this point')

        # if self.all_subs_dead == True:
        #     print('all subs destroys you won!')
        #     return True

    def updating_submarine_and_check_if_destroyed(self,pos_x_hit,pos_y_hit):
        for sub in self.submarine_list:
            for cell in sub.cells_list:
                if cell.x == pos_x_hit and cell.y == pos_y_hit:
                    cell.cell_hit(True)
            if sum(sub.cells_list.cell_status) == 0:
                print(f'submarine {sub.cells_list.submarine_name} destroys')
                self.surround_destroys_submarine()
                return True

    def surround_destroys_submarine(self):
        #TODO: surround destroys subs
        self.chech_if_all_destroys()

    def chech_if_all_destroys(self):
        total_cells = 0
        for sub in self.submarine_list:
            total_cells += sum(sub.cells_list.cell_status)
        if total_cells == 0:
            self.all_subs_dead = True
            return 'all subs destroys'

