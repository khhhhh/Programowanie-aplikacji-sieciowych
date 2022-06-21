from re import I
import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            mess = input()
            s.sendto(mess.encode(), ('212.182.24.27', 2901))
            print("Connected!")
            answer = s.recv(1024)
            print(answer)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)


    s.close()