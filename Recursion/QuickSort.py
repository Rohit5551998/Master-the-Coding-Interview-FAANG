nums = [5, 3, 1, 6, 4, 2]

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

def quickSort(nums, left, right):
	if(left < right):
		partitionIndex = partition(nums, left, right)	

	quickSort(nums, left, partitionIndex - 1)
	quickSort(nums, partitionIndex+1, right)

print(quickSort(nums, 0, len(nums) - 1))

#Can be used for Kth Largest Element