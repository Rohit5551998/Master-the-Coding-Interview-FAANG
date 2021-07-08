directions = [[-1, 0], #UP
							[0, 1],	 #RIGHT
							[1, 0],	 #DOWN
							[0, -1]] #LEFT

matrix = [[1, 2, 3, 4, 5, 6],
					[7, 8, 9, 10, 11, 12],
					[13, 14, 15, 16, 17, 18],
					[19, 20, 21, 22, 23, 24]]

def dfs(matrix, row, col, seen, res):
	if (row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col] == True):
		return

	res.append(matrix[row][col])
	seen[row][col] = True

	for i in range(0, len(directions)):
		currDir = directions[i]
		dfs(matrix, row + currDir[0], col + currDir[1], seen, res)

	

def traversal(matrix):
	seen = [[False for i in range(len(matrix[0]))] for i in range(len(matrix))]
	res = []

	dfs(matrix, 0, 0, seen, res)

	return res

print(traversal(matrix))
