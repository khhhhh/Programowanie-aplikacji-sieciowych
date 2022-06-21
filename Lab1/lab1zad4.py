import socket

ip_addr = input()



try:
    host_name = socket.gethostbyaddr(ip_addr)
    print(ip_addr + " jest poprawny, nazwa hosta: " + host_name[0])
except:
    print("Host nie został znaleziony.")