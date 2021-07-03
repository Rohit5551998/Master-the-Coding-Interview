class MyArray:
	def __init__(self):
		self.length = 0
		self.data = {}

	def get(self, index):
		return self.data[index]
	
	def push(self, element):
		self.data[self.length] = element
		self.length += 1

	def pop(self):
		element = self.data[self.length-1]
		del self.data[self.length - 1]
		self.length -= 1
		return element 

	def shiftItems(self, index):
		for i in range(index, self.length-1):
			self.data[i] = self.data[i+1]
		del self.data[self.length - 1]
		self.length -= 1

	def delete(self, index):
		element = self.data[index]
		self.shiftItems(index)
		return element
		

if __name__ == "__main__":
	arr1 = MyArray()
	arr1.push('hi')
	arr1.push('hello')
	arr1.push('you')
	arr1.push(1)
	arr1.pop()
	arr1.delete(1)
	print(vars(arr1))