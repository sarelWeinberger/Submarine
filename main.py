from notebook.notebookapp import raw_input
from  board import Bcolors
from myborad import MyBorad
from competitorboard import CompetitorBoard
import re
from competitorboard import CompetitorBoard

def check_server_or_client_input(input_valid):
    valid_input = None
    while not valid_input:
        pattern = re.compile(r'(c|s)', re.IGNORECASE)
        match = pattern.match(input_valid)
        if match:
            valid_input = True
            input_valid = input_valid.upper()
            return input_valid
        else:
            valid_input = False
            print(Bcolors.FAIL + "not valid input" + Bcolors.ENDC)
            input_valid = input(Bcolors.OKBLUE + 'do you paly as aserver [press "S"] or as a client [press "C"]?' + Bcolors.ENDC)

if __name__ == '__main__':
    server_or_client = input(Bcolors.OKBLUE + 'do you paly as aserver [press "S"] or as a client [press "C"]?' +  Bcolors.ENDC)
    server_or_client = check_server_or_client_input(server_or_client)

    player_wins = None
    my_bord = MyBorad(server_or_client)
    competitor_bord = CompetitorBoard()

    while not player_wins:
        pass

    competitor = raw_input(Bcolors.OKBLUE + 'define your competitor: press 1 to computer and 2 to anther player' +  Bcolors.ENDC)

    competitor_bord = CompetitorBoard(competitor)
