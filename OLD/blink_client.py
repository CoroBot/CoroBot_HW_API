'''
blink_client.py

Communicates with a server to control a remote Arduino LED.

By Keenan Fejeran
1/28/2015
'''

import zmq
import time

#Create a context and socket
context = zmq.Context()
socket = context.socket(zmq.PAIR)

#Connect socket to server
socket.connect("tcp://localhost:5556")

#Send messages to server and listen to response

while True:
	socket.send("C2S" + time.ctime())
	msg = socket.recv()
	print msg
	time.sleep(1)
