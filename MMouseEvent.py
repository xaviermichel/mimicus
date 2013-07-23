#-*-coding:utf-8-*-

from MEvent import *
from pymouse import PyMouse

class MMouseEvent(MEvent):

	""" Event specialized for mouse """
	def __init__(self, x, y, button):
		self.x = x
		self.y = y
		self.button = button

	def __str__(self):
		return '{ "event": "click", "type": "press", "x": "' + str(self.x) + '", "y": "' + str(self.y) + '", "button": "' + str(self.button) + '"}'

	def playEvent(self):
		 PyMouse().click(self.x, self.y, self.button)


