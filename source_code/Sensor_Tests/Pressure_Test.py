#!/usr/bin/python

# John Filipowicz
# Radford University

# Purpose: Test the pressure sensor by outputting the analogue signal recieved
# 0 means below threshold (3.3V to the pin)
# 1 means at or above threshold

import time
import RPi.GPIO as GPIO


# GPIO pin connected to pressure sensor. Must be correct for test to be accurate.
pin = 21

# BCM means GPIO numbering instead of pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

print("Press CTRL-C to quit")
time.sleep(1)
print("Zero means below threshold, one means at or above threshold.")
time.sleep(3)
print("The threshold cannot be changed via software, the curcuit would have to be altered")
time.sleep(3)

while True:
	print(GPIO.input(pin))
	time.sleep(1)
