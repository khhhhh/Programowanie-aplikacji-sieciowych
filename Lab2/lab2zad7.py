from ast import parse
import socket
import sys


var_host_name = sys.argv[1]
var_port = sys.argv[2]
host_port_tuple = (var_host_name, int(var_port))
s = socket.socket()
print(var_host_name, var_port)
try:
    result = s.connect(host_port_tuple)
    print(s.getsockname())
    print(s.getsockopt())
    print("Connected!")
except:
    print("Not connected!")