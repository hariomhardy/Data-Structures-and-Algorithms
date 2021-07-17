class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        node = Tree(data)
        t= self
        while t is not None:
            if data > t.data:
                t = t.right
            else:
                t = t.left
        t = node

    def inorder(self):
        self.inorder(self.left)
        print(self.data)
        self.inorder(self.right)

tree = Tree(10)
tree.insert(5)
tree.insert(12)
tree.inorder()
