directions = [[-2, -1], [-2, 1], [-1, 2], [-1, -2], [2, 1], [2, -1], [1, -2], [1, 2]]

#Recursive Solution
def knightProbability(n, k, row, col):
	if (row<0 or row>=n or col<0 or col>=n):
		return 0
	
	if (k == 0):
		return 1

	res = 0

	for i in range(len(directions)):
		dir = directions[i]
		res += knightProbability(n, k-1, row+dir[0], col+dir[1])/8

	return res

#Memoization
def knightProbability(n, k, row, col):
	dp = [[[0 for i in range(n)] for i in range(n)] for i in range(k+1)]

	return recurse(n, k, row, col, dp)

def recurse(n, k, row, col, dp):
	if (row<0 or row>=n or col<0 or col>=n):
		return 0

	if (k == 0):
		return 1

	if (dp[k][row][col]):
		return dp[k][row][col]

	res = 0
	for i in range(len(directions)):
		dir = directions[i]
		res += recurse(n, k-1, row+dir[0], col+dir[1], dp)/8

	dp[k][row][col] = res

	return dp[k][row][col]

#Bottom Up Approach
def knightProbability(n, k, row, col):
	dp = [[[0 for i in range(n)] for i in range(n)] for i in range(k+1)]

	dp[0][row][col] = 1

	for step in range(1, k+1):
		for row in range(0, n):
			for col in range(0, n):
				for i in range(len(directions)):
					dir = directions[i]
					prevRow = row + dir[0]
					prevCol = col + dir[1]

					if (prevRow >= 0 and prevRow < n and prevCol >= 0 and prevCol < n):
						dp[step][row][col] += dp[step-1][prevRow][prevCol] / 8

	res = 0
	for i in range(n):
		for j in range(n):
			res += dp[k][i][j]
	
	return res

#Bottom Up Optimization
def knightProbability(n, k, row, col):
	prevDp = [[0 for i in range(n)] for j in range(n)]
	currDp = [[0 for i in range(n)] for j in range(n)]
	
	prevDp[row][col] = 1

	for step in range(1, k+1):
		for row in range(0, n):
			for col in range(0, n):
				for i in range(len(directions)):
					dir = directions[i]
					prevRow = row + dir[0]
					prevCol = col + dir[1]

					if (prevRow >= 0 and prevRow < n and prevCol >= 0 and prevCol < n):
						currDp[row][col] += prevDp[prevRow][prevCol] / 8

		prevDp = currDp
		currDp = [[0 for i in range(n)] for j in range(n)]

	res = 0
	for i in range(n):
		for j in range(n):
			res += prevDp[i][j]
	
	return res
