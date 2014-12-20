#-*- encoding=utf-8 -*-

from Entity.Station import Station
from Entity.Line import Line
from Entity.Selection import Selection
from Tool.Getdata import loadData

import Func.Bfs as BFS
import Func.Dijk as DIJKSTRA
import Func.Mintransfer as TRANSFER

def create_subway_map(lines_data,weights):
	station_dict={}
	line_dict={}
	for line_name in lines_data:
		line = lines_data[line_name]
		subline = Line(line_name)
		for station_name in line:
			subline.addStation(station_name)
			if station_name not in station_dict:			
				station_dict[station_name]=Station(station_name)
		line_dict[line_name] = subline
	for line_name in lines_data:
		line = lines_data[line_name]
		line_length=len(line)
		for i in range(line_length-1):
			mainstation,neiborstation=line[i:i+2]
			station_dict[mainstation].addNeibor(neiborstation,timecost=weights[neiborstation])#weights[neiborstation])
		for i in range(line_length-1,0,-1):
			mainstation,neiborstation=line[i],line[i-1]
			station_dict[mainstation].addNeibor(neiborstation,timecost=weights[neiborstation])#weights[neiborstation])
	return station_dict,line_dict


if __name__ == '__main__':
	lines_data,weights = loadData()

	station_dict,line_dict=create_subway_map(lines_data,weights)
	
	while True:
		start = raw_input('出发点>>')
		end = raw_input('目的地>>')
		print '******最少换乘******'
		intersectionMatrix=TRANSFER.create_Intersection_Matrix(line_dict)
		TRANSFER.leastexchange(intersectionMatrix,line_dict,station_dict,start,end)
		print '******最少用时******'
		DIJKSTRA.dijkstra(station_dict,start,end)
		print '******最少停站******'
		BFS.breadfs(station_dict ,start ,end)