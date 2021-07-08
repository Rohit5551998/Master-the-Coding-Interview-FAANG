from collections import deque

matrix = [[2, 0, 1, 0, 0],
					[1, 1, 0, 0, 2],
					[0, 1, 1, 1, 1],
					[0, 1, 0, 0, 1]]
					
ROTTEN = 2
FRESH = 1
EMPTY = 0

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def orangesRotting(matrix):
	if len(matrix) == 0:
		return 0

	queue = deque()
	freshOranges = 0

	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[0])):
				
			if (matrix[row][col] == FRESH):
				freshOranges += 1

			if (matrix[row][col] == ROTTEN):
				queue.append([row, col])

	currQueueSize = len(queue)
	minutes = 0

	while (len(queue)):
			
		if (currQueueSize == 0):
			minutes += 1
			currQueueSize = len(queue)

		currentOrange = queue.popleft()
		currQueueSize -= 1

		row, col = currentOrange

		for i in range(0, len(directions)):
			direction = directions[i]
			nextRow = row + direction[0]
			nextCol = col + direction[1]

			if (nextRow < 0 or nextCol < 0 or nextRow >= len(matrix) or nextCol >= len(matrix[0])):
				continue

			if (matrix[nextRow][nextCol] == FRESH):
				matrix[nextRow][nextCol] = ROTTEN
				freshOranges -= 1
				queue.append([nextRow, nextCol])

	return (minutes if (freshOranges == 0) else -1)
print(orangesRotting(matrix)) 
