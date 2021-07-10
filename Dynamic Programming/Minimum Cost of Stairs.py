cost = [20, 15, 30, 5]

#Top Down Approach
def minCost(i, cost, dp):
	if i < 0:
		return 0

	if i == 0 or i == 1:
		return cost[i]

	if (dp[i] != None):
		return dp[i]

	dp[i] = cost[i] + min(minCost(i-1, cost, dp), minCost(i-2, cost, dp))

	return dp[i]


def minCostClimbingStairs(cost):
	n = len(cost)
	dp = []

	return min(minCost(n-1, cost, dp), minCost(n-2, cost, dp))

#Bottom Up Approach
def minCostClimbingStairs(cost):
	dp = []
	n = len(cost)

	for i in range(n):
		if (i<2):
			dp[i] = cost[i]

		else:
			dp[i] = cost[i] + min(dp[i-1], dp[i-2])

#Bottom Up Optimization
def minCostClimbingStairs(cost):
	n = len(cost)
	if(n == 0): return 0
	if(n == 1): return cost[0]

	dpOne = cost[0]
	dpTwo = cost[1]

	for i in range(2, n):
		currDp = cost[i] + min(dpOne, dpTwo)
		dpOne = dpTwo
		dpTwo = currDp

	return min(dpOne, dpTwo)