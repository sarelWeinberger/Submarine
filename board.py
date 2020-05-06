import numpy as np
from bcolors import Bcolors
from submarine import Submarine
from checkinput import check_input


# stage 9:
class Board:
    ROW_SIZE = 10
    COLUMN_SIZE = 10
    basic_check = False

    # stage 6
    def GetSubsFromPlayer(self):
        biggest_submarine = input("define what is your bigger submarine")
        valid_size_for_the_bigger_submarine = check_input(biggest_submarine, 'proportional_to_the_board',
                                                          Board.basic_check)
        self.fill_board(valid_size_for_the_bigger_submarine)

    def fill_board(self, biggest_submarine):
        for i in range(biggest_submarine, 1, -1):
            num_of_submarines_of_that_size = ((biggest_submarine - i) + 1)
            for j in range(num_of_submarines_of_that_size):
                submarine_name = 'submarine_of_size_{}_number_{}'.format(i, j + 1)
                print("fill {} length , current board: {}, rows \ columns {} {}".format(submarine_name, '\n', '\n',
                                                                                        self.board_cells))
                submarine_name = Submarine(i, submarine_name)
                filling_ok = None
                while not filling_ok:
                    submarine_name.fill_submarine_position()
                    filling_ok = self.checking_subs_occupird_or_adjacent_before_filling(submarine_name)

                if filling_ok:
                    submarine_name.define_cells()
                    self.submarine_list.append(submarine_name)
                    self.add_the_submarine_to_board(submarine_name)
        print("filing complete successfully ")

    def __init__(self, player_definition):
        self.board_cells = np.zeros((self.ROW_SIZE + 1, self.COLUMN_SIZE + 1), dtype=int)

        '''init graphic cells and indexing the lines'''
        self.board_grafic_cells = [[0] * (10 + 1) for i in range(self.COLUMN_SIZE + 1)]
        for i in range(self.ROW_SIZE + 1):
            self.board_cells[i, 0] = i
            self.board_cells[0, i] = i
            self.board_grafic_cells[0][i] = i
            self.board_grafic_cells[i][0] = i
        for i in self.board_grafic_cells:
            print(i)

        self.cell_list = []
        self.all_subs_dead = False
        self.submarine_list = []
        self.player_definition = player_definition  # define if the player is a client or a server
        # TODO: add some condition - when we want the user to THE computer fill the board!!!
        self.GetSubsFromPlayer()
        print("my cells full:  '\n' {} ".format(self.board_cells))



        def hits(self, pos_x_hit, pos_y_hit):
            if self.board_grafic_cells == 0:
                # print('you miss')
                self.board_grafic_cells = 2
                return 'you miss'

            if self.board_cells[pos_x_hit, pos_y_hit] == 1:
                # print('hit succeed')
                sub_destroyed = self.updating_submarine_and_check_if_destroyed(pos_x_hit, pos_y_hit)
                if self.all_subs_dead == True:
                    return ('all subs destroys you won!')
                if sub_destroyed:
                    return 'sub_destroyed!!!'
                else:
                    return 'hit submarine'

                # connect to the sub-object and see if see destroyed
                self.board_cells[pos_x_hit, pos_y_hit] = 3
                return 'your hit succeed'
            if self.board_grafic_cells == 2:
                return ('you already miss this point')

            if self.board_grafic_cells == 3 or 4:
                return ('you already shout and hit this point')

            # if self.all_subs_dead == True:
            #     print('all subs destroys you won!')
            #     return True

        def updating_submarine_and_check_if_destroyed(self, pos_x_hit, pos_y_hit):
            for sub in self.submarine_list:
                cells_status = 0
                for cell in sub.cells_list:
                    if cell.x == pos_x_hit and cell.y == pos_y_hit:
                        cell.cell_hit(True)
                    cells_status += cell.cell_status
                    if cell == 0:
                        print(f'submarine {sub.cells_list.submarine_name} destroys')
                        self.surround_destroys_submarine()
                        return True

        def surround_destroys_submarine(self):
            # TODO: surround destroys subs
            self.chech_if_all_destroys()

        def chech_if_all_destroys(self):
            total_cells = 0
            for sub in self.submarine_list:
                for cell in sub:
                    total_cells += cell.cell_status
            if total_cells == 0:
                self.all_subs_dead = True
                return 'all subs destroys'

    def checking_subs_occupird_or_adjacent_before_filling(self, submarine_name):
        if submarine_name.submarine_orientation == 'H':
            # checking
            for i in range(submarine_name.submarine_column_start, submarine_name.submarine_column_end):
                not_occupied_position = self.checking_cells_adjacent_to_existing_submarine(self.board_cells,
                                                                                            submarine_name.submarine_row_start,
                                                                                            i)
                not_adjacent_position = self.checking_cells__adjacent_to_existing_submarine(self.board_cells, submarine_name.submarine_row_start, i)
                if (not not_occupied_position) or (not not_adjacent_position):
                    return False

        if submarine_name.submarine_orientation == 'V':
            # checking
            for i in range(submarine_name.submarine_row_start, submarine_name.submarine_row_end):
                not_occupied_position = self.checking_cells_adjacent_to_existing_submarine(self.board_cells, i,
                                                                                            submarine_name.submarine_column_start)

                not_adjacent_position = self.checking_cells__adjacent_to_existing_submarine(self.board_cells, i, submarine_name.submarine_column_start)
                if(not not_occupied_position) or (not not_adjacent_position):
                    return False

        return True

    def add_the_submarine_to_board(self, submarine_obj):
        cell_pos_in_sub = 0
        if submarine_obj.submarine_orientation == 'H':
            for j,i in enumerate(range(submarine_obj.submarine_column_start, submarine_obj.submarine_column_end)):
                self.board_cells[submarine_obj.submarine_row_start, i] = 1
                submarine_obj.cells_list[j].x = submarine_obj.submarine_row_start
                submarine_obj.cells_list[j].y = i

                # fill SubCell
                # check
                if cell_pos_in_sub != submarine_obj.cells_list[cell_pos_in_sub].cell_pos_in_sub:
                    print(f'{cell_pos_in_sub} not follow the submarine position')
                submarine_obj.cells_list[cell_pos_in_sub].get_and_return_sub_pos(submarine_obj.submarine_row_start, i)
                cell_pos_in_sub += 1

        if submarine_obj.submarine_orientation == 'V':
            for j,i in enumerate(range(submarine_obj.submarine_row_start, submarine_obj.submarine_row_end)):
                self.board_cells[i, submarine_obj.submarine_column_start] = 1
                submarine_obj.cells_list[j].x = i
                submarine_obj.cells_list[j].y = submarine_obj.submarine_column_start

                # fill SubCell
                # check
                if cell_pos_in_sub != submarine_obj.cells_list[cell_pos_in_sub].cell_pos_in_sub:
                    print(f'{cell_pos_in_sub} not follow the submarine position')
                submarine_obj.cells_list[cell_pos_in_sub].get_and_return_sub_pos(i, submarine_obj.submarine_column_start)
                cell_pos_in_sub += 1

    def checking_cells_adjacent_to_existing_submarine(self, cells, row_x, row_y):
        successful_pos = None
        if cells[row_x, row_y] == 0:
            successful_pos = True
        else:
            print(Bcolors.FAIL + "cell already occupied try new position{} {}".format('\n', cells) + Bcolors.ENDC)
            successful_pos = False
        return successful_pos

    def checking_cells__adjacent_to_existing_submarine(self, cells, row_x, row_y):
        successful_pos = None
        if ((cells[row_x + 1, row_y + 1] == 0)
                    and (cells[row_x + 0, row_y + 1] == 0)
                    and (cells[row_x + 1, row_y + 0] == 0)
                    and (cells[row_x - 1, row_y - 1] == 0)
                    and (cells[row_x - 1, row_y + 1] == 0)
                    and (cells[row_x + 1, row_y - 1] == 0)
                    and (cells[row_x - 0, row_y - 1] == 0)
                    and (cells[row_x - 1, row_y - 0] == 0)):
            successful_pos = True
        else:
            print(Bcolors.FAIL + "The cell is adjacent to an existing submarine {} {}".format('\n',cells) + Bcolors.ENDC)
            successful_pos = False

        return successful_pos

    def transform_all_cell_value_to_graphic_char(self, is_praive):
        for i in range(Board.ROW_SIZE):
            for j in range(Board.COLUMN_SIZE):
                graphic_cell = transform_cell_value_to_graphic_char(self.board_cells[i+1, j+1], is_praive)
                self.board_grafic_cells[i+1][j+1] = graphic_cell
        print('from board_grafic_cells method ')
        return self.board_grafic_cells


def transform_cell_value_to_graphic_char(cell_val, is_praive):
    if cell_val == 0:  # empty / unchecked
        return '.'
    elif cell_val == 1:  # has submarine in the cell
        if is_praive:
            return 0
        else:  # the competitor board - unchecked
            return '.'
    elif cell_val == 2:  # miss hit
        return '*'
    elif cell_val == 3:  # hits the sub
        return '@'
    elif cell_val == 4:  # destroyed sub
        return '#'
    else:
        print('not a legal number')
        return 1





