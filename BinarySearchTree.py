class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.head = None
    def create(self, val):
        self.node = Node(val)
        if(self.head == None):
            self.head = self.node
        else:
            self.temp = self.head
            while True:
                if(self.temp.data > self.node.data):
                    # self.temp = self.temp.left
                    if(self.temp.left != None):
                        self.temp = self.temp.left
                    else:
                        self.temp.left = self.node
                        break
                elif(self.temp.data < self.node.data):
                    if(self.temp.right != None):
                        self.temp = self.temp.right
                    else:
                        self.temp.right = self.node
                        break
                else:
                    print("Node already EXISTS")
    def display(self):
        self.temp = self.head
        while(self.temp != None):
            print(self.temp.data)
            self.temp = self.temp.left
    def inorder(self, root):
        if(root!= None):
            self.inorder(root.left)
            print(root.data, end = " ")
            self.inorder(root.right)
    def preorder(self, root):
        if(root != None):
            print(root.data, end = " ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if(root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end= " ")

bt = BST()
bt.create(1)
bt.create(0)
bt.create(2)
bt.inorder(bt.head)
print()
bt.preorder(bt.head)
print()
bt.postorder(bt.head)
