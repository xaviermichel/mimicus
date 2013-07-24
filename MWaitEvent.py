#-*-coding:utf-8-*-

from MEvent import *
from pymouse import PyMouse

import time

class MWaitEvent(MEvent):

	""" Event specialized for timer """

	def __init__(self, sleeping_time):
		self.sleeping_time = sleeping_time

	def __str__(self):
		return '{ "event": "sleep", "time": "' + str(self.sleeping_time) + '"}'

	def playEvent(self):
		time.sleep(self.sleeping_time)


