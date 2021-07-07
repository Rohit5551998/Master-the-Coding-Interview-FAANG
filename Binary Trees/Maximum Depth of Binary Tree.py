def recursiveTree(node, count):
	if(node == None):
		return count
	
	count += 1
	lc = recursiveTree(node.left, count)
	rc = recursiveTree(node.right, count)

	return max(lc, rc)


def maxDepth(root):
	
	if (root == None):
		return 0

	if(root.left == None and root.right == None):
		return 1

	return recursiveTree(root, 0)

