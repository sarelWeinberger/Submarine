import numpy as np
from bcolors import Bcolors
from submarine import Submarine
from checkinput import check_input

ROW_SIZE = 10
COLUMN_SIZE = 10


# stage 9:
class Board:
    basic_check = False

    def __init__(self, player_definition):
        '''init graphic cells and indexing the lines'''
        self.board_cells = [[0] * (10 + 1) for i in range(COLUMN_SIZE + 1)]
        for i in range(ROW_SIZE + 1):
            self.board_cells[0][i] = i
            self.board_cells[i][0] = i
        self.all_subs_dead = False
        self.submarine_list = []

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
                show_board(self.board_cells)
                current_submarine = Submarine(i, submarine_name)
                filling_ok = None
                while not filling_ok:
                    current_submarine.fill_submarine_position()
                    filling_ok = self.checking_subs_occupird_or_adjacent_before_filling(current_submarine)

                if filling_ok:
                    current_submarine.define_cells()
                    self.submarine_list.append(current_submarine)
                    self.add_the_submarine_to_board(current_submarine)
        print("filing complete successfully ")

    def checking_subs_occupird_or_adjacent_before_filling(self, current_submarine):
        if current_submarine.submarine_orientation == 'H':
            # checking
            for i in range(current_submarine.submarine_column_start, current_submarine.submarine_column_end):
                not_occupied_position = self.checking_cells_occupie_by_existing_submarine(self.board_cells,
                                                                                          current_submarine.submarine_row_start,
                                                                                          i)
                not_adjacent_position = self.checking_cells_adjacent_to_existing_submarine(self.board_cells,
                                                                                           current_submarine.submarine_row_start,
                                                                                           i)
                if (not not_occupied_position) or (not not_adjacent_position):
                    return False

        if current_submarine.submarine_orientation == 'V':
            # checking
            for i in range(current_submarine.submarine_row_start, current_submarine.submarine_row_end):
                not_occupied_position = self.checking_cells_occupie_by_existing_submarine(self.board_cells, i,
                                                                                          current_submarine.submarine_column_start)

                not_adjacent_position = self.checking_cells_adjacent_to_existing_submarine(self.board_cells, i,
                                                                                           current_submarine.submarine_column_start)
                if (not not_occupied_position) or (not not_adjacent_position):
                    return False
        return True

    def checking_cells_occupie_by_existing_submarine(self, cells, row_x, row_y):
        successful_pos = None
        if cells[row_x][row_y] == 0:
            successful_pos = True
        else:
            print(Bcolors.FAIL + "cell already occupied try new position{} {}".format('\n', cells) + Bcolors.ENDC)
            successful_pos = False
        return successful_pos

    def checking_cells_adjacent_to_existing_submarine(self, cells, row_x, row_y):
        successful_pos = None
        if ((cells[row_x + 1][row_y + 1] == 0)
                and (cells[row_x + 0][row_y + 1] == 0)
                and (cells[row_x + 1][row_y + 0] == 0)
                and (cells[row_x - 1][row_y - 1] == 0)
                and (cells[row_x - 1][row_y + 1] == 0)
                and (cells[row_x + 1][row_y - 1] == 0)
                and (cells[row_x - 0][row_y - 1] == 0)
                and (cells[row_x - 1][row_y - 0] == 0)):
            successful_pos = True
        else:
            print(
                Bcolors.FAIL + "The cell is adjacent to an existing submarine {} {}".format('\n', cells) + Bcolors.ENDC)
            successful_pos = False

        return successful_pos

    def add_the_submarine_to_board(self, current_submarine):
        cell_pos_in_sub = 0
        if current_submarine.submarine_orientation == 'H':
            for j, i in enumerate(
                    range(current_submarine.submarine_column_start, current_submarine.submarine_column_end)):
                self.board_cells[current_submarine.submarine_row_start][i] = 1
                current_submarine.cells_list[j].x = current_submarine.submarine_row_start
                current_submarine.cells_list[j].y = i

                if cell_pos_in_sub != current_submarine.cells_list[cell_pos_in_sub].cell_pos_in_sub:
                    print(f'{cell_pos_in_sub} not follow the submarine position')
                current_submarine.cells_list[cell_pos_in_sub].get_and_return_sub_pos(
                    current_submarine.submarine_row_start, i)
                cell_pos_in_sub += 1

        if current_submarine.submarine_orientation == 'V':
            for j, i in enumerate(range(current_submarine.submarine_row_start, current_submarine.submarine_row_end)):
                self.board_cells[i][current_submarine.submarine_column_start] = 1
                current_submarine.cells_list[j].x = i
                current_submarine.cells_list[j].y = current_submarine.submarine_column_start

                if cell_pos_in_sub != current_submarine.cells_list[cell_pos_in_sub].cell_pos_in_sub:
                    print(f'{cell_pos_in_sub} not follow the submarine position')
                current_submarine.cells_list[cell_pos_in_sub].get_and_return_sub_pos(i,
                                                                                     current_submarine.submarine_column_start)
                cell_pos_in_sub += 1

    def hits(self, pos_x_hit, pos_y_hit):
        if self.board_cells[pos_x_hit][pos_y_hit] == 0:
            self.board_cells[pos_x_hit][pos_y_hit] = 2
            return 0
        if self.board_cells[pos_x_hit][pos_y_hit] == 1:
            sub_destroyed = self.updating_submarine_and_check_if_destroyed(pos_x_hit, pos_y_hit)
            if self.all_subs_dead == True:
                return 1
            if sub_destroyed:
                return 2
            else:
                return 3
            # connect to the sub-object and see if see destroyed
            self.board_grafic_cells[pos_x_hit][pos_y_hit] = 3
            return 4

        if self.board_cells[pos_x_hit][pos_y_hit] == 2:
            return 5

        if self.board_cells[pos_x_hit][pos_y_hit] == 3 or 4:
            return 6

        if self.board_cells[pos_x_hit][pos_y_hit] == 'X':
            return 7

    def updating_submarine_and_check_if_destroyed(self, pos_x_hit, pos_y_hit):
        for sub in self.submarine_list:
            cells_status = 0
            for cell in sub.cells_list:
                if cell.x == pos_x_hit and cell.y == pos_y_hit:
                    cell.cell_hit(True)
                cells_status += cell.cell_status
            if cells_status == 0:
                print(f'submarine {sub.cells_list.submarine_name} destroys')
                self.surround_destroys_submarine(pos_x_hit, pos_y_hit)
                self.check_if_all_destroys()
                return True

    def surround_destroys_submarine(self, row_x, row_y):
        self.board_cells[row_x + 1][row_y + 1] = 'X'
        self.board_cells[row_x + 0][row_y + 1] = 'X'
        self.board_cells[row_x + 1][row_y + 0] = 'X'
        self.board_cells[row_x - 1][row_y - 1] = 'X'
        self.board_cells[row_x - 1][row_y + 1] = 'X'
        self.board_cells[row_x + 1][row_y - 1] = 'X'
        self.board_cells[row_x - 0][row_y - 1] = 'X'
        self.board_cells[row_x - 1][row_y - 0] = 'X'

    def check_if_all_destroys(self):
        total_cells = 0
        for sub in self.submarine_list:
            for cell in sub:
                total_cells += cell.cell_status
        if total_cells == 0:
            self.all_subs_dead = True


    def transform_all_cell_value_to_graphic_char(self, is_praive):
        board_graphic_cells = [[0] * (10 + 1) for i in range(COLUMN_SIZE + 1)]
        for i in range(ROW_SIZE):
            for j in range(COLUMN_SIZE):
                graphic_cell = transform_cell_value_to_graphic_char(self.board_cells[i + 1][j + 1], is_praive)
                board_graphic_cells[i + 1][j + 1] = (graphic_cell)
        return board_graphic_cells


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
    if cell_val == 'X':  # sorrund sub hits
        return 'X'
    else:
        print('not a legal number')
        return 1

def show_board(board_grafic_cells):
    for i in board_grafic_cells:
        print(i)
