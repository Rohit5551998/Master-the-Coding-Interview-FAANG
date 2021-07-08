adjacencyList = [
  [1, 3],
  [0],
  [3, 8],
  [0, 2, 4, 5],
  [3, 6],
  [3],
  [4, 7],
  [6],
  [2]
]

def traversalBFS(graph):
	seen = {}
	queue = [0]
	values = []

	while (len(queue)):
		currNode = queue.pop(0)

		values.append(currNode)		
		seen[currNode] = True

		connections = graph[currNode]

		for i in range(0, len(connections)):
			connection = connections[i]
			if (not(connection in seen)):
				queue.append(connection)

	return values
	
print(traversalBFS(adjacencyList))