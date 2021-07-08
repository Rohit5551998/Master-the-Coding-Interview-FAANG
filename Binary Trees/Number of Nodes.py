import math

def nodeExists(idxToFind, height, node):
	left = 0
	right = pow(2, height) - 1
	count = 0

	while(count < height):
		midNode = math.ceil((left + right)/2)
		
		if(idxToFind >= midNode):
			node = node.left
			left = midNode

		else:
			node = node.right
			right = midNode - 1

		count += 1

	return (node != None)

def getTreeHeight(root):
	height = 0
	while (root.left != None):
		height += 1
		root = root.left

	return height

def countNodes(root):
	if not root:
		return 0

	height = getTreeHeight(root)

	if (height == 0):
		return 1

	upperCount = pow(2, height) - 1

	left = 0
	right = upperCount

	while(left < right):
		idxToFind = math.ceil((left + right) / 2)
		if(nodeExists(idxToFind, height, root)):
			left = idxToFind
		else:
			right = idxToFind - 1

	return (upperCount+left+1)