import re
from bcolors import Bcolors

# stages 4-5:
def check_input(user_input, input_check_type, basic_match=True, Board=None, Submarine=None):
    valid_input = None

    while not valid_input:

        if basic_match:
            if input_check_type == 'orientation':
                pattern = re.compile(r'(h|v)', re.IGNORECASE)
            elif input_check_type == 'player':
                pattern = re.compile(r'(c|s)', re.IGNORECASE)
            elif input_check_type == 'number':
                pattern = re.compile(r'\d')
            else:
                basic_match = False
            match = pattern.match(user_input)

            if match:
                valid_input = True
                if input_check_type != 'number':
                    user_input = user_input.upper()
                else:
                    user_input = int(user_input)
                return user_input
            else:
                valid_input = False
                print(Bcolors.FAIL + "not valid input" + Bcolors.ENDC)
                if input_check_type == 'orientation':
                    user_input = input(
                        Bcolors.OKBLUE + 'choose "V" to vertical submarine or "H" to horizontal submarine' + Bcolors.ENDC)
                if input_check_type == 'player':
                    user_input = input(
                        Bcolors.OKBLUE + 'do you paly as aserver [press "S"] or as a client [press "C"]?' + Bcolors.ENDC)
                if input_check_type == 'number':
                    print(Bcolors.FAIL + 'input is not a number try new input' + Bcolors.ENDC)
                    user_input = input(' try new int - input')
        else:
            pattern = re.compile(r'proportional.to.(the.)?board', re.IGNORECASE)
            match = pattern.search(input_check_type)
            if match:
                user_input = check_input(user_input, 'number')
                if user_input <= 5 and user_input >= 2:
                    valid_input = True
                    return user_input
                else:
                    valid_input = False
                    user_input = input(Bcolors.FAIL + "not valid size, choose size between 2 to 5")
                # TODO: create equation for any size of board
            else:
                pattern = re.compile(r'define.in.(the.)?board', re.IGNORECASE)
                match = pattern.search(input_check_type)
                if match:
                    user_input = check_input(user_input, 'number')
                    if (int(user_input) > 0 and (int(user_input) <= Board.ROW_SIZE)) and (
                            int(user_input) > 0 and (int(user_input) <= Board.COLUMN_SIZE)):
                        valid_input = True
                        return user_input
                    else:
                        valid_input = False
                        print(Bcolors.FAIL + f"Incorrect input, not an int between 0 and {Board.ROW_SIZE}"
                              + Bcolors.ENDC)
                        user_input = input('try new input')
