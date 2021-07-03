class Node:
	def __init__(self, val):
		self.value = val
		self.next = None

class LinkedList:
	def __init__(self, val):
		self.head = Node(val)
		self.tail = self.head
		self.length = 1

	def append(self, val):
		newNode = Node(val)
		self.tail.next = newNode 
		self.tail = self.tail.next
		self.length += 1

	def prepend(self, val):
		newNode = Node(val)
		newNode.next = self.head
		self.head = newNode
		self.length += 1

	def insert(self, index, val):
		if index == 0:
			self.prepend(val)

		elif (index >= self.length):
			self.append(val)

		else:
			newNode = Node(val)
			temp = self.head
			for i in range(1, index):
				temp = temp.next
			newNode.next = temp.next
			temp.next = newNode
			self.length += 1

	def remove(self, index):
		if index == 0:
			temp = self.head
			self.head = self.head.next
			print(temp.value)
			self.length -= 1
			del temp

		elif (index >= self.length):
			print("Wrong Input")

		else:
			curr = self.head
			for i in range(1, index):
				curr = curr.next
			temp = curr.next
			if temp.next == None:
				self.tail = curr
			curr.next = curr.next.next
			print(temp.value)
			self.length -= 1
			del temp

	def printList(self):
		array1 = []
		currentNode = self.head
		while(currentNode != None):
			array1.append(currentNode.value)
			currentNode = currentNode.next
		return print(f'{array1} with length {self.length}')

	def reverse(self):
		if (not self.head.next):
			return self.head

		else:
			curr = self.head
			self.tail = self.head
			while(curr.next is not None):
				temp = curr.next
				curr.next = curr.next.next
				temp.next = self.head
				self.head = temp
			return self.head


ll = LinkedList(10)
ll.append(5)
ll.append(16)
ll.prepend(1)
ll.insert(2, 99)
ll.remove(4)
ll.append(55)
ll.printList()
ll.reverse()
ll.printList()