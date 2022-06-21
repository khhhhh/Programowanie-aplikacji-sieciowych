import socket


if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sockIPv4.connect(('212.182.24.27', 2900))

        while True:
            mess = input()
            sockIPv4.send(mess)
            retVal = sockIPv4.recv(1024)
            print(retVal)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)

    sockIPv4.close()