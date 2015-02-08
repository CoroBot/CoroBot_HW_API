#simple_serial.py

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 0) #change to tiva board?

i = 0

while i<10:
	#ser.write(bytes("Hello", 'UTF-8'))
	ser.write("Hello")
	#msg = ser.readline() #?
	time.sleep(1)
	i = i+1
	
ser.close()
