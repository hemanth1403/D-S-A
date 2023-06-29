# circular queue

from re import T


class CQueue:
    def __init__(self, s):
        self.q = []
        self.front = 0
        self.rear = 0
        self.count = 0
        self.size = s
    def enqueue(self, ele):
        if(self.count == self.size):
            print("Queue OverFlow")
        else:
            self.q.append(ele)
            self.rear = (self.rear + 1)%self.size
            self.count += 1
    def dequeue(self):
        if(self.count == 0):
            print("Queue UnderFlow")
        else:
            del self.q[self.front]
            self.front = (self.front + 1)%self.size
            self.count -= 1
    def display(self):
        return self.q[self.front:self.rear]

q = CQueue(5)
i= 0
while i<6:
    n = int(input())
    if(n == 1):
        n = int(input())
        q.enqueue(n)
        print(q.display())
    else:
        q.dequeue()
        q.display()
    i+=1