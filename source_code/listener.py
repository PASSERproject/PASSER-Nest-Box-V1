#!/usr/bin/python

# John Filipowicz
# Radford University

# The purpose of this file is to 'listen' for either a sizable pressure reading
#    or for a proximity sensor hit that is close enough. Once one is found, the
#    appropriate code is executed and the program shall loop.

import time
import RPi.GPIO as GPIO
import sys
import collect_data
from subprocess import call

sys.path.insert(0, '~/sensor_libraries/Proximity')
import Adafruit_VCNL40xx


# Pin to read. Verify correctness
pin = 21

# Threshold for Proximity sensor
threshold = 2600

# Time to sleep between hits in seconds
sleep_hit = 11

# Time to sleep between misses in seconds
sleep_miss = .25


# BCM means we are using GPIO numbering instead of pin numbering.
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

# Creating Proximity sensor instance
vcnl = Adafruit_VCNL40xx.VCNL4010()


while True:
	#print('Pressure={0}  ,  Proximity={1}'.format(GPIO.input(pin), vcnl.read_proximity()))
	if ((vcnl.read_proximity() > threshold) or GPIO.input(pin)):
		#print('Triggered by sensor')
		#collect_data.capture();
		#call(["./servo2.py", "&"])
		call("./images.sh")
                collect_data.collect();
		#time.sleep(sleep_hit);
	else:
		#print('below threshold')
		time.sleep(sleep_miss);

