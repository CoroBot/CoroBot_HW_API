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
	#socket.send("MOT||"+str(motornum)+"||DIR||"+str(direction))
	sendMultipart(["MOT", str(motornum), "DIR", str(direction)])
	# socket.send("MOT", zmq.SNDMORE)
	# socket.send(str(motornum), zmq.SNDMORE)
	# socket.send("DIR", zmq.SNDMORE)
	# socket.send(str(direction))

def motorPWM(motornum, duty_cycle):
	#socket.send("MOT||"+str(motornum)+"||SPEED||"+ str(duty_cycle))
	socket.send("MOT", zmq.SNDMORE)
	socket.send(str(motornum), zmq.SNDMORE)
	socket.send("SPEED", zmq.SNDMORE)
	socket.send(str(duty_cycle))

def ID():
	socket.send("ID", zmq.SNDMORE)
	socket.send("1", zmq.SNDMORE)
	socket.send("TYPE")
	msg = socket.recv() #if server responds with more than one msg, this needs work
	return msg

def version():
	#socket.send("ID||1||VERSION")
	socket.send("ID", zmq.SNDMORE)
	socket.send("1", zmq.SNDMORE)
	socket.send("VERSION")
	return socket.recv()
	
def cameraPWR(power):
	socket.send("CAM", zmq.SNDMORE)
	socket.send("1", zmq.SNDMORE)
	socket.send("PWR", zmq.SNDMORE)
	socket.send(str(power))
	
#######################################################
#sendMultipart(parts)
#Sends an array of objects using ZMQ multipart messages.
#inputs: parts is an array of objects to send
#
#returns: none	
def sendMultipart(parts):
	#send pieces, with SNDMORE flag
	for i in range(len(parts) - 1):
		socket.send(parts[i], zmq.SNDMORE) #or str value of
	
	#send last part, without SNDMORE flag
	socket.send(parts[len(parts) - 1])
	
