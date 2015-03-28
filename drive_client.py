'''
drive_client.py

A development space for the CoroBot Spark API

Calls the spark API.

By Keenan Fejeran
1/31/2015
'''
#imports, currently from a local module

#the following import should work, but isn't in my environment.
#import SparkControl

from SparkControl import *

#example API calls 
#motorDir(1234, "FORWARD") #set all motors direction to forward
i = 0
while i<5:
	i = i + 1
	print setMotorDir(1, "FORWARD")

#motorPWM(1, 50) #set motor 1 speed to 50%

#API calls that get a response
#print "Robot Type: " + ID()
#print "Firmware Version: " + version()

#alternative ways we could set up the api calls, using the dot call.
#print spark.ID()
#print spark.version()
