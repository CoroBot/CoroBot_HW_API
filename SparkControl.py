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
def motorDir(motornum, direction):
	socket.send("MOT||"+str(motornum)+"||SPEED||"+str(direction))

def motorPWM(motornum, duty_cycle):
	socket.send("MOT||"+str(motornum)+"||DIR||"+ str(duty_cycle))
