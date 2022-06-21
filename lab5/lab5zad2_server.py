#!/usr/bin/env python3
import socket
import random


HOST = '127.0.0.1'
PORT = 2900


print(HOST)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    while True:
      data = conn.recv(1024)
      if not data:
        break
      try:
        number = int(data)
        randNum = random.randint(-100, 100)
        if number == randNum:
            conn.send(b'Liczba ' + str.encode(str(number)) + b' jest rowna wylosowanej przez serwer: ' + str.encode(str(randNum)))
        elif number > randNum:
            conn.send(b'Liczba ' + str.encode(str(number)) + b' jest wieksza wylosowanej przez serwer: ' + str.encode(str(randNum)))
        elif number == randNum:
            conn.send(b'Liczba ' + str.encode(str(number)) + b' jest mniejsza wylosowanej przez serwer: ' + str.encode(str(randNum)))
      except:
          conn.send(b'Prosze wpisac liczbe!')
