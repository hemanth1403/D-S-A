class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SingleLL:
    def __init__(self):
        self.head = None
        self.last = None                    # Actually there is no use of self.last and IN interviews they 
                                            # Just give you the head
    def create(self, val):
        self.node = Node(val)
        if (self.head == None):
            self.head = self.node
            self.last = self.node
        else:
            self.last.next = self.node
            self.last = self.node

    def reverseFull(self):
        self.prev = None
        self.cur = self.head
        while(self.cur != None):
            self.temp = self.cur.next
            self.cur.next = self.prev
            self.prev = self.cur
            self.cur = self.temp
        self.head = self.prev

    def reverseSub(self, left, right):
        if(left == 1):
            self.end = None
            self.t0 = self.head
            self.ec = left
            while(self.t0 != None):
                if(self.ec == right):
                    break
                else:
                    self.t0 = self.t0.next
                    self.ec += 1
            self.end = self.t0.next
            self.prev = None
            self.cur = self.head
            while(self.cur != None):
                if(left == right+1):
                    break
                else:
                    self.temp = self.cur.next
                    self.cur.next = self.prev
                    self.prev = self.cur
                    self.cur = self.temp
                    left += 1
            self.head = self.prev
            self.t2 = self.head
            # while(self.temp.next != None):
            #     self.temp = self.temp.next
            # self.temp.next = self.end
            while(self.t2.next != None):
                # print(self.t2.data, end =' ')
                self.t2 = self.t2.next
            self.t2.next = self.end
            # print()
        else:
            self.t1 = self.head
            self.start = None
            self.lc = 1
            while(self.t1 != None):
                if(self.lc == left - 1):
                    self.start = self.t1
                    break
                else:
                    self.t1 = self.t1.next
                    self.lc += 1
            self.rc = self.lc
            self.end = self.start
            while(self.end != None):
                if(self.rc == right):
                    break
                else:
                    self.end = self.end.next
                    self.rc += 1
            self.prev = None
            self.cur = self.start.next
            while(self.cur != None):
                if(self.lc == self.rc):
                    # print(self.cur.next.data)
                    break
                else:
                    self.temp = self.cur.next
                    self.cur.next = self.prev
                    self.prev = self.cur
                    self.cur = self.temp
                    self.lc += 1
            self.start.next = self.prev
            self.t1 = self.head
            while(self.t1.next != None):
                self.t1 = self.t1.next
            self.t1.next = self.cur

    def display(self):
        self.temp = self.head
        while(self.temp != None):
            print(self.temp.data, end = ' ')
            self.temp = self.temp.next
        print()

    def fur(self):
        print((self.head.next).data)
        # print(self.head.data)

sll = SingleLL()
sll.create(2)
sll.create(3)
sll.create(4)
sll.create(5)
sll.create(6)
sll.create(7)
sll.display()
# sll.reverseFull()
sll.reverseSub(3,4)    # Working for except 1 as a starting index -> (RESOLVED)
sll.display()
# sll.fur()
