#enter in Anaconda:
#python -m pip install -U pip setuptools
#pip install feedparser

import feedparser
import time
from toneGenerator import playTone
firstQuakeID = " "

try:
	while True:
		d = feedparser.parse('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.atom')
		print d['feed']['title']
		for idx, item in enumerate(d['entries']):
			currentQuakeID = str(d['entries'][idx]['id']).split(":")[3] #id number of the current earthquake being processed
			magnitude = float(str(d['entries'][idx]['title']).split(" ")[1]) #position 1 in the title is always the magnitude. eg: M 0.8 - 17km ESE of Anza, California
			if currentQuakeID != firstQuakeID: #check that the particular earthquake hasn't been played already.  The atom feed contains all quakes from the past hour.
				print str(d['entries'][idx]['title'])
				playTone(magnitude * 100)
			else:
				break
		firstQuakeID = str(d['entries'][0]['id']).split(":")[3] #the id number of the first earthquake played this round is stored
		print "Ctrl-C to stop program"
		print " "
		time.sleep(300) #the USGS atom feed updates once every 5 minutes, so the script loops every five minutes
except KeyboardInterrupt:
	print "stop"