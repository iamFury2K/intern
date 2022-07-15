class Node:
	def __init__(self, data=None, link=None):
		self.data = data
		self.link = link

class LinkedList:
	def __init__(self):
		self.head = None
		
	def insert_at_beginning(self, data):
		node = Node(data, self.head)
		self.head = node
		
	def display(self):
		itr = self.head
		llstr = ''
		while itr:
			if itr is None:
				print('List is empty')
			
			print(itr.data)
			itr = itr.link

	def insert_at_last(self, data):
		tail = self.head
		for i in range(len(data)):
			tail.data = data
				
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.display()
