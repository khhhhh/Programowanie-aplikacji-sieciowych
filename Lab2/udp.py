import socket

if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockIPv6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

    sockIPv4.close()
    sockIPv6.close()