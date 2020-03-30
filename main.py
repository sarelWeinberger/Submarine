from notebook.notebookapp import raw_input
import  MyBord
import  CompetitorBord

if __name__ == '__main__':

    my_bord = MyBord()

    competitor = raw_input('define your competitor: press 1 to computer and 2 to anther player')
    # check input

    competitor_bord = CompetitorBord()
