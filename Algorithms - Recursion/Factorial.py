def findFactorialRecursive(num):
	if (num == 0 or num == 1):
		return 1
	else:
		return num * findFactorialRecursive(num - 1) 

def findFactorialIterative(num):
	if (num == 0 or num == 1):
		return 1
	factorial = 1
	for i in range(2, num+1):
		factorial *= i
	return factorial

print(findFactorialRecursive(5))
print(findFactorialIterative(5))