#-*-coding:utf-8-*-

import abc

class MEvent:
	""" Generic user event """
	
	@abc.abstractmethod
	def playEvent(self) :
		""" replay the event """
		raise NotImplementedError('Not implemented yet !')
		return

