import socket


if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(5)

    try:
        sockIPv4.connect(('172.217.20.163', 80))
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)
