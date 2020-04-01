from notebook.notebookapp import raw_input
from mybord import MyBord
from competitorbord import CompetitorBord


if __name__ == '__main__':

    my_bord = MyBord()

    competitor = raw_input('define your competitor: press 1 to computer and 2 to anther player')

    competitor_bord = CompetitorBord()
