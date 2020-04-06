from notebook.notebookapp import raw_input
from  board import Bcolors
from myborad import MyBorad
from competitorboard import CompetitorBoard
import re

def check_server_or_client_input(input):
    valid_input = None
    while not valid_input:
        pattern = re.compile(r'(c|s)', re.IGNORECASE)
        match = pattern.match(input)
        if match:
            valid_input = True
            input = input.upper()
            return input
        else:
            valid_input = False
            print(Bcolors.FAIL + "not valid input" + Bcolors.ENDC)
            input = raw_input(Bcolors.OKBLUE + 'choose "V" to vertical submarine or "H" to horizontal submarine' + Bcolors.ENDC)

if __name__ == '__main__':
    server_or_client = raw_input('do you paly as aserver [press "S"] or as a client [press "C"]?')
    server_or_client = check_server_or_client_input(server_or_client)

    my_bord = MyBorad(server_or_client)

    competitor = raw_input('define your competitor: press 1 to computer and 2 to anther player')

    competitor_bord = CompetitorBoard(competitor)
