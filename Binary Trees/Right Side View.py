# BFS Approach

def rightSideView(root):
	if (not(root)):
		return []

	res = []
	queue = [root]
	currLen = len(queue)
	count = 0

	while (len(queue)):
		
		if(count < currLen):
			node = queue.pop(0)

			if(node.left):
				queue.append(node.left)
			if(node.right):
				queue.append(node.right)

			count += 1
			if(count == currLen):
				temp = node.val
		
		elif(currLen == count):
			res.append(temp)
			currLen = len(queue)
			count = 0

	res.append(temp)

	return res

#DFS Approach

def dfs(node, currLevel, res):
	if not node:
		return res

	if (currLevel >= len(res)):
		res.append(node.val)

	if(node.right):
		dfs(node.right, currLevel+1, res)

	if(node.left):
		dfs(node.left, currLevel+1, res)


def rightSideViewDFS(root):
	res = []
	dfs(root, 0, res)
	return res




