#!/bin/bash

# John Filipowicz
# Radford University

# Purpose: Capture images from webcam and make them into a video

# Loop control variable, do not change
i=0

location=/media/pi/NESTBOX_DATA
timestamp=$(date +"%m-%d-%Y_%H-%M-%S")
mkdir -p $location/images/$timestamp
mkdir -p $location/images/$timestamp/outside
mkdir -p $location/images/$timestamp/inside
#rm $location/images/*.jpeg

while [ $i -lt 10 ]
do
	# -n for no preview, -t for time before picture, -o to specify output file
	raspistill  -n -o $location/images/$timestamp/inside/image$i.jpeg

	streamer -f jpeg -r 640x480 -o $location/images/$timestamp/outside/image$i.jpeg > Logs/listener.log
	let i=i+1
done


# Uncomment the below lines if you want to do the image processing immediately.

#mogrify -resize 800x800 $location/images/*.jpeg
#convert $location/images/*.jpeg -delete 10 -morph 10 $location/images/%05d.jpeg
#avconv -r 25 -i $location/images/%05d.jpeg -qscale 2 $location/test.mp4
