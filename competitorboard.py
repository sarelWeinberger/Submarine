from notebook.notebookapp import raw_input
from board import Board

class CompetitorBoard(Board):
    # globals:
    hit_i_index = None
    hit_j_index = None

    def geuss_submarine(self):
        i_index = raw_input('enter row  num for guessing  submarine position - int between 0-9')
        i_index =self.check_input_define_in_the_board(i_index)

        j_index = raw_input('enter column num for guessing  submarine position - int between 0-9')
        j_index = self.check_input_define_in_the_board(j_index)



    def guess_position(self,submarine, i_pos, j_pos, is_praive):

        if submarine[i_pos][j_pos] == 0:  # empty / unchecked
            return '.'
        elif submarine[i_pos][j_pos] == 1:
            if is_praive:
                return 0
            else: # the competitor board
                return '.'
        elif submarine[i_pos][j_pos] == 2:
            return '*'
        elif submarine[i_pos][j_pos] == 3:
            return '@'
        elif submarine[i_pos][j_pos] == 4:
            return '#'
        else:
            print('not a legal number')
            return 1

    # input for the player

    # guess_position(i_index,j_index)