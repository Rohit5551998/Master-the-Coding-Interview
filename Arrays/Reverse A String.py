def reverse1(str1):
	if (not str1 or type(str1) != str or len(str1) == 1):
		return str1

	#return str1[::-1]
	totalItems = len(str1) - 1
	temp = [''] * (totalItems + 1)
	for i in range(totalItems, -1, -1):
		temp.append(str1[i])
	return "".join(temp)


def reverse2(str1):

	if (not str1 or type(str1) != str or len(str1) == 1):
		return str1

	low = 0
	high = len(str1) - 1
	temp = ['']*(high+1)
	while(low < high):
		temp[low], temp[high] = str1[high], str1[low]
		low += 1
		high -= 1
	return str("".join(temp))

string = "Hi My name is Rohit"
print(reverse2(string))