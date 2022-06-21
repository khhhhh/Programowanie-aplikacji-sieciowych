from re import I
import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(5)

    HOST = open("ip.txt", "r").read().strip()
    PORT = 2901

    try:
        operation = input("Wpisz hostname:")
        s.sendto(operation.encode(), (HOST, PORT))
        answer = s.recv(1024)
        print(answer)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)


    s.close()