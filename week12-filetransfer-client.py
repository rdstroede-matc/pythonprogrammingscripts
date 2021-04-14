#!/usr/bin/env python3
import socket


hFile = open("test.txt", "r")
listfiletext = hFile.readlines()
print(listfiletext)
print(type(listfiletext))
print(len(listfiletext))
hFile.close()

RHOST = '127.0.0.1'
RPORT = 5000
SND_DATA = str(listfiletext)

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

#Put the pattern you want to send here.
C_SOCK.send(bytearray(SND_DATA,'utf8')) 

RCV_DATA = C_SOCK.recv(1024)
print(RCV_DATA)

C_SOCK.close()
