from  board import Bcolors
from competitorboard import CompetitorBoard
from checkinput import check_input
from server import Server
from client import Clinent
from myborad import MyBorad


def run_server():
    player1 = Server()

def run_client():
    player2 = Clinent()

if __name__ == '__main__':
    # stage 10:

    server_or_client = input('do you play as a server [press "S"] or as a client [press "C"]?' )
    server_or_client = check_input(server_or_client, 'player')

    if server_or_client == 'S':
        run_server()
    if server_or_client == 'C':
        run_client()

    # player_wins = None
    #
    #
    # # while not player_wins:
    # #     pass
    #
    # competitor = input(Bcolors.OKBLUE + 'define your competitor: press 1 to computer and 2 to anther player' +  Bcolors.ENDC)
    #
    # competitor_bord = CompetitorBoard(competitor)


