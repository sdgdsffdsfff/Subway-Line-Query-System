#-*- encoding=utf-8 -*-

from Entity.Station import Station
from Entity.Line import Line
from Entity.Selection import Selection
from Global.Var import MAX

def breadfs(station_dict,start,end):
	queue=[]
	cur = Selection(start,0)
	minheight = MAX

	available_paths=[]
	
	queue.append(cur)

	while queue:
		cur = queue.pop(0)
		if cur.height > minheight:
			break
		if cur.station_name == end and cur.height <= minheight:
			minheight = cur.height
			available_paths.append(cur)
			continue
		for neibor in station_dict[cur.station_name].getNeibors():
			if not cur.inPath(neibor):
				next = Selection(neibor,cur.height+1,parent=cur)
				queue.append(next)
	for path in available_paths:
		way = path.displayPath()
		size = len(way)
		print way[0],
		cost = 0
		for i in range(size-1):
			st_name1,st_name2 = way[i:i+2]
			print '=>%s' % (st_name2),
			st1,st2 = station_dict[st_name1],station_dict[st_name2]
			cost += st1.getNeiborWeight(st_name2)
		print '(用时大约 %d 分钟)' % cost