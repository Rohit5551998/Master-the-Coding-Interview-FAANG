nums = [1]
k = 1

def swap(nums, i, j):
	nums[i], nums[j] = nums[j], nums[i]

def partition(nums, left, right):
	pivot = nums[right]
	partitionIndex = left #i
	for j in range(left, right+1):
		if(nums[j] < pivot):
			swap(nums, j, partitionIndex)
			partitionIndex += 1
	swap(nums, partitionIndex, right)
	return partitionIndex

def quickSelect(nums, left, right, k): #k = IndextoFind
	if(left <= right):
		partitionIndex = partition(nums, left, right)	

		if(partitionIndex == k):
			return nums[partitionIndex]
		
		elif(k < partitionIndex):
			return quickSelect(nums, left, partitionIndex - 1)

		elif(k > partitionIndex):
			return quickSelect(nums, partitionIndex+1, right)

print(quickSelect(nums, 0, len(nums) - 1, len(nums) - k))
