import socket
from myborad import MyBorad

FORMAT = 'utf-8'
PORT_NUM = 5050
class Server:
    def __init__(self):
        # 1. creating socket obj and define it's protocol:
        my_socket = socket.socket(socket.AF_INET,  # ipv4
                                  socket.SOCK_STREAM)  # tcp

        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. get specific ip and port for the socket
        my_socket.bind(
            (socket.gethostname(), PORT_NUM))  # gethostname -> ip from this program ,  port_num -> port number

        # 3. start listening with a que length:
        my_socket.listen(4)

        # init server board:
        server_bord = MyBorad('S')
        self.dead = False
        first_itatation = True

        while True:
            client_socket, address = my_socket.accept()
            print(f'connection from socket {client_socket} ,ipv4 {address} succeed')
            if first_itatation:
                client_socket.send(bytes("welcome to the server player!", "utf-8"))
            first_itatation = False

            connection = True
            while connection:
                # 1. sending the board condition
                client_socket.send(bytes(server_bord.transform_cell_value_to_graphic_char(True)), FORMAT) # --> THE PRIVET VERSION

                # 2. asking for hitting gassing
                client_socket.send(bytes('DIFINE X POS FOR HIT'),FORMAT)
                hit_position_X = client_socket.recv(2048).decode(FORMAT) # TODO: PASS A HEADER OF MESSAGE SIZE, create new thread
                if hit_position_X: # checking massage is valid in the first time
                    hit_position_X = int(hit_position_X)

                client_socket.send(bytes('DIFINE Y POS FOR HIT'), FORMAT)
                hit_position_Y = client_socket.recv(2048).decode(FORMAT)
                hit_position_Y = int(hit_position_Y)

                server_bord.cell_list(hit_position_X,hit_position_Y)

                # geiitng the same q from the client (in application level)
                if server_bord.all_subs_dead == True:
                     self.dead = True
                     print("client won!!!")
                     client_socket.send(bytes('you win the gmae!!'), FORMAT)
                     connection = False;
                     client_socket.close()
