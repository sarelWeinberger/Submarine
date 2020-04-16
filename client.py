import socket
from myborad import MyBorad

PORT_NUM = 5050

class Clinent:
    def __init__(self):
        ip = socket.gethostname()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, PORT_NUM))

        #client_bord = MyBorad('C')

        msg = client_socket.recv(1024)  # num of bits stream
        print(msg.decode("utf-8"))
