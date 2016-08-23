#!/usr/bin/python

import socket
import sys
from time import sleep

HOST = "localhost"
PORT = 5632


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



try:
	sock.connect((HOST,PORT))
	sock.sendall("Request Tempature")
	print(sock.recv(1024))
	sock.close()
	del sock

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST,PORT))
#	sock.sendall("Set Target:20")
#	print(sock.recv(1024))
	sock.close()
	del sock

        sock3.connect((HOST,PORT))
	sock3.sendall("Set Mode")
	print(sock3.recv(1024))
	sock3.close()

finally:
	print("End")
	
	


