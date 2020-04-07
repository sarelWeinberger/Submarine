from notebook.notebookapp import raw_input
from myborad import MyBorad
from competitorboard import CompetitorBoard


if __name__ == '__main__':

    my_bord = MyBorad()

    competitor = raw_input('define your competitor: press 1 to computer and 2 to anther player')

    competitor_bord = CompetitorBoard()
