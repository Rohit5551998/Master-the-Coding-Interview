nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(nums):
	numLen = len(nums)
	for i in range(0, numLen):
		for j in range(0, numLen-i-1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]

bubbleSort(nums)
print(nums)