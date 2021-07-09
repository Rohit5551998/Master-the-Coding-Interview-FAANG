class Person:
	def __init__(self, name):
		self.name = name
		self.isAlive = True
		self.children = []

class Monarchy:
	def __init__(self, kingName):
		self.king = Person(kingName)
		self.__persons = { self.king.name: self.king}

	def birth(self, childName, parentName):
		parent = self.__persons[parentName]	
		newChild = Person(childName)
		parent.children.append(newChild)
		self.__persons[childName] = newChild

	def death(self, name):
		if (name in self.__persons):
			person = self.__persons[name]
			person.isAlive = False

	def getOrderofSuccession(self):
		order = []
		self.__dfs(self.king, order)
		return order

	def __dfs(self, currPerson, order):
		if (currPerson.isAlive):
			order.append(currPerson.name)

		for i in range(0, len(currPerson.children)):
			self.__dfs(currPerson.children[i], order)

