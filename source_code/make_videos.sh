#!/bin/bash

# John Filipowicz
# Radford University

# Purpose: Create videos for each set of images previously taken.

location=/media/pi/FEEDER_DATA
cd $location/images

for d in */; do
  mogrify -resize 800x800 $location/images/$d*.jpeg
  convert $location/images/$d*.jpeg -delete 10 -morph 10 $location/images/$d%05d.jpeg
  avconv -r 25 -i $location/images/$d%05d.jpeg -qscale 2 $location/images/$dvideo.mp4
done

cd ~/Feeder/source_code
