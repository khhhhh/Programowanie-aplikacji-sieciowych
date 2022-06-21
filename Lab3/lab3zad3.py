import socket


if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = open("ip.txt", "r").read().strip()
    PORT = 2900

    try:
        sockIPv4.connect((HOST, PORT))

        while True:
            mess = input()
            sockIPv4.send(mess.encode())
            retVal = sockIPv4.recv(1024)
            print(retVal)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)

    sockIPv4.close()