import socket
import time
from tracemalloc import start


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 2900
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(5)

    try:
        sockIPv4.connect((HOST, PORT))
        startTime = time.time()
        sockIPv4.send(b'time test TCP')
        mess = sockIPv4.recv(1024)
        elapsedTime = time.time() - startTime
        print('TCP = ', elapsedTime)
        
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)


    HOST = '127.0.0.1'
    PORT = 2903
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        startTime = time.time()
        sockIPv4.sendto(b'time test UDP', (HOST, PORT))
        mess = sockIPv4.recvfrom(1024)
        elapsedTime = time.time() - startTime
        print('UDP = ', elapsedTime)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)
    sockIPv4.close()