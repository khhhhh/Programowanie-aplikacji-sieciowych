import socket


if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sockIPv4.connect(('172.20.193.97', 2900))

        sockIPv4.send(b"Message")
        retVal = sockIPv4.recv(1024)
        print(retVal)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)

    sockIPv4.close()