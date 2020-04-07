from board import Board


class CompetitorBoard():
    # globals:
    hit_i_index = None
    hit_j_index = None

    def __init__(self,competitor):
         self.competitor = competitor

    def geuss_submarine(self):
        i_index = input('enter row  num for guessing  submarine position - int between 0 and {}'.format(Board.ROW_SIZE))
        i_index = Board.check_input_define_in_the_board(i_index)

        j_index = input('enter column num for guessing  submarine position - int between 0 AND {}'.format(Board.COLUMN_SIZE))
        j_index = Board.check_input_define_in_the_board(j_index)



    # input for the player

    # guess_position(i_index,j_index)
