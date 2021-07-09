def numOfMin(n, headID, manager, informTime):
	adjList = [[] for i in range(len(manager))]
	
	for i in range(len(manager)):
		currManager = manager[i]

		if (currManager == -1): continue

		adjList[currManager].append(i)

	return dfs(headID, adjList, informTime)

def dfs(currID, adjList, informTime):

	if (len(adjList[currID]) == 0): return 0

	maxVal = 0
	subordinates = adjList[currID]

	for i in range(0, len(subordinates)):
		maxVal = max(maxVal, dfs(subordinates[i], adjList, informTime))

	return maxVal + informTime[currID]


