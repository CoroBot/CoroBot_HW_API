'''
drive_client.py

A development space for the CoroBot Spark API

Sends zmq calls to a local server

By Keenan Fejeran
1/31/2015
'''

import zmq
#import spark


#Create a context and socket
context = zmq.Context()
socket = context.socket(zmq.PAIR)

#connect to server
socket.connect("tcp://localhost:5656")

def drive(speed):
	socket.send('MOT', zmq.SNDMORE)
	socket.send(speed)
	print "drive() done"

#send multipart zmq messages?

#begin motor method
#spark.drive(
drive("Fast")
