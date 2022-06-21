from base64 import encode
import socket


if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = open("ip.txt", "r").read().strip()
    PORT = 29000
    try:
        mess = input("Wpisz wiadomość:").encode()
        if len(mess) > 20:
            # mess = mess[0:19]
            pass
        elif len(mess) < 20:
            strr = " " * (20 - len(mess))
            print(type(strr))
            mess = b''.join([mess, strr.encode()])
        sockIPv4.connect((HOST, PORT))
        sockIPv4.send(mess)
        retVal = sockIPv4.recv(1024)
        print(retVal)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)

    sockIPv4.close()