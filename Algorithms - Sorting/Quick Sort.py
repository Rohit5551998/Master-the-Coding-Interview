arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def partition(arr, low, high):
  i = (low-1)      
  pivot = arr[high]     
  
  for j in range(low, high):
		if (arr[j] <= pivot):
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return (i+1)


def quickSort(arr, low, high):
  if len(arr) == 1:
    return arr

  if low < high:
    pi = partition(arr, low, high)
  
    quickSort(arr, low, pi-1)
  	quickSort(arr, pi+1, high)

quickSort(arr, 0, len(arr)-1)
print(arr)