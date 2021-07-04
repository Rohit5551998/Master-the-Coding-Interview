class Stack:
	def __init__(self):
		self.list1 = []

	def peek(self):
		return self.list1[len(self.list1) - 1]

	def push(self, val):
		self.list1.append(val)

	def pop(self):
		print(self.list1.pop())

	def isEmpty(self):
		return True if len(self.list1) == 0 else False

st = Stack()
st.push("Google")
st.push("udemy")
st.push("discord")
st.pop()
st.pop()
st.pop()
st.isEmpty()