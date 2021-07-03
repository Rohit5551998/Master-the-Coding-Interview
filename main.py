def firstRecChar(list1):
	set1 = set({})
	for i in list1:
		if i in set1:
			return i
		set1.add(i)
	return None

print(firstRecChar([2,5,1,2,3,5,1,2,4]))
print(firstRecChar([2,3,4,5]))