heights = [7, 1, 2, 3, 9]

def naiveMostWater(heights):
	maxWater = 0
	for p1 in range(0, len(heights)):
		for p2 in range(p1 + 1, len(heights)):
			currWater = min(heights[p1], heights[p2]) * abs(p2 - p1)
			maxWater = max(maxWater, currWater)
	return maxWater

def mostWater(heights):
	p1 = 0
	p2 = len(heights) - 1
	maxWater = 0
	while(p1 < p2):
		height = min(heights[p1], heights[p2])
		width = p2 - p1
		area = height * width
		maxWater = max(maxWater, area)
		if(heights[p1] <= heights[p2]):
			p1 += 1
		else:
			p2 -= 1
	return maxWater

print(mostWater(heights))
