class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def peek(self):
		return print(self.first.val)

	def isEmpty(self):
		return print(True) if self.length == 0 else print(False)

	def enqueue(self, val):
		newNode = Node(val)
		if (self.first == None):
			self.first, self.last = newNode, newNode
		else:
			self.last.next = newNode
			self.last = newNode
		self.length += 1
			
	def dequeue(self):
		curr = self.first
		if(self.first == self.last):
			self.first, self.last = None, None
		else:
			self.first = self.first.next
		print(curr.val)
		del curr
		self.length -= 1

queue = Queue()
queue.enqueue("Google")
queue.enqueue("Udemy")
queue.enqueue("Discord")
queue.peek()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.isEmpty()