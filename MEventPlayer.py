#-*-coding:utf-8-*-

from MMouseEvent import *

import config

class MEventPlayer:
	""" Event player """

	def __init__(self, events) :
		self.events = events
		self.pymouse = PyMouse()

	def run(self):
		for i in range(config.REPEAT_COUNT):
			for event in self.events :
				print event
				event.playEvent()

