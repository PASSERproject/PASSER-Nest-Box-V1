#!/bin/bash

# John Filipowicz
# Radford University

# Purpose: Prep for and launch all necessary processes.

CSV=/media/pi/NESTBOX_DATA/DHT_data.csv

if [ ! -f "$CSV" ] ; then
	echo "Temperature,Humidity,TimeStamp" >> "$CSV"
fi

# Remove '#' and the space before it to redirect stderr & stdout to logs
./periodic.py & #>./Logs/periodic.log
./listener.py & #>./Logs/listener.log
./programed_feeding.py & 
#Dr. Ray's Program too

