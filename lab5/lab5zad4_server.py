#!/usr/bin/env python3
import socket

HOST = '127.0.0.1'
PORT = 2900

print(HOST)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            conn.sendall(data)
            break

print("END")

HOST = '127.0.0.1'
PORT = 2903

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    bytesAddressPair = s.recvfrom(1024)
    mess = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(mess)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    s.sendto(clientMsg.encode(), address)
