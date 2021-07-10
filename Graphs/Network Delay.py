times = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]

import heapq, math

#Dijkstra's Implementation
def networkDelay(times, n, k):
	distances = [math.inf for i in range(n)]
	adjList = [[] for i in range(n)]

	#Starting node of Signal and indexes start from 1 hence k-1
	distances[k - 1] = 0
	heapList = []
	heapList.append(k-1)
	heapq.heapify(heapList)

	for i in range(len(times)):
		source = times[i][0]
		target = times[i][1]
		weight = times[i][2]
		adjList[source - 1].append([target - 1, weight])

	while (len(heapList)):
		currVertex = heapq.heappop(heapList)
		adjacent = adjList[currVertex]

		for i in range(len(adjacent)):
			neighbourVertex = adjacent[i][0]
			weight = adjacent[i][1]

			if (distances[currVertex] + weight < distances[neighbourVertex]):
				distances[neighbourVertex] = distances[currVertex] + weight
				heapq.heappush(heapList, neighbourVertex)
	
	answer = max(distances)
	return answer if answer != math.inf else -1


#Bellman-Ford Implementation
def networkDelayDP(times, n, k):
	distances = [math.inf for i in range(n)]
	distances[k] = 0

	for i in range(n-1):
		count = 0
		for j in range(len(times)):
			source = times[j][0]
			target = times[j][1]
			weight = times[j][2]

			if (distances[source] + weight < distances[target]):
				distances[target] = distances[source] + weight
				count += 1
			
		if (count == 0): break

	ans = max(distances)

	return ans if ans != math.inf else -1