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

	def BFS(self):
		curr = self.root
		list1 = []
		queue = []
		queue.append(curr)
		
		while(len(queue) > 0):
			curr = queue.pop(0)
			list1.append(curr.val)
			if curr.left:
				queue.append(curr.left)
			if curr.right:
				queue.append(curr.right)

		return print(list1)

	def BFSRecursive(self, queue, list1):
		if not len(queue):
			return list1
		curr = queue.pop(0)
		list1.append(curr.val)
		if curr.left:
			queue.append(curr.left)
		if curr.right:
			queue.append(curr.right)
		return self.BFSRecursive(queue, list1)

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.PrintTree(tree.root)
tree.BFS()
print(tree.BFSRecursive([tree.root], []))
