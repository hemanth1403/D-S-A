class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Dll:
    def __init__(self):
        self.root = None
        self.last = None
    def create(self, val):
        self.node = Node(val)
        if(self.root == None):
            self.root = self.node
            self.last = self.node
        else:
            # self.last.next = self.node
            n = int(input("Enter on which side you want to enter Left - 0 and Right - 1 : "))
            if(n == 0):
                self.last.left = self.node
                self.last = self.node
            elif(n == 1):
                self.last.right = self.node
                self.last = self.node
    # def Display(self):
    #     self.temp = self.root


def display_inorder(t):
    temp = t
    while(temp.data != None):
        display_inorder(temp.left)
        print(temp.data, end = " ")
        display_inorder(temp.right)

tree = Dll()
while 1:
    n = int(input("If you want to Enter the values (1 | 0): "))
    if( n == 1 ):
        v = int(input("Val : "))
        tree.create(v)
    else:
        break
display_inorder(tree.root)           # Display ---> Not Working
# temp = tree.root
# while(temp.data != None):
