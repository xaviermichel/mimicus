#-*-coding:utf-8-*-

from MMouseEvent import *
from pymouse import PyMouse
import time
import mimicus as config

class MEventPlayer:
	""" Event player """

	def __init__(self, events) :
		self.events = events
		self.pymouse = PyMouse()

	def run(self):
		for i in range(config.REPEAT_COUNT):
			for event in self.events :
				print event
				if isinstance(event, MMouseEvent) :
					self.pymouse.click(event.x, event.y, event.button)
					time.sleep(config.TIME_BETWEEN_ACTION)

