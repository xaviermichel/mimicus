#-*-encoding:utf-8-*-

from MMouseEvent import *
from MWaitEvent import *

from pymouse import PyMouseEvent

import config

class MEventRecorder(PyMouseEvent):

	""" Event recorder """

	def __init__(self):
		PyMouseEvent.__init__(self)
		self.events = []
		self.stop_trigger = None

	def click(self, x, y, button, press):
		if press:
			event = MMouseEvent(x, y, button)
			print event
			self.events.append(event)
			self.stop_test()

	def stop_test(self):
		# Should I stop ?
		if not self.stop_trigger is None and self.stop_trigger(self.events[-1]):
			# do not keep stop event
			del self.events[-1]
			self.stop()
		else:
			# add sleep (after break, very important)
			self.events.append(MWaitEvent(config.TIME_BETWEEN_ACTION))

