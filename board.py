import numpy as np
from bcolors import Bcolors


# stage 9:
class Board:
    ROW_SIZE = 10
    COLUMN_SIZE = 10
    board_cells = np.zeros((ROW_SIZE + 1, COLUMN_SIZE + 1), dtype=int)
    for i in range(ROW_SIZE + 1):
        board_cells[i, 0] = i
        board_cells[0, i] = i

    board_grafic_cells = [[]]

    @classmethod
    def checking_before_filling(cls, submarine_name):
        if submarine_name.submarine_orientation == 'H':
            # checking
            for i in range(submarine_name.submarine_column_start, submarine_name.submarine_column_end):
                filling_successful = Board.checking_cells_occupied_or_adjacent_to_existing_submarine(cls.board_cells,
                                                                                                     submarine_name.submarine_row_start,
                                                                                                     i)
                if not filling_successful:
                    return False

        if submarine_name.submarine_orientation == 'V':
            # checking
            for i in range(submarine_name.submarine_row_start, submarine_name.submarine_row_end):
                filling_successful = Board.checking_cells_occupied_or_adjacent_to_existing_submarine(cls.board_cells, i,
                                                                                                     submarine_name.submarine_column_start
                                                                                                     )
                if not filling_successful:
                    return False

        return True

    @classmethod
    def add_the_submarine_to_board(cls, submarine_name, cell_list):
        cell_pos_in_sub = 0
        if submarine_name.submarine_orientation == 'H':
            for i in range(submarine_name.submarine_column_start, submarine_name.submarine_column_end):
                cls.board_cells[submarine_name.submarine_row_start, i] = 1

                # fill SubCell
                # check
                if cell_pos_in_sub != cell_list[cell_pos_in_sub].cell_pos_in_sub:
                    print(f'{cell_pos_in_sub} not follow the submarine position')
                cell_list[cell_pos_in_sub].get_and_return_sub_pos(submarine_name.submarine_row_start, i)
                cell_pos_in_sub += 1

        if submarine_name.submarine_orientation == 'V':
            for i in range(submarine_name.submarine_row_start, submarine_name.submarine_row_end):
                cls.board_cells[i, submarine_name.submarine_column_start] = 1

                # fill SubCell
                # check
                if cell_pos_in_sub != cell_list[cell_pos_in_sub].cell_pos_in_sub:
                    print(f'{cell_pos_in_sub} not follow the submarine position')
                cell_list[cell_pos_in_sub].get_and_return_sub_pos(i, submarine_name.submarine_column_start)
                cell_pos_in_sub += 1

    @staticmethod
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
        for i in range(Board.ROW_SIZE):
            for j in range(Board.COLUMN_SIZE):
                # TODO: ADDING INDEX FOR THE GRAPIC EXHIBITION OF ROWS AND COLUMNS
                Board.board_grafic_cells[i, j] = Board.transform_cell_value_to_graphic_char(Board.board_cells[i,j],is_praive)

    @staticmethod
    def transform_cell_value_to_graphic_char(cell_val, is_praive):

        if cell_val == 0:  # empty / unchecked
            return '.'
        elif cell_val == 1: # has submarine in the cell
            if is_praive:
                return 0
            else:  # the competitor board - unchecked
                return '.'
        elif cell_val == 2: # miss hit
            return '*'
        elif cell_val == 3: # hits the sub
            return '@'
        elif cell_val == 4: # destroyed sub
            return '#'
        else:
            print('not a legal number')
            return 1
