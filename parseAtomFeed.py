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
			if mystring != quakeID:
				print mystring
				playTone(float(mystring.split(" ")[1]) * 100)
			else:
				break
		quakeID = str(d['entries'][0]['title'])
		print "Ctrl-C to stop program"
		print " "
		time.sleep(300)
except KeyboardInterrupt:
	print "stop"