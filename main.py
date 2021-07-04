def memoizedAddto80():
	cache = {}
	def innerMemoized(n):
		if (n in cache):
			return cache[n]
		else:
			print("Long Time")
			cache[n] = n + 80
			return cache[n]
	return innerMemoized

memoized = memoizedAddto80()
print('1', memoized(5))
print('2', memoized(5))