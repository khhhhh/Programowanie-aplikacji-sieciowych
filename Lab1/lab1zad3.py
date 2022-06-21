import socket

ip_addr = input()



try:
    socket.inet_aton(ip_addr)
except:
    print(ip_addr+" jest niepoprawny!")
else:
    print(ip_addr+" jest poprawny!")
