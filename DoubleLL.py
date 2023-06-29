class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
        self.head = None
        self.last = None
    def insert(self, val):
        self.node = Node(val)
        if(self.head == None):
            self.head = self.node
            self.last = self.node
        else:
            self.last.next = self.node
            self.node.prev = self.last
            self.last = self.node
    def delete(self):
        self.last = self.last.prev
        self.last.next = None
    def insertMid(self, val, before):
        self.node = Node(val)
        self.temp = self.head
        while(self.temp != None):
            if(self.temp.data == before):
                self.temp1 = self.temp.prev
                self.temp1.next = self.node
                self.node.prev = self.temp1
                self.node.next = self.temp
                self.temp.prev = self.node
                break
            else:
                self.temp = self.temp.next
    def deleteMid(self, val):
        self.temp = self.head
        while(self.temp != None):
            if(self.temp.data == val):
                self.temp1 = self.temp.prev
                self.temp2 = self.temp.next
                self.temp1.next = self.temp2
                self.temp2.prev = self.temp1
                break
            else:
                self.temp = self.temp.next
    def display(self):
        self.temp = self.head
        while(self.temp != None):
            print(self.temp.data, end= " ")
            self.temp = self.temp.next
        print()

dll = Dll()
dll.insert(20)
dll.insert(30)
dll.insertMid(10, 30)
dll.display()
dll.deleteMid(10)
dll.display()