#!/usr/bin/env python

from threading import Thread
from ytmusicapi import YTMusic

ytmusic=YTMusic()

class MusicUpdater(Thread):
	def __init__(self,content,queue):
		Thread.__init__(self)
		self.content=content
		self.queue=queue
	
	def run(self):
		try:
			song = ytmusic.search(self.content, 'songs')[0]
			videoId=song['videoId']
			duration=song['duration']
			self.queue.add(videoId,duration)
		except:
			pass