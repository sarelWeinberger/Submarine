import socket
import pickle
from board import Board
FORMAT = 'utf-8'
PORT_NUM = 5050
import board

class Server:
    def __init__(self):
        # 1. creating socket obj and define it's protocol:
        my_socket = socket.socket(socket.AF_INET,  # ipv4
                                  socket.SOCK_STREAM)  # tcp

        # 2. get specific ip and port for the socket
        my_socket.bind(
            (socket.gethostname(), PORT_NUM))  # gethostname -> ip from this program ,  port_num -> port number

        # 3. start listening with a QUEUE length:
        my_socket.listen(10)

        # init server board:
        server_bord = Board('S')
        server_bord.GetSubsFromPlayer()
        self.dead = False
        my_grafic_board = server_bord.transform_all_cell_value_to_graphic_char(True)
        board.show_board(my_grafic_board)

        while True:
            client_socket, address = my_socket.accept()
            print(f'connection from socket {address} ,ipv4, succeed')

            connection = True
            while connection:


                other_grafic_board = server_bord.transform_all_cell_value_to_graphic_char(False)
                grafic_to_send = pickle.dumps(other_grafic_board)

                # 1. sending the board condition
                try:
                    client_socket.send(grafic_to_send)# --> THE PRIVET VERSION
                except:
                    print('seding grafig board problem')

                # 2. asking for hitting gassing
                msg_pos_x = pickle.dumps('DEFINE X POS FOR HIT')
                try:
                    client_socket.send(msg_pos_x) #(bytes('DEFINE X POS FOR HIT'), encoding='utf8')
                except Exception as e:
                    print(e.args)
                # try:
                #     hit_position_X = client_socket.recv(2048).decode(FORMAT) # TODO: PASS A HEADER OF MESSAGE SIZE, create new thread
                #except:
                try:
                    hit_position_X = client_socket.recv(1024)
                    hit_position_X = pickle.loads(hit_position_X)

                    if hit_position_X: # checking massage is valid in the first time
                        hit_position_X = int(hit_position_X)

                except Exception as e:
                    print(e.args)
                # try:
                #     client_socket.send(bytes('DIFINE Y POS FOR HIT'), encoding=FORMAT)
                # except:
                try:
                    msg_pos_y =  pickle.dumps('DEFINE y POS FOR HIT')
                    client_socket.send(msg_pos_y)

                # try:
                #     hit_position_Y = client_socket.recv(2048).decode(FORMAT)
                # except:
                    hit_position_Y = client_socket.recv(1024)
                    hit_position_Y = pickle.loads(hit_position_Y)

                    hit_position_Y = int(hit_position_Y)
                except:
                    input('pos y error')

                try:
                    if hit_position_X and hit_position_Y:
                        msg = server_bord.hits(hit_position_X, hit_position_Y)
                        msg = pickle.dumps(msg)
                        client_socket.send(msg)

                except Exception as e:
                        print(f'general position input problem, {e.args}')
                        #connection = False;

                # geiitng the same q from the client (in application level)
                if server_bord.all_subs_dead == True:
                     self.dead = True
                     print("client won!!!")
                     client_socket.send(bytes('you win the game!!'), FORMAT)
                     connection = False;
                     client_socket.close()
        client_socket.close()
