from ast import parse
import socket
import socketserver
import sys


def port_scanner(host, port):
    try:
        my_ip_address = socket.gethostbyname(host)  #get my ip address

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.settimeout(0.5)
    
        s.connect((my_ip_address, port))
        try:
            service = s.recv(1024).decode()
            print(f"Port {port} is open[+] using service {service}")
        except:
            print(f"Port {port} is open [+]")
    except:
        pass


ip_addr = sys.argv[1]
try:
    host = socket.gethostbyaddr(ip_addr)
    for port in range(1,5000):
        port_scanner(host,port)
except:
    pass
