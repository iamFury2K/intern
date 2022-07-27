class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    def add_child(self, data):
        if self.data == data:
            return
        else:
            if data < self.data:
                if self.left_child:
                    self.add_child(data)
                else:
                    self.left_child = BinarySearchTree(data)
            else:
                 if self.right_child:
                    self.add_child(data)
                 else:
                    self.right_child = BinarySearchTree(data)

                
                