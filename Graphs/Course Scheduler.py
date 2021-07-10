from collections import deque

def naiveScheduler(numCourses, prerequisites):
	adjList = [[] for i in range(numCourses)]

	for i in range(len(prerequisites)):
		pair = prerequisites[i]
		adjList[pair[1]].append(pair[0])

	for v in range(len(numCourses)):
		queue = []
		seen = {}

		for i in range(0, len(adjList[v])):
			queue.append(adjList[v][i])	

		while(len(queue)):
			current = queue.pop(0)
			seen[current] = True

			if (current == v):
				return False
			adjacent = adjList[current]
			for i in range(0, len(adjacent)):
				next = adjacent[i]
				
				if(not(next in seen)):
					queue.append(next)

	return True

#Topological Sort Implementation
def canFinish(numCourses, prerequisites):
	adjList = [[] for i in range(numCourses)]
	inDegree = [0 for i in range(numCourses)]

	for i in range(len(prerequisites)):
		pair = prerequisites[i]
		inDegree[pair[0]] += 1
		adjList[pair[1]].append(pair[0])

	stack = deque()

	for i in range(len(inDegree)):
		if (inDegree[i] == 0):
			stack.append(i)

	count = 0

	while (len(stack)):
		current = stack.pop()
		count += 1

		adjacent = adjList[current]

		for i in range(len(adjacent)):
			next = adjacent[i]
			inDegree[next] -= 1
			
			if (inDegree[next] == 0):
				stack.append(next)

	return (count == numCourses)
