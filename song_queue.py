#!/usr/bin/env python

from threading import Thread
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

class Queue(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.queue={}
		self.open=True
		options=Options()
		options.add_extension("/path/to/adblock.crx")
		options.binary_location="/path/to/chrome.exe"
		self.chrome=Chrome(chrome_options=options, executable_path="/path/to/chromedriver.exe")
	
	def run(self):
		try:
			while True:
				if len(self.queue)>0:
					videoId=next(iter(self.queue))
					duration=self.queue.pop(videoId)
					self.chrome.get("https://music.youtube.com/watch/?v="+videoId)
					min,sec=duration.split(":")
					sleep(int(min)*60+int(sec))
				else:
					sleep(0.1)
		except:
			pass
		self.chrome.close()
	
	def add(self, id, duration):
		self.queue[id]=duration