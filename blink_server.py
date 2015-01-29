'''
blink_server.py

A server that talks zmq on one end, and pyserial on the other.
Controls an LED on a local RPi via commands over zmq.

By Keenan Fejeran
1/20/2015
'''

import zmq
import serial
import time

#Print the current version of zmq
print "pyzmq version: " + zmq.pyzmq_version()

#Open a serial port (note could be a command line arg)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 0)
print ser.name

#Create a ZMQ context
context = zmq.Context()

#Create ZMQ socket, bind it to localhost (for testing)
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5556")


#listen to the client, passing a trivial message to arduino
while True:
	msg = socket.recv()
	print "server recieved " + msg
	socket.send("reply from server from hearing \""+msg+"\"")
	ser.write("hello")
	time.sleep(1)


''' 
pyserial setup?
context
socket - type
loop
block on recv
reply with command recieved: <command>
if command was "on/off" toggle led
'''
