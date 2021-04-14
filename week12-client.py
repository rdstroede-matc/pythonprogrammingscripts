#!/usr/bin/env python3
import socket

RHOST = '127.0.0.1'
RPORT = 50007
SND_DATA = ''
while SND_DATA != 'Quit':
	SND_DATA = input("Enter your message here. Type Quit to exit.")

	C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	C_SOCK.connect((RHOST, RPORT))

	#Put the pattern you want to send here.
	C_SOCK.send(bytearray(SND_DATA,'utf8')) 

	RCV_DATA = C_SOCK.recv(1024)
	print(RCV_DATA)

	C_SOCK.close()
