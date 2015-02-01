'''
drive_client.py

A development space for the CoroBot Spark API

Calls the spark API.

By Keenan Fejeran
1/31/2015
'''
#imports, currently from a local package
#from SparkPython.spark import *
from SparkControl import *

#example API calls
#spark.ID()
#spark.version()

#spark.motorPWM(1, 50)
#spark.motorDir(1, 1)
#drive = spark.drive()

#drive(3)
#SparkControl.motorDir(SparkControl.FORWARD)
motorDir(1, "FOWARD")
motorPWM(1234, 50)
