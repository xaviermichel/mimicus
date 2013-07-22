#-*-encoding:utf-8-*-

from MMouseEvent import *
from pymouse import PyMouseEvent

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

		# Should I stop ?
		if not self.stop_trigger is None and self.stop_trigger(button):
			self.stop()

	def set_stop_trigger(self, f):
		self.stop_trigger = f

