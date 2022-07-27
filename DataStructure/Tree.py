class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.data = child.data
        self.children.append(child)
        child.parent = self
    def display_child(self):
        print(self.data)
        if self.children:
            for runner in self.children:
                runner.display_child() 


#Driver Code
inst1 = TreeNode('Parent')
inst2 = TreeNode('A')
inst2.add_child(TreeNode('X'))
inst2.add_child(TreeNode('Y'))
inst2.add_child(TreeNode('Z'))
inst1.add_child(inst2)

inst1.display_child()
    