'''
spark.py

Module that contains the CoroBot Spark API

By Keenan Fejeran
1/31/2015
'''

import zmq

#SparkSocket

#def setSocket(socket):
#	SparkSocket = socket

#def sparkConfig():
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:5656")
#print "Connection to Spark confirmed. Ready to send Commands"
#return socket

def drive(speed):
	socket.send("Fastest")

#def drive(speed, socket):
#	socket.send("faster")


