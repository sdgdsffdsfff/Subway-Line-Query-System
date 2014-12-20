#-*- encoding=utf-8 -*-

class Selection(object):
	"""docstring for Selection"""
	def __init__(self, station_name,height,timecost=0,parent=None):
		super(Selection, self).__init__()
		self.station_name=station_name
		self.timecost=timecost
		self.height=height
		self.parent=parent
	def inPath(self, station_name):
		ok=0
		curnode=self
		while not ok and curnode:
			if curnode.station_name == station_name:
				ok = 1
			curnode = curnode.parent
		return ok
	def displayPath(self):
		curnode=self
		path = []
		while curnode:
			path.append(curnode.station_name)
			curnode = curnode.parent
		path.reverse()
		return path