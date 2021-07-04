def fibonacciRecursive(num):
	if (num == 0 or num == 1):
		return num
	else:
		return fibonacciRecursive(num - 1) + fibonacciRecursive(num - 2)

def fibonacciIterative(num):
	if (num < 2):
		return num
	arr = [0, 1]
	for i in range(2, num+1):
		arr.append(arr[i-1] + arr[i-2])
	return arr[num]

print(fibonacciIterative(30))
print(fibonacciRecursive(30))

