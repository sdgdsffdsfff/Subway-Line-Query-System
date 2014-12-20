#-*- encoding=utf-8 -*-

def loadData():
	files=['1.txt','13.txt','2.txt','5.txt','8t.txt','cp.txt','fs.txt','yz.txt','10.txt','15.txt','4.txt','8.txt','9.txt','dx.txt','jc.txt']
	lines_data={}
	weights={}	
	for filename in files:
		with open('data/%s' % filename,'r') as file:
			line_name=file.readline()[:-1]
			lines_data[line_name]=[]
			for line in file:
				line = line.strip()
				lineAttr = line.split('\t')
				station_name, station_time = lineAttr[0],int(lineAttr[1])
				if station_name not in weights:
					weights[station_name] = station_time
				lines_data[line_name].append(station_name)
	return lines_data,weights