from notebook.notebookapp import raw_input
from board import Board

class CompetitorBord(Board):
    # globals:
    hit_i_index = None
    hit_j_index = None

    def geuss_submarine(self):
        i_index = raw_input('enter row  num for guessing  submarine position - int between 0-9')
        i_index =self.check_input_define_in_the_board(i_index)

        j_index = raw_input('enter column num for guessing  submarine position - int between 0-9')
        j_index = self.check_input_define_in_the_board(j_index)



    def guess_position(self, i_pos, j_pos, is_praive):

        if is_praive:
            pass

        # if (submarine[i_pos][j_pos] == 0):  # empty
        #     print('empty')
        #     submarine[i_pos][j_pos] == '.'
        # elif (submarine[i_pos][j_pos] == 1):  # hit submarine
        #     print('hit submarine')
        #     submarine[i_pos][j_pos] == '0'
        # elif (submarine[i_pos][j_pos] == 2):  # submarine
        #     submarine[i_pos][j_pos] == '0'
        # elif (submarine[i][j] == 3):  # submarine
        # elif (submarine[i][j] == 4):  # submarine
        else:
            print('not a legal number')
            return 1

    # input for the player

    # guess_position(i_index,j_index)