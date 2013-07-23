#-*-coding:utf-8-*-

from MEventRecorder import *
from MEventPlayer import *

def main() :
	print 'Recorder is running !'
	recorder = MEventRecorder()
	recorder.stop_trigger = lambda x : isinstance(x, MMouseEvent) and x.button == 3
	recorder.run()
	print 'Record is over'
	print 'It''s time to play'
	player = MEventPlayer(recorder.events)
	player.run()
	print 'The game is over !'

if __name__ == '__main__' :
	main()
