from re import I
import socket

if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sockIPv4.connect(('212.182.24.27', 2901))
        sockIPv4.send(b"Test")
        answer = sockIPv4.recv(1024)
        print(answer)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)


    sockIPv4.close()