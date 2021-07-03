def mergeSorted(l1, l2):
	mergedArray = []
	f1, f2 = 0, 0
	
	if (len(l1) == 0):
		return l2

	if (len(l2) == 0):
		return l1

	while (f1 < len(l1) and f2 < len(l2)):
		if (l1[f1] < l2[f2]):
			mergedArray.append(l1[f1])
			f1 += 1
		else:
			mergedArray.append(l2[f2])
			f2 += 1

	while (f1 < len(l1)):
		mergedArray.append(l1[f1])
		f1 += 1

	while (f2 < len(l2)):
		mergedArray.append(l2[f2])
		f2 += 1

	return mergedArray

print(mergeSorted([0, 3, 4, 31], [4, 6, 30, 70]))