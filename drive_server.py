'''
drive_server.py

Listens for commands from a client and responds
to a limited set of requests.

By Keenan Fejeran
1/31/2015
'''

import zmq

#Firmware Constants
VERSION = "0.1"
TYPE = "SPARK_0.5"

#Create context and socket
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5656")

print "Server ready for commands."

#listen for commands
while True:
	#block until message recieved
	msg = socket.recv()
	
	#decypher commands
	print msg
	#print str(socket.getsockopt(zmq.RCVMORE)) #testing SNDMORE flag
	'''
	if "VERSION" in msg:
		socket.send(VERSION)
	elif "TYPE" in msg:
		socket.send(TYPE)
	else: print msg 
	'''
