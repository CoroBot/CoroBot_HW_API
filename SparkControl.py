'''
SparkControl.py

The CoroBot Spark API

By: Keenan Fejeran
3/27/2015
'''

#imports
import zmq
import time

#global constants
TIMEOUT = 500 #milliseconds to wait for a reply to a command

TIMEOUT_ERROR = -1 #indicates that a response was required, but didn't come in time.
		   #If this error is returned, there's no guarantee the robot got the command.

ARGUMENT = 4 #indicates which part of a message is returned by the locally defined poll function.				   
				   
#ZMQ Setup
context = zmq.Context()
socket = context.socket(zmq.PAIR)
host = "tcp://localhost:5656" #change to connect to pi<->hat broker
socket.connect(host) 
time.sleep(1) #sleep for a second to allow sockets to connect.
#note, does this code need to go inside some containing function?

#defines

#######################################################
#pollForMultipartMsg(partToReturn)
#
#Polls the socket for any incoming messages, up to TIMEOUT. If successful
#it returns the part of the message indicated by partToReturn.
#
#inputs: partToReturn is the part of the multipart message to return, typically ARGUMENT
#
#returns: response argument if successful, TIMEOUT_ERROR if not.
def pollForMultipartMsg(partToReturn):
	result = socket.poll(TIMEOUT, zmq.POLLIN) #poll for a message up until TIMEOUT is reached.
	
	if (result == 0): #if no poll events, return error
		return TIMEOUT_ERROR
	
	response = socket.recv_multipart(zmq.NOBLOCK) #should not need to block if polling returned >0

	if (partToReturn == NULL): #by default, return the 4th part of the message.
		partToReturn = ARGUMENT;
	
	return response.pop(partToReturn) #return the Nth part of the multipart message
	

#######################################################
#setMotorDir(motornum, direction)
#
#Sets the direction for the motor indicated by motornum.
#
#inputs: motornum is the motor to set
#        direction is either forward or reverse, 1 or 0 respectively
#
#returns: direction if successful, or TIMEOUT_ERROR
def setMotorDir(motornum, direction):
	socket.send_multipart(["MOT", str(motornum), "DIR", str(direction)]) #send command
	return pollForMultipartMsg(ARGUMENT) #return the 4th part of the multipart message, 
						 #which is the argument (in this case the direction).

#######################################################
#getMotorDir(motornum, direction)
#
#Gets the direction for the motor indicated by motornum.
#
#inputs: motornum is the motor to get the direction for.
#
#returns: 1 for foward, 0 for reverse, or TIMEOUT_ERROR
def getMotorDir(motornum):
	socket.send_multipart(["MOT", str(motornum), "DIR"]) #send only unit, number and verb. no argument.
	return pollForMultipartMsg(ARGUMENT);
	
def setMotorPWM(motornum, duty_cycle):
	socket.send_multipart(["MOT", str(motornum), "SPEED", str(duty_cycle)])
	return pollForMultipartMsg(ARGUMENT);
	
def getMotorPWM(motornum, duty_cycle):
	socket.send_multipart(["MOT", str(motornum), "SPEED"])
	return pollForMultipartMsg(ARGUMENT);
	
	
def ID():
	socket.send_multipart(["ID", "1", "TYPE"]) #should the second "part" be static? 
						   #or is this a special case?
	return pollForMultipartMsg(ARGUMENT);

def version():
	socket.send_multipart(["ID", "1", "VERSION"])
	return pollForMultipartMsg(ARGUMENT);
	
def cameraPWR(power):
	socket.send_multipart(["CAM", "1", "PWR", str(power)])
	return pollForMultipartMsg(ARGUMENT);

#Legacy motorDir function.
#
#######################################################
#motorDir(motornum, direction)
#Sets the direction for the motor indicated.
#inputs: motornum is the motor to set
#        direction is either forward or reverse, 1 or 0 respectively
#returns: none
#def motorDir(motornum, direction):
	#socket.send_multipart(["MOT", str(motornum), "DIR", str(direction)])
	#add functionality to read motor direction?
	#if direction == NULL:
	#	send a request to read motor status instead and return value
	
	#OR, do we need to write two methods, get/setMotorDir() ?
