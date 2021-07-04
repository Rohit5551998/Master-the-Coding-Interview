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
					# Left
					if not (curr.left):
						curr.left = newNode
						return
					else:
						curr = curr.left
				else:
					# Right
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
		print(f'Val: {node.val}, Left: {node.left}, Right: {node.right}')
		if (node.left):
			self.PrintTree(node.left)
		if (node.right):
			self.PrintTree(node.right)
		return self

	def remove(self, val):
		if not (self.root):
			return print("No Root Found")
		currentNode = self.root
		parentNode = None
		while (currentNode):
			if (val < currentNode.val):
				parentNode = currentNode
				currentNode = currentNode.left
			elif (val > currentNode.val):
				parentNode = currentNode
				currentNode = currentNode.right
			elif (val == currentNode.val):
			# We have a match, get to work!

      			# Option 1: No right child:
				if currentNode.right == None:
					if parentNode == None:
						self.root = currentNode.left
					else:
						# if parent > current data, make current left child a child of parent
						if currentNode.data < parentNode.data:
							parentNode.left = currentNode.left
						# if parent < current data, make left child a right child of parent
						elif currentNode.data > parentNode.data:
							parentNode.right = currentNode.left

            	# Option 2: Right child which doesnt have a left child
				elif (currentNode.right.left == None):
					currentNode.right.left = currentNode.left
					if parentNode == None:
						self.root = currentNode.right
                  	else:
                    # //if parent > current, make right child of the left the parent
						if currentNode.data < parentNode.data:
							parentNode.left = currentNode.right
                    # //if parent < current, make right child a right child of the parent
						elif currentNode.data > parentNode.data:
							parentNode.right = currentNode.right

              	# Option 3: Right child that has a left child
				else:
                	# find the Right child's left most child
                	leftmost = currentNode.right.left
                	leftmostParent = currentNode.right
                  	while leftmost.left != None:
                    	leftmostParent = leftmost
                    	leftmost = leftmost.left

                		# Parent's left subtree is now leftmost's right subtree
						leftmostParent.left = leftmost.right
						leftmost.left = currentNode.left
                		leftmost.right = currentNode.right

                		if parentNode == None:
                    		self.root = leftmost
                  		else:
                      		if currentNode.data < parentNode.data:
                          		parentNode.left = leftmost
                      		elif currentNode.data > parentNode.data:
								parentNode.right = leftmost

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.PrintTree(tree.root)
print()
tree.lookup(20)
tree.lookup(1)
tree.lookup(55)
