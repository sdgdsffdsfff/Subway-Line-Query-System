#-*- encoding=utf-8 -*-

class Station(object):
	"""docstring for Station"""
	def __init__(self, station_name):
		super(Station, self).__init__()
		self.station_name = station_name
		self.neibor_stations={}
		self.change=False
	def addNeibor(self, station_name, timecost):
		self.neibor_stations[station_name]=timecost
	def getNeibors(self):
		return self.neibor_stations.keys()
	def getNeiborWeight(self, neibor):
		return self.neibor_stations[neibor]
	def imchange(self):
		self.change=True