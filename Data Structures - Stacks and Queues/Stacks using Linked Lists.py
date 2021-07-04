class Node:
	def __init__(self, val):
		self.val = val
		self.next = next

class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def peek(self):
		return self.top

	def push(self, value):
		newNode = Node(value)
		if self.top == None:
			self.top, self.bottom = newNode, newNode
		else:
			curr = self.top
			self.top = newNode
			self.top.next = curr

		self.length += 1

	def pop(self):
		curr = self.top
		if (self.top == self.bottom):
			self.top, self.bottom = None, None
		else:
			self.top = self.top.next
		print(curr.val)
		del curr
		self.length -= 1

	def isEmpty(self):
		if self.length > 0:
			return print(False)
		return print(True)

st = Stack()
st.push("Google")
st.push("udemy")
st.push("discord")
st.pop()
st.pop()
st.pop()
st.isEmpty()