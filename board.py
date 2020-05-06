import numpy as np
from bcolors import Bcolors


# stage 9:
class Board:
    ROW_SIZE = 10
    COLUMN_SIZE = 10

    def __init__(self):
        self.board_cells = np.zeros((self.ROW_SIZE + 1, self.COLUMN_SIZE + 1), dtype=int)
        self.board_grafic_cells = []

        self.board_grafic_cells = [[0] * (10 + 1) for i in range(self.COLUMN_SIZE + 1)]
        for i in range(self.ROW_SIZE + 1):
            self.board_cells[i, 0] = i
            self.board_cells[0, i] = i
            self.board_grafic_cells[0][i] = i
            self.board_grafic_cells[i][0] = i
        for i in self.board_grafic_cells:
            print(i)

    def checking_before_filling(self, submarine_name):
        if submarine_name.submarine_orientation == 'H':
            # checking
            for i in range(submarine_name.submarine_column_start, submarine_name.submarine_column_end):
                filling_successful = Board.checking_cells_occupied_or_adjacent_to_existing_submarine(self.board_cells,
                                                                                                     submarine_name.submarine_row_start,
                                                                                                     i)
                if not filling_successful:
                    return False

        if submarine_name.submarine_orientation == 'V':
            # checking
            for i in range(submarine_name.submarine_row_start, submarine_name.submarine_row_end):
                filling_successful = Board.checking_cells_occupied_or_adjacent_to_existing_submarine(self.board_cells, i,
                                                                                                     submarine_name.submarine_column_start
                                                                                                     )
                if not filling_successful:
                    return False

        return True

    def add_the_submarine_to_board(self, submarine_name):
        cell_pos_in_sub = 0
        if submarine_name.submarine_orientation == 'H':
            for j,i in enumerate(range(submarine_name.submarine_column_start, submarine_name.submarine_column_end)):
                self.board_cells[submarine_name.submarine_row_start, i] = 1
                submarine_name.cells_list[j].x = submarine_name.submarine_row_start
                submarine_name.cells_list[j].y = i

                # fill SubCell
                # check
                if cell_pos_in_sub != submarine_name.cells_list[cell_pos_in_sub].cell_pos_in_sub:
                    print(f'{cell_pos_in_sub} not follow the submarine position')
                submarine_name.cells_list[cell_pos_in_sub].get_and_return_sub_pos(submarine_name.submarine_row_start, i)
                cell_pos_in_sub += 1

        if submarine_name.submarine_orientation == 'V':
            for j,i in enumerate(range(submarine_name.submarine_row_start, submarine_name.submarine_row_end)):
                self.board_cells[i, submarine_name.submarine_column_start] = 1
                submarine_name.cells_list[j].x = i
                submarine_name.cells_list[j].y = submarine_name.submarine_column_start

                # fill SubCell
                # check
                if cell_pos_in_sub != submarine_name.cells_list[cell_pos_in_sub].cell_pos_in_sub:
                    print(f'{cell_pos_in_sub} not follow the submarine position')
                submarine_name.cells_list[cell_pos_in_sub].get_and_return_sub_pos(i, submarine_name.submarine_column_start)
                cell_pos_in_sub += 1

    @staticmethod # now that we use the cell as instance of board we can change it to obj.method
    def checking_cells_occupied_or_adjacent_to_existing_submarine(cells, row_x, row_y):
        # occupied_checking
        filling_successful = None
        if cells[row_x, row_y] == 0:
            filling_successful = True
        else:
            print(Bcolors.FAIL + "cell already occupied try new position{} {}".format('\n', cells) + Bcolors.ENDC)
            filling_successful = False

        if filling_successful:
            # adjacent_checking:
            if ((cells[row_x + 1, row_y + 1] == 0)
                    and (cells[row_x + 0, row_y + 1] == 0)
                    and (cells[row_x + 1, row_y + 0] == 0)
                    and (cells[row_x - 1, row_y - 1] == 0)
                    and (cells[row_x - 1, row_y + 1] == 0)
                    and (cells[row_x + 1, row_y - 1] == 0)
                    and (cells[row_x - 0, row_y - 1] == 0)
                    and (cells[row_x - 1, row_y - 0] == 0)):
                filling_successful = True
            else:
                print(Bcolors.FAIL + "The cell is adjacent to an existing submarine {} {}".format('\n',
                                                                                                  cells) + Bcolors.ENDC)
                filling_successful = False

        return filling_successful

    def transform_all_cell_value_to_graphic_char(self, is_praive):
        #print(Board.board_grafic_cells)
        for i in range(Board.ROW_SIZE):
            for j in range(Board.COLUMN_SIZE):
                # Board.board_grafic_cells[i][j] = '0'
                # TODO: ADDING INDEX FOR THE GRAPIC EXHIBITION OF ROWS AND COLUMNS
                cell_val = Board.board_cells[i+1, j+1]
                grapic_cell = transform_cell_value_to_graphic_char(Board.board_cells[i+1, j+1], is_praive)
                self.board_grafic_cells[i+1][j+1] = grapic_cell
        print('from board_grafic_cells method ')
        # for i in  Board.board_grafic_cells:
        #     print(i)
        return Board.board_grafic_cells


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



