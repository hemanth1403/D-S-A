class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None
        self.last = None

    def create(self, val):
        self.node = Node(val)
        if (self.head == None):
            self.head = self.node
            self.last = self.node
        else:
            self.last.next = self.node
            self.last = self.node

    def insertFirst(self, val):
        self.node = Node(val)
        self.node.next = self.head
        self.head = self.node

    def insertLast(self, val):
        self.node = Node(val)
        # self.last.next = self.node
        # self.last = self.node
        self.temp = self.head
        while (self.temp.next != None):
            self.temp = self.temp.next
        self.temp.next = self.node

    def deleteFirst(self):
        self.temp = self.head.next
        self.head = self.temp

    def deleteLast(self):
        self.temp = self.head
        self.poTemp = self.temp.next
        while (self.poTemp.next != None):       # Not Working
            self.temp = self.temp.next
            self.poTemp = self.temp.next
        self.last = self.temp

    def display(self):
        self.temp = self.head
        while (self.temp != None):
            print(self.temp.data, end=' ')
            self.temp = self.temp.next


sll = SingleLL()
sll.create(2)
sll.create(3)
sll.insertFirst(4)
sll.display()
print('\n')
sll.insertLast(5)
sll.display()
print('\n')
sll.deleteFirst()
# sll.deleteLast()
sll.display()
