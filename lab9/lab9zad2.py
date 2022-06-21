import socket
from base64 import b64decode, b64encode

if __name__ == '__main__':
    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = 'httpbin.org'
    PORT = 80
    message = b"GET /image/png HTTP/1.1 \r\n" + \
              b"User-agent: Version/7.0.3 Safari/7046A194A \r\n" + \
              b"HOST: httpbin.org \r\n" + \
              b"accept: image/apng \r\n" + \
              b"\r\n\r\n"
    try:
        file = open("lab9zad2.png", 'wb')
        sockIPv4.connect((HOST, PORT))
        sockIPv4.sendall(message)
        retVal = sockIPv4.recv(8192)
        header = retVal.split(b'\r\n\r\n')[0]
        pic = retVal[len(header)+4:]

        file.write(pic)
        file.close()

    except socket.error as exc:
        print("Wyjatek socket.error : %s" % exc)

    sockIPv4.close()