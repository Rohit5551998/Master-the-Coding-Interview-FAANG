directions = [[-1, 0], #UP
							[0, 1],	 #RIGHT
							[1, 0],	 #DOWN
							[0, -1]] #LEFT

matrix = [[1, 2, 3, 4, 5, 6],
					[7, 8, 9, 10, 11, 12],
					[13, 14, 15, 16, 17, 18],
					[19, 20, 21, 22, 23, 24]]

def traversal(matrix):
	seen = [[False for i in range(len(matrix[0]))] for i in range(len(matrix))]
	res = []
	queue = [[0, 0]]

	while (len(queue)):
		currPos = queue.pop(0)
		row = currPos[0]
		col = currPos[1]

		if(row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col] == True):
			continue
		
		seen[row][col] = True
		res.append(matrix[row][col])

		for i in range(0, len(directions)):
			currDir = directions[i]
			queue.append([ row + currDir[0], col + currDir[1] ])

	return res

print(traversal(matrix))