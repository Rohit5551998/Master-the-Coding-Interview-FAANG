#Left = m and Right = n
def reverseBetween(head, left, right):
	currPos = 1
	currNode = head
	start = head

	while(currPos < left):
		start = currNode
		currNode = currNode.next
		currPos += 1
	
	newList = None
	# Save this for attaching this node to remaining unreversed list
	tail = currNode

	while(currPos >= left and currPos <= right):
		# Grab Next Node
		nextNode = currNode.next
		# Set currnode to point to new empty list
		currNode.next = newList
		# Change the head of new empty list
		newList = currNode
		# Set the current Node to the previously stored next node
		currNode = nextNode
		#Simply update currPos
		currPos += 1

	#Set the next of original list before m to new list
	start.next = newList
	# Attach the first node's next before reversing to the node after N
	tail.next = currNode

	if(left > 1):
		return head
	#If m=0 return the head as first node of new list
	else:
		return newList