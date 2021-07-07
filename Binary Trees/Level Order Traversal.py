def levelOrder(root):

	if root is None:
		return []

	res = []
	queue = [root]
	reqCount = 1
	count = 0
	temp = []

	while(len(queue)):
		
		if(reqCount == count):
			res.append(temp)
			reqCount = len(queue)
			temp = []
			count = 0

		elif(count < reqCount):
			node = queue.pop(0)
			temp.append(node.val)

			if(node.left):
				queue.append(node.left)

			if(node.right):
				queue.append(node.right)

			count += 1

	res.append(temp)
	return res
