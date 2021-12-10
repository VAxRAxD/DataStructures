import collections
class BinarySearchTree:
	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None

	def addChild(self,data):
		if data==self.data:
			return
		elif data<self.data:
			if self.left:
				self.left.addChild(data)
			else:
				self.left=BinarySearchTree(data)
		else:
			if self.right:
				self.right.addChild(data)
			else:
				self.right=BinarySearchTree(data)

	def inorder(self):
		elements=[]
		if self.left:
			elements+=self.left.inorder()
		elements.append(self.data)
		if self.right:
			elements+=self.right.inorder()
		return elements

	def preorder(self):
		elements=[]
		elements.append(self.data)
		if self.left:
			elements+=self.left.preorder()
		if self.right:
			elements+=self.right.preorder()
		return elements

	def postorder(self):
		elements=[]
		if self.left:
			elements+=self.left.postorder()
		if self.right:
			elements+=self.right.postorder()
		elements.append(self.data)
		return elements

	def levelorder(self):
		elements=[]
		buffer=collections.deque()
		buffer.appendleft(self)
		while len(buffer)!=0:
			size=len(buffer)
			level=[]
			for i in range(size):
				node=buffer[-1]
				buffer.pop()
				if node.left: buffer.appendleft(node.left)
				if node.right: buffer.appendleft(node.right)
				level.append(node.data)
			elements+=level
		return elements

	def search(self,data):
		if self.data==data:
			return "Element found"
		if data<self.data:
			if self.left:
				return self.left.search(data)
			else:
				return "Element not found"
		if data>self.data:
			if self.right:
				return self.right.search(data)
			else:
				return "Element not found"

	def delete(self,data):
		if self.search(data)=="Element not found":
			return "Element not found"
		if data<self.data:
			self.left=self.left.delete(data)
		elif data>self.data:
			self.right=self.right.delete(data)
		else:
			if self.child(self.data)==0:
				return None
			if self.left is None: 
				return self.right
			if self.right is None:
				return self.left
			min_val=self.right.minimum()
			self.data=min_val
			self.right=self.right.delete(min_val)
		return self


	def child(self,data):
		if self.search(data)=="Element not found":
			return "Element not found"
		children=0
		if self.data==data:
			if self.right : children+=1
			if self.right : children+=1
		if data<self.data:
			if self.left:
				children+=self.left.child(data)
		if data>self.data:
			if self.right:
				children+=self.right.child(data)
		return children

	def maximum(self):
		if self.right is None:
			return self.data
		else:
			return self.right.maximum()

	def minimum(self):
		if self.left is None:
			return self.data
		else:
			return self.left.minimum()


def build(arr):
	root=BinarySearchTree(arr[0])
	for i in range(1,len(arr)):
		root.addChild(arr[i])
	return root

numbers=[17,4,1,20,9,23,18,34]
root=build(numbers)
print(root.inorder())
print(root.preorder())
print(root.postorder())
print(root.levelorder())
print(root.search(9))
print(root.maximum())
print(root.minimum())
print(root.child(34))
root.delete(4)
print(root.inorder())