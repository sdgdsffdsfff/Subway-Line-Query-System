#-*- encoding=utf-8 -*-

class Member(object):
	"""docstring for Member"""
	def __init__(self, station_name, cost):
		super(Member, self).__init__()
		self.station_name = station_name
		self.cost = cost
		self.parent = None
	def displayPath(self,mincost):
		curnode=self
		path = []
		while curnode:
			path.append(curnode.station_name)
			curnode = curnode.parent
		path.reverse()
		for out in path:
			print '=>%s' % str(out),
		print '(用时%d分钟)' % mincost
		return path

class MinHeap(object):
	"""docstring for Heap"""
	def __init__(self, heapsize):
		super(MinHeap, self).__init__()
		self.heapsize = heapsize
		self.heap=[]
	def setData(self,members):
		for member in members:
			self.heap.append(member)

def holdHeap(minheap,pos):
	left,right,minpos=2*pos+1,2*pos+2,pos
	minvalue = minheap.heap[pos].cost

	if right < minheap.heapsize and  minheap.heap[right].cost < minheap.heap[minpos].cost:
		minpos = right
	if left < minheap.heapsize and minheap.heap[left].cost < minheap.heap[minpos].cost:
		minpos = left
	if minpos != pos:
		minheap.heap[pos],minheap.heap[minpos]=minheap.heap[minpos],minheap.heap[pos]
		holdHeap(minheap,minpos)

def initHeap(minheap):
	haslastleaf = minheap.heapsize/2-1
	for i in range(haslastleaf,-1,-1):
		holdHeap(minheap,i)
def emptyHeap(minheap):
	return True if not minheap.heapsize else False

def topHeap(minheap):
	minMem = minheap.heap[0]
	minheap.heap[0] = minheap.heap[minheap.heapsize-1]
	minheap.heapsize-=1
	holdHeap(minheap,0)
	return minMem

def decHeap(minheap,station_name,newcost,parent):
	targetPos = -1
	for i,mem in enumerate(minheap.heap[:minheap.heapsize]):
		if targetPos != -1:
			break
		if mem.station_name == station_name:
			targetPos = i
	if targetPos <=0 or minheap.heap[targetPos].cost <= newcost:
		return 
	minheap.heap[targetPos].cost = newcost
	minheap.heap[targetPos].parent = parent

	parentPos = (targetPos-1)/2

	while parentPos >= 0:
		if minheap.heap[targetPos].cost >= minheap.heap[parentPos].cost:
			break
		minheap.heap[targetPos],minheap.heap[parentPos]=\
		minheap.heap[parentPos],minheap.heap[targetPos]
		targetPos = parentPos
		parentPos = (targetPos-1)/2