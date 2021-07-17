import random

class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def add(self,value):
        h = Tree(value)
        if value > self.value:
            if self.right != None:
                self.right.add(value)
            else:
                self.right = h

        else:
            if self.left != None:
                self.left.add(value)
            else:
                self.left = h

    def inorder(self):
        if self.left != None:
            self.left.inorder()
            
        print(self.value)

        if self.right != None:
            self.right.inorder()
            
t = Tree(5)
for i in range(10):
    r = random.randint(0,100)
    print(r)
    t.add(r)

print("order")
t.inorder()
