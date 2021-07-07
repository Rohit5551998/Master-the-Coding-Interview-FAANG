def flatten(head):
	if (head is None):
		return head	
	
	currNode = head

	while(currNode is not None):

		if(currNode.child is None):
			currNode = currNode.next

		else:
			tail = currNode.child
			while(tail.next is not None):
				tail = tail.next

			tail.next = currNode.next
			if(tail.next is not None):
				tail.next.prev = tail
			currNode.next = currNode.child
			currNode.next.prev = currNode
			currNode.child = None

	return head
