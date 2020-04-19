import socket
from myborad import MyBorad
import pickle

FORMAT = 'utf-8'
PORT_NUM = 5050
class Server:
    def __init__(self):
        # 1. creating socket obj and define it's protocol:
        my_socket = socket.socket(socket.AF_INET,  # ipv4
                                  socket.SOCK_STREAM)  # tcp

        #my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. get specific ip and port for the socket
        my_socket.bind(
            (socket.gethostname(), PORT_NUM))  # gethostname -> ip from this program ,  port_num -> port number

        # 3. start listening with a que length:
        my_socket.listen(10)

        # init server board:
        server_bord = MyBorad('S')
        self.dead = False
        first_itatation = True

        grafic_board = server_bord.transform_all_cell_value_to_graphic_char(True)
        while True:
            client_socket, address = my_socket.accept()
            print(f'connection from socket {address} ,ipv4, succeed')

            # if first_itatation:
            #     client_socket.send(bytes("welcome to the server player!", "utf-8"))
            #first_itatation = False

            connection = True
            while connection:
                # 1. sending the board condition
                grafic_board = server_bord.transform_all_cell_value_to_graphic_char(True)
                # for i in grafic_board:
                #     print(i)

                grafic_to_send = pickle.dumps(grafic_board)
                # for i in grafic_to_send:
                #     print(i)
                client_socket.send(grafic_to_send)# --> THE PRIVET VERSION

                # 2. asking for hitting gassing
                msg_pos_x = pickle.dumps('DEFINE X POS FOR HIT')
                client_socket.send(msg_pos_x) #(bytes('DEFINE X POS FOR HIT'), encoding='utf8')
                # try:
                #     hit_position_X = client_socket.recv(2048).decode(FORMAT) # TODO: PASS A HEADER OF MESSAGE SIZE, create new thread
                #except:
                hit_position_X = client_socket.recv(1024)
                hit_position_X = pickle.loads(hit_position_X)

                if hit_position_X: # checking massage is valid in the first time
                    hit_position_X = int(hit_position_X)

                # try:
                #     client_socket.send(bytes('DIFINE Y POS FOR HIT'), encoding=FORMAT)
                # except:
                msg_pos_y =  pickle.dumps('DEFINE y POS FOR HIT')
                client_socket.send(msg_pos_y)
                # try:
                #     hit_position_Y = client_socket.recv(2048).decode(FORMAT)
                # except:
                hit_position_Y = client_socket.recv(1024)
                hit_position_Y = pickle.loads(hit_position_Y)

                hit_position_Y = int(hit_position_Y)

                server_bord.hits(hit_position_X, hit_position_Y)

                # geiitng the same q from the client (in application level)
                if server_bord.all_subs_dead == True:
                     self.dead = True
                     print("client won!!!")
                     client_socket.send(bytes('you win the gmae!!'), FORMAT)
                     connection = False;
                     client_socket.close()
