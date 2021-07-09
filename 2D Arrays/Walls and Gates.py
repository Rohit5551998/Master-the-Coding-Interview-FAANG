INF = 2147483647
matrix = [[INF, -1, 0, INF],
					[INF, INF, INF, -1],
					[INF, -1, INF, -1],
					[0, -1, INF, INF]]

WALL = -1
GATE = 0
EMPTY = 2147483647


directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(matrix, row, col, currStep):
	if (row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or currStep > matrix[row][col]):
		return

	matrix[row][col] = currStep

	for i in range(0, len(directions)):
		direction = directions[i]
		dfs(matrix, row+direction[0], col+direction[1], currStep+1)

def WallsAndGates(matrix):

	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[0])):

			if(matrix[row][col] == GATE):
				dfs(matrix, row, col, 0)

	return matrix

print(WallsAndGates(matrix))
