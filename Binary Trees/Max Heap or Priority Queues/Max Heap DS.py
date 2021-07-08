import math

def comparator(a, b):
	return a > b

class PriorityQueue:
	def __init__(self, comparator):
		self.__heap = []
		self.__comparator = comparator

	def size(self):
		return len(self.__heap)

	def isEmpty(self):
		return (self.size() == 0)

	def peek(self):
		return (self.__heap[0])

	def __parent(self, idx):
		return math.floor((idx - 1) / 2)

	def __leftChild(self, idx):
		return (idx * 1 + 1)

	def __rightChild(self, idx):
		return (idx * 1 + 2)

	def __swap(self, i, j):
		[self.__heap[i], self.__heap[j]] = [self.__heap[j], self.__heap[i]]

	def __compare(self, i, j):
		return self.__comparator(self.__heap[i], self.__heap[j])

	def push(self, value):
		self.__heap.append(value)
		self.__siftUp()

		return self.size()

	def __siftUp(self):
		nodeIdx = self.size() - 1

		while (0 < nodeIdx and self.__compare(nodeIdx, self.__parent(nodeIdx))):
			self.__swap(nodeIdx, self.__parent(nodeIdx))
			nodeIdx = self.__parent(nodeIdx)

	def pop(self):
		if (self.size() > 1):
			self.__swap(0, self.size() - 1)

		poppedValue = self.__heap.pop()
		self.__siftDown()
		return poppedValue

	def __siftDown(self):
		nodeIdx = 0

		while ((self.__leftChild(nodeIdx) < self.size() and self.__compare(self.__leftChild(nodeIdx), nodeIdx)) or (self.__rightChild(nodeIdx) < self.size() and self.__compare(self.__rightChild(nodeIdx), nodeIdx))):
    	
			greaterChildIdx = self.__rightChild(nodeIdx) if (self.__rightChild(nodeIdx) < self.size() and self.__compare(self.__rightChild(nodeIdx), self.__leftChild(nodeIdx))) else self.__leftChild(nodeIdx)


			self.__swap(greaterChildIdx, nodeIdx);
			nodeIdx = greaterChildIdx;
    
pq = PriorityQueue(comparator)
pq.push(15)
pq.push(12)
pq.push(50)
pq.push(7)
pq.push(40)
pq.push(22)

while (not pq.isEmpty()):
	print(pq.pop())
	
	import math

def comparator(a, b):
	return a > b

class PriorityQueue:
	def __init__(self, comparator):
		self.__heap = []
		self.__comparator = comparator

	def size(self):
		return len(self.__heap)

	def isEmpty(self):
		return (self.size() == 0)

	def peek(self):
		return (self.__heap[0])

	def __parent(self, idx):
		return math.floor((idx - 1) / 2)

	def __leftChild(self, idx):
		return (idx * 1 + 1)

	def __rightChild(self, idx):
		return (idx * 1 + 2)

	def __swap(self, i, j):
		[self.__heap[i], self.__heap[j]] = [self.__heap[j], self.__heap[i]]

	def __compare(self, i, j):
		return self.__comparator(self.__heap[i], self.__heap[j])

	def push(self, value):
		self.__heap.append(value)
		self.__siftUp()

		return self.size()

	def __siftUp(self):
		nodeIdx = self.size() - 1

		while (0 < nodeIdx and self.__compare(nodeIdx, self.__parent(nodeIdx))):
			self.__swap(nodeIdx, self.__parent(nodeIdx))
			nodeIdx = self.__parent(nodeIdx)

	def pop(self):
		if (self.size() > 1):
			self.__swap(0, self.size() - 1)

		poppedValue = self.__heap.pop()
		self.__siftDown
		return poppedValue

	def __siftDown(self):
		nodeIdx = 0

		while ((self._leftChild(nodeIdx) < self.size() and self._compare(self._leftChild(nodeIdx), nodeIdx)) or (self._rightChild(nodeIdx) < self.size() and self._compare(self._rightChild(nodeIdx), nodeIdx))):

    	greaterChildIdx = self.__rightChild(nodeIdx) if (self._rightChild(nodeIdx) < self.size() and self._compare(self._rightChild(nodeIdx), self._leftChild(nodeIdx)))
      else self._leftChild(nodeIdx)

      self._swap(greaterChildIdx, nodeIdx);
      nodeIdx = greaterChildIdx;
    
pq = PriorityQueue()
pq.push(15)
pq.push(12)
pq.push(50)
pq.push(7)
pq.push(40)
pq.push(22)

while (!pq.isEmpty()):
	print(pq.pop())
	
	