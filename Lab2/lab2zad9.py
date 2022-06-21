import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            s.sendto("2+2".encode(), ('212.182.24.27', 2902))
            answer = s.recv(1024)
            print(answer)
    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)


    s.close()