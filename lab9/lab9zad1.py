import socket

if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = 'httpbin.org'
    PORT = 80
    message = b"GET /html HTTP/1.1 \r\n" + \
              b"User-agent: Version/7.0.3 Safari/7046A194A \r\n" + \
              b"HOST: httpbin.org \r\n\r\n\r\n"
    try:
        file = open("lab9zad1.html", 'w')
        sockIPv4.connect((HOST, PORT))
        sockIPv4.sendall(message)
        retVal = sockIPv4.recv(8192)
        response = retVal.decode("UTF-8")
        response = response.split("\r\n\r\n")[1]

        file.write(response)
        file.close()

    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)

    sockIPv4.close()