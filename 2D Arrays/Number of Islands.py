from collections import deque

matrix = [[1, 1, 1, 1, 0],
					[1, 1, 0, 1, 0],
					[1, 1, 0, 0, 1],
					[0, 0, 0, 1, 1]]

directions = [[-1, 0],
							[0, 1],
							[1, 0],
							[0, -1]]

def numberofIslands(matrix):
	if len(matrix) == 0:
		return 0

	islandCount = 0

	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[0])):
			if matrix[row][col] == 1:
				islandCount += 1
				matrix[row][col] = 0 

				queue = deque()
				queue.append([row, col])

				while (len(queue)):
					currNode = queue.popleft()
					currRow = currNode[0]
					currCol = currNode[1]

					for i in range(0, len(directions)):
						currDir = directions[i]
						nextRow = currRow + currDir[0]
						nextCol = currCol + currDir[1]

						if(nextRow < 0 or nextRow >= len(matrix) or nextCol < 0 or nextCol >= len(matrix[0])):
							continue

						if(matrix[nextRow][nextCol] == 1):
							queue.append([nextRow, nextCol])
							matrix[nextRow][nextCol] = 0

	return islandCount

print(numberofIslands(matrix))
