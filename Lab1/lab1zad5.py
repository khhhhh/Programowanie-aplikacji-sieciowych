import socket

host_name = input()



try:
    ip_addr = socket.gethostbyname(host_name)
    print("Host "+ host_name + " jest poprawny, ip address: ")
    print(ip_addr)
except:
    print("IP address nie został znaleziony.")