nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(nums):
	numLen = len(nums)
	for i in range(1, numLen):
		key = nums[i]
		j = i-1
		while (j >= 0 and key < nums[j]):
			nums[j+1] = nums[j]
			j -= 1
		nums[j+1] = key

insertionSort(nums)
print(nums)