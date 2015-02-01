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
socket.connect("tcp://localhost:5656")

#defines for controlling spark

#######################################################
#motorDir(motornum, direction)
#Sets the direction for the motor indicated.
#inputs: motornum is the motor to set
#        direction is either forward or reverse, 1 or 0 respectively
#returns: none
def motorDir(motornum, direction):
	socket.send("MOT||"+str(motornum)+"||DIR||"+str(direction))

def motorPWM(motornum, duty_cycle):
	socket.send("MOT||"+str(motornum)+"||SPEED||"+ str(duty_cycle))

def ID():
	socket.send("ID||1||TYPE")
	msg = socket.recv()
	return msg

def version():
	socket.send("ID||1||VERSION")
	return socket.recv()
