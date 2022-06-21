import socket


if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIPv4.settimeout(5)

    try:
        sockIPv4.connect(('ntp.task.gda.pl', 13))
        retDate = sockIPv4.recv(1024)
        print(retDate)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)
