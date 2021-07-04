arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def merge(nums, low, mid, high):
	temp = [0] * len(nums)
	i, j = low, mid + 1
	k = low
	while(i <= mid and j <= high):
		if (nums[i] < nums[j]):
			temp[k] = nums[i]
			i += 1
		else:
			temp[k] = nums[j]
			j += 1
		k += 1

	while(i <= mid):
		temp[k] = nums[i]
		i, k = i+1, k+1

	while(j <= high):
		temp[k] = nums[j]
		j, k = j+1, k+1
	
	for i in range(low, high+1):
		nums[i] = temp[i]

def mergeSort(nums, low, high):
	if (low < high):

		mid = (low+high)//2
		
		mergeSort(nums, low, mid)
		mergeSort(nums, mid+1, high)
		
		merge(nums, low, mid, high)


mergeSort(arr, 0, len(arr)-1)
print(arr)