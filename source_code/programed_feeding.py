#!/usr/bin/python

# philson
# radford university

# purpose: to ensure food is avaiable to attract animals by dispencing food on a timer
import time
from subprocess import call

# time in secconds to dispenc food without a trigger
interval = 14400

while True:
  time.sleep(interval);
  call(["./servo2.py", "&"])
  
