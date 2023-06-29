class Stack:
    def __init__(self, s):
        self.size = s
        self.st = []
        self.top = -1
    def push(self, ele):
        if(self.top < self.size - 1):
            self.st.append(ele)
            self.top+=1
        else:
            print("Stack is Full")
    def pop(self):
        if(self.top>=0):
            del self.st[self.top]
            self.top -= 1
        else:
            print("Stack is Emplty")
    def display(self):
        print(self.st[::-1])
    def peek(self):
        print(self.st[self.top])
n=int(input())
s = Stack(n)
s.push(2)
s.push(3)
s.push(4)
s.display()
s.pop()
s.pop()
s.peek()
s.display()