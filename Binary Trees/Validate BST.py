import math

def isValidBST(root):
	if not root:
		return False

	left = -math.inf
	right = math.inf

	return checkBST(root, left, right)

def checkBST(node, left, right):

	if (node.val <= left or node.val >= right ):
		return False
	
	if node.left:
		if not checkBST(node.left, left, node.val):
			return False

	if node.right:
		if not checkBST(node.right, node.val, right):
			return False

	return True