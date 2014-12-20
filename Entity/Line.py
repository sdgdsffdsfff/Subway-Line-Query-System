#-*- encoding=utf-8 -*-

from Station import Station

class Line(object):
	"""docstring for Line"""
	def __init__(self, line_name):
		super(Line, self).__init__()
		self.line_name = line_name
		self.stations=[]
	def addStation(self, station_name):
		self.stations.append(station_name)
	def intersectWith(self, otherline):
		return True if set(self.stations) & set(otherline.stations) else False
	def inLine(self, station_name):
		return (station_name in self.stations)
	def getExstations(self, otherline):
		return set(self.stations) & set(otherline.stations)
	def getRouteinLine(self, station1,station2,station_dict):
		pos1,pos2 = self.stations.index(station1),self.stations.index(station2)
		route = self.stations[pos1:pos2+1]
		if pos1 > pos2:
			route = list(reversed(self.stations[pos2:pos1+1]))
		size = len(route)
		cost = 0
		retString = ''
		retString += '%s' % (str(route[0]))
		for i in range(size-1):
			st1_name,st2_name = route[i:i+2]
			retString += '=>%s' % (str(st2_name))
			st1 = station_dict[st1_name]
			cost += st1.getNeiborWeight(st2_name)
		retString += '(%s)\n' % self.line_name
		return cost,retString