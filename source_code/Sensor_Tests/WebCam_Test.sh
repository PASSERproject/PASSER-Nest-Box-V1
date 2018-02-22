#!/bin/bash

# John Filipowicz
# Radford University

# Purpose: Take a 10 sec test video from the WebCam (Video Only)


streamer -q -r 60 -t 0:0:10 -f rgb24 -o /media/pi/FEEDER_DATA/test.avi &>/dev/null
