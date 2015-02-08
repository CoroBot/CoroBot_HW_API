'''
SparkControl.py

The CoroBot Spark API

By: KMF
1/31/2015
'''

#imports
import zmq

#ZMQ Setup
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:5656") #change to connect to pi<->hat broker

#defines for controlling spark

#######################################################
#motorDir(motornum, direction)
#Sets the direction for the motor indicated.
#inputs: motornum is the motor to set
#        direction is either forward or reverse, 1 or 0 respectively
#returns: none
def motorDir(motornum, direction):
	socket.send_multipart(["MOT", str(motornum), "DIR", str(direction)])
	#add functionality to read motor direction?
	#if direction == NULL:
	#	send a request to read motor status instead and return value
	
	#OR, do we need to write two methods, get/setMotorDir() ?

def motorPWM(motornum, duty_cycle):
	socket.send_multipart(["MOT", str(motornum), "SPEED", str(duty_cycle)])

def ID():
	socket.send_multipart(["ID", "1", "TYPE"]) #should the second "part" be static? 
											   #or is this a special case?
											   
	msg = socket.recv() #if server responds with more than one msg, this needs work
	return msg

def version():
	socket.send_multipart(["ID", "1", "VERSION"])
	return socket.recv()
	
def cameraPWR(power):
	socket.send_multipart(["CAM", "1", "PWR", str(power)])

	
