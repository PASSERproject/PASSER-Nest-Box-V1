#!/usr/bin/python

# John Filipowicz
# Radford University

# Purpose: collect dht11 data every x amount of seconds

import time
import collect_data

# Time in seconds to sleep untill next collection
interval = 1800

while True:
	collect_data.collect()
	time.sleep(interval);


