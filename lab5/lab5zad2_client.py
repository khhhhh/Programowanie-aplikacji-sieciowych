import socket
import random


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 2900
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(5)

    try:
        sockIPv4.connect((HOST, PORT))
        inputMess = input()
        sockIPv4.send(str.encode(inputMess))
        mess = sockIPv4.recv(1024)
        print(mess)
        
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)
