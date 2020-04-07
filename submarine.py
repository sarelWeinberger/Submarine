from board import Bcolors
from notebook.notebookapp import raw_input
from board import Board


class Submarine:

    def __init__(self, submarine_len, sub_name):
        self.checking_ok = False
        self.submarine_length = submarine_len
        self.submarine_name = sub_name

        self.submarine_orientation = ''
        self.submarine_row_start = 0
        self.submarine_row_end = 0
        self.submarine_column_start = 0
        self.submarine_column_end = 0

    def fill_submarine_request(self):
        self.__init__(self.submarine_length, self.submarine_name)
        # 1. orientation
        self.submarine_orientation = raw_input(
            Bcolors.OKBLUE + 'choose "V" to vertical submarine or "H" to horizontal ' + self.submarine_name + Bcolors.ENDC)
        self.submarine_orientation = Board.submarine_orientation_input_validation(self.submarine_orientation)

        # 2. define stat point and end point
        # a. row start:
        self.submarine_row_start = raw_input(Bcolors.OKGREEN +
                                             'choose row for the {} size submarine starting point - the small number in the index'.format(
                                                 self.submarine_name) + Bcolors.ENDC)
        self.submarine_row_start = Board.check_input_define_in_the_board(self.submarine_row_start)

        # b. row end
        if self.submarine_orientation == 'V':
            self.submarine_row_end = raw_input(Bcolors.OKGREEN +
                                               'choose row for the {} size submarine end point - the big number in the index'.format(
                                                   self.submarine_name) + Bcolors.ENDC)
            self.submarine_row_end = Board.check_input_define_in_the_board(self.submarine_row_end)
            submarine_row_start, submarine_row_end = Board.submarine_legal_length_check(self.submarine_length,
                                                                                        self.submarine_row_start, self.submarine_row_end)

        # c. column start
        self.submarine_column_start = raw_input(
            'choose column for the {} size submarine start point - the small number in the index'.format(
                self.submarine_name))
        self.submarine_column_start = Board.check_input_define_in_the_board(self.submarine_column_start)

        # d. column end
        if self.submarine_orientation == 'H':
            self.submarine_column_end = raw_input(
                'choose column for the {} size submarine end point - the big number in the index'.format(
                    self.submarine_name))
            self.submarine_column_end = Board.check_input_define_in_the_board(self.submarine_column_end)
            submarine_column_start, submarine_column_end = Board.submarine_legal_length_check(self.submarine_length,
                                                                                              self.submarine_column_start,
                                                                                              self.submarine_column_end)





