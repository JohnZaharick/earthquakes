#enter in Anaconda:
#python -m pip install -U pip setuptools
#pip install feedparser

import feedparser
import time
from toneGenerator import playTone
quakeID = " "

try:
	while True:
		d = feedparser.parse('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.atom')
		print d['feed']['title']
		for idx, item in enumerate(d['entries']):
			mystring = str(d['entries'][idx]['title'])
			if mystring != quakeID: #check that the particular earthquake hasn't been played already.  The atom feed contains all quakes from the past hour.
				print mystring
				playTone(float(mystring.split(" ")[1]) * 100)
			else:
				break
		quakeID = str(d['entries'][0]['title']) #the title of the first earthquake played this round is stored
		print "Ctrl-C to stop program"
		print " "
		time.sleep(300) #the USGS atom feed updates once every 5 minutes, so the script loops every five minutes
except KeyboardInterrupt:
	print "stop"