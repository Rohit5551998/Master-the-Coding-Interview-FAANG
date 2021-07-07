class QueueWithStacks:
	
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def push(self, val):
		self.s1.append(val)
	
	def pop(self):
		if(len(self.s2) == 0):
			while(len(self.s1) != 0):
				self.s2.append(self.s1.pop())
		return self.s2.pop()

	def peek(self):
		if(len(self.s2) == 0):
			while(len(self.s1) != 0):
				self.s2.append(self.s1.pop())
		return self.s2[len(self.s2) - 1]

	def empty(self):
		return (len(self.s2) == 0 and len(self.s1) == 0)