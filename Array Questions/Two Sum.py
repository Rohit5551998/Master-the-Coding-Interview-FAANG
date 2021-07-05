nums = [9, 2, 7, 1, 3]

def naiveTwoSum(nums, target):
	numLen = len(nums)
	for p1 in range(0, numLen):
		numToFind = target - nums[p1]
		for p2 in range(p1+1, numLen):
			if (numToFind == nums[p2]):
				return [p1, p2]
	return None

def twoSum(nums, target):
	numsMap = {}
	for p in range(0, len(nums)):
		# currVal = numsMap.get(nums[p], None)
		# if (currVal is not None):
		if (nums[p] in numsMap):
			return [numsMap[nums[p]], p]
		else :
			numToFind = target - nums[p]
			numsMap[numToFind] = p
	return None

print(twoSum(nums, 11))