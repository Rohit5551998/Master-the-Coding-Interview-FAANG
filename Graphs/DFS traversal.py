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

def traversalDFS(vertex, graph, values, seen):
	values.append(vertex)
	seen[vertex] = True

	connections = graph[vertex]
	for i in range(0, len(connections)):
		connection = connections[i]

		if (not(connection in seen)):
			traversalDFS(connection, graph, values, seen)
	
values = []
traversalDFS(0, adjacencyList, values, {})
print(values)