class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, val):
		newNode = Node(val)
		if (self.root == None):
			self.root = newNode
		else:
			curr = self.root
			while(True):
				if(val < curr.val):
					#Left
					if not (curr.left):
						curr.left = newNode
						return
					else:
						curr = curr.left
				else:
					#Right
					if not (curr.right):
						curr.right = newNode
						return
					else:
						curr = curr.right

	def lookup(self, val):
		if not self.root:
			return print("Value Not Found")
		else:
			curr = self.root
			while(curr):
				if (val < curr.val):
					curr = curr.left
				elif (val > curr.val):
					curr = curr.right
				elif (curr.val == val):
					print(f'Val: {curr.val}, Left: {curr.left}, Right: {curr.right}')
					return print("Value Found")
			return print("Value Not Found")

	def PrintTree(self, root):
		node = root
		print(root.val)
		# print(f'Val: {node.val}, Left: {node.left}, Right: {node.right}')
		if (node.left):
			self.PrintTree(node.left)
		if (node.right):
			self.PrintTree(node.right)
		return self

	def DFSInOrder(self, root, list1):
		if root == None:
			return list1

		self.DFSInOrder(root.left, list1)
		list1.append(root.val)
		self.DFSInOrder(root.right, list1)
		return list1
	
	def DFSPreOrder(self, root, list1):
		if root == None:
			return list1

		list1.append(root.val)
		self.DFSPreOrder(root.left, list1)
		self.DFSPreOrder(root.right, list1)
		return list1

	def DFSPostOrder(self, root, list1):
		if root == None:
			return list1

		self.DFSPostOrder(root.left, list1)
		self.DFSPostOrder(root.right, list1)
		list1.append(root.val)
		return list1
		


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.PrintTree(tree.root)
print(tree.DFSInOrder(tree.root, []))
print(tree.DFSPreOrder(tree.root, []))
print(tree.DFSPostOrder(tree.root, []))
