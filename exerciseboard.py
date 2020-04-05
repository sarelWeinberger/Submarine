from board import Board

def create_zeros_list():
    list = [0] * Board.ROW_SIZE
    print(list)
    return list


my_cells_list = [[]]
my_list = []
for i, my_list in enumerate(my_cells_list):
    list = create_zeros_list
    my_cells_list[i] = list  #[[] for i in range(Board.ROW_SIZE)]  # form the Targil definition
print(my_cells_list)

# building board as list of lists:
def build_board_list_of_lists(cells, x, y):
    for rows in my_cells_list:
        for columns in my_cells_list:
            my_cells_list[rows, columns] = cells[x, y]

class BoardForPlayer:

    def fill_exercise_board(self, my_cells_list, is_private):
        cells_as_string = ''
        for row_index, rows in enumerate(my_cells_list):
            # converting from list's to string
            string_rows = str(my_cells_list).strip('[]')
            # adding row index:
            indexed_row = str(row_index) + string_rows
            cells_as_string += indexed_row
            # for column_index, columns in rows:
            #     pass
                #columns.insert(0, column_index)

a = BoardForPlayer()
#a.fill_exercise_board(my_cells_list,True)