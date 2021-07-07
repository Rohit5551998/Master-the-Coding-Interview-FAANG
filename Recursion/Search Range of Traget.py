nums = [1, 3, 3, 5, 5, 5, 8, 9]

def binarySearch(nums, left, right, target):
	while(left <= right):
		mid = (left + right)//2

		if(nums[mid] == target):
			return mid

		elif(target < nums[mid]):
			right = mid - 1

		else:
			left = mid + 1

	return -1

def searchRange(nums, target):
	if (len(nums) == 0):
		return [-1, -1]

	firstPos = binarySearch(nums, 0, len(nums)-1, target)

	if(firstPos == -1): 
		return [-1, -1]

	startPos, endPos = firstPos, firstPos

	while (startPos != -1):
		temp1 = startPos
		startPos = binarySearch(nums, 0, startPos - 1, target)

	while (endPos != -1):
		temp2 = endPos
		endPos = binarySearch(nums, endPos + 1, len(nums) - 1, target)

	return [temp1, temp2]

print(searchRange(nums, 5))