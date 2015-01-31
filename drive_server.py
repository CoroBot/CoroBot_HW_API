'''
drive_server.py

Listens for commands from a client and prints
a string based on the command.

By Keenan Fejeran
1/31/2015
'''

import zmq

#Create context and socket
context = zmq.Context()

socket = context.socket(zmq.PAIR)

socket.bind("tcp://*:5656")

print "Server ready for commands."

#listen for commands
while True:
	msg = socket.recv()
	#decypher commands
	print msg
