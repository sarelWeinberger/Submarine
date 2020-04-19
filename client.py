import socket
import pickle
from myborad import MyBorad

PORT_NUM = 5050
FORMAT = 'utf-8'

class Clinent:

    def __init__(self):
        print('starting')
        ip = socket.gethostname()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, PORT_NUM))
        #client_socket.setblocking(False)
        # user_name = input('your name:')
        #client_socket.send(user_name.encode(FORMAT))

        while True:
            msg = client_socket.recv(1024)  # num of bits stream
            decode_msg = ''
            get_input = True
            try:
                decode_msg = pickle.loads(msg)
                for i ,line in enumerate(decode_msg):
                    if isinstance(line, list):
                        get_input = False
                        print(f"{line}")
                if get_input:
                    print(decode_msg)
                    msg = input('get input')
                    #TODO: CHECK INPUT
                    msg = pickle.dumps(msg)
                    client_socket.send(msg)

            except:
                #client_socket.send(bytes('DEFINE X POS FOR HIT'), 'utf8')
                decode_msg = str(msg, FORMAT)
                print(decode_msg)
                msg = input('input' + decode_msg)
                print(msg)
            # check input
                msg = bytes(msg, FORMAT)
                client_socket.send(msg)
                    #client_socket.send(msg)
                #print('leaving the app')
                    #print(msg.decode("utf-8"))
