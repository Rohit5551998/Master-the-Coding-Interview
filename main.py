def fibonacciMaster():
	cache = {}
	def fiboInner(n):
		if (n in cache):
			return cache[n]
		else:
			if (n < 2):
				cache[n] = n
				return n
			else:
				cache[n] = fiboInner(n-1) + fiboInner(n-2)
				return cache[n]
	return fiboInner

fibo = fibonacciMaster()
print(fibo(60))