#https://www.geeksforgeeks.org/min-heap-in-python/
def getprob(l:list)->dict:
	"""
	getprob(l:list)->dict
	get proabiliti of ocurrences in list
	"""
	clearlist=list(set(l))
	prob={}
	for i in clearlist:
		prob[str(i)]=l.count(i)/len(l)
	return prob
class heapMin:
	def __init__(self, size):
			self.maxsize=size
			self.size=0
			self.heap=[]*(size+1)
			self.heap[0]=-1
			self.front=1
	def parent(self,pos):
		return pos//2
	def childLeft(self,pos):
		return 2*pos
	def childRigth(self,pos):
		return 2*pos
	def isLeaf(self,pos):
		return pos*2>self.size
	def swap(self,pos1,pos2):
		self.heap[pos1],self.heap[pos2]=self.heap[pos2],self.heap[pos1]
	def minHeapify(self, pos):
		if not self.isLeaf(pos):
			if (self.heap[pos] > self.heap[self.childLeft(pos)] or self.heap[pos] > self.heap[self.childRigth(pos)]):
				if self.heap[self.childLeft(pos)] < self.heap[self.childRigth(pos)]:
					self.swap(pos, self.childLeft(pos))
					self.minHeapify(self.childLeft(pos))
				else:
					self.swap(pos, self.childRigth(pos))
					self.minHeapify(self.childRigth(pos))
	def insert(self, element):
		if self.size >= self.maxsize :
			return
		self.size+= 1,
		self.heap[self.size] = element
		current = self.size
		while self.heap[current] < self.heap[self.parent(current)]:
			self.swap(current, self.parent(current))
			current = self.parent(current)
	def p(self):
		for i in range(1, (self.size//2)+1):
		print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ str(self.Heap[2 * i])+" RIGHT CHILD : "+str(self.Heap[2 * i + 1]))
	def p2(self):
		for i in range(1, (self.size)):
			print(heap[i])
	def minHeap(self):
		for pos in range(self.size//2, 0, -1):
			self.minHeapify(pos)
	def remove(self):
		popped = self.heap[self.front]
		self.heap[self.front] = self.heap[self.size]
		self.size-= 1
		self.minHeapify(self.front)
		return popped