nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(nums):
	numLen = len(nums)
	for i in range(0, numLen):
		min = i
		temp = nums[i]
		for j in range(i+1, numLen):
			if (nums[j] < nums[min]):
				min = j
		nums[i] = nums[min]
		nums[min] = temp

selectionSort(nums)
print(nums)