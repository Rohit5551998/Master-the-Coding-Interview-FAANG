def revList(self, head):
	if (head is None or head.next is None):
		return head
	curr = self.head
	while (curr.next is not None):
		temp = curr.next
		curr.next = curr.next.next
		temp.next = head
		head = temp
	return head