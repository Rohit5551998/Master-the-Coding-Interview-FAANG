def naiveDetection(head):
	currNode = head
	cycleSet = set()

	while(not(currNode in cycleSet)):
		if (currNode.next == None):
			return False
		
		cycleSet.add(currNode)
		currNode = currNode.next

	return currNode	

def cycleDetection(head):
	if(not(head)):
		return None

	slow, fast = head, head

	while(True):
		slow, fast = slow.next, fast.next

		if(fast == None or fast.next == None):
			return None
		else:
			fast = fast.next

		if(slow == fast):
			break

	p1, p2 = head, slow

	while(p1 != p2):
		p1, p2 = p1.next, p2.next

	return p2