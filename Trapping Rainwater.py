heights = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
def naiveRainWater(heights) -> int:
	totalWater = 0
	#Check each index in array
	for i in range(0, len(heights)):
		#Initialize variables for current run
		currHeight = heights[i]
		maxL, maxR = 0, 0
		currArea = 0
		#Check all elements to left and set max
		for j in range(0, i):
			if (heights[j] > maxL):
				maxL = heights[j]
		#Check all elements to right and set max
		for j in range(i+1, len(heights)):
			if (heights[j] > maxR):
				maxR = heights[j]
		#Calculate area trapped by current index
		currArea = min(maxL, maxR) - currHeight
		if (currArea > 0):
			totalWater += currArea
	return totalWater

def rainWater(heights):
	totalWater = 0
	maxLeft, maxRight = 0, 0
	currLeft, currRight = 0, len(heights) - 1
	while(currLeft < currRight):
		if(heights[currLeft] <= heights[currRight]):
			if(heights[currLeft] >= maxLeft):
				maxLeft = heights[currLeft]
			else:
				totalWater += (maxLeft - heights[currLeft])
				# print("Left", totalWater)
			currLeft += 1
		else:
			if(heights[currRight] >= maxRight):
				maxRight = heights[currRight]
			else:
				totalWater += (maxRight - heights[currRight])
				# print("Right", totalWater)
			currRight -= 1
	return totalWater

print(rainWater(heights))