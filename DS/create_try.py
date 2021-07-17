class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def create(arr):
    if arr:
        root = Node(arr[0])
        add(root,arr,0)
        add(root,arr,0)
        return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def add(root,arr,i):
    if root:
        if 2*i+1 < len(arr) and arr[2*i+1]:
            root.left = Node(arr[2*i+1])
            add(root.left,arr,2*i+1)
        if 2*i+2 < len(arr) and arr[2*i+2]:
            root.right = Node(arr[2*i+2])
            add(root.right,arr,2*i+2)

l = [1,3,5,None,7,13,None] ##level order traversal
root = create(l)
inorder(root)
    
        
        
        
