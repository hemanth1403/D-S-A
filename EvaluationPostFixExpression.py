class Stack:
    def __init__(self, s):
        self.size = s
        self.s = []
        self.top = -1
    def push(self, ele):
        if self.top <= self.size -1:
            self.s.append(ele)
            self.top += 1
        else:
            print("Stack is full")
    def pop(self):
        if self.top >= 0:
            del self.s[self.top]
            self.top -= 1
        else:
            print("Stack is Empty")
    def peek(self):
        return self.s[self.top]
    def display(self):
        return self.s[::-1]

n = input()
l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = Stack(len(n))
for i in n:
    if i in l:
        s.push(i)
    else:
        if i == '^':
            v1 = s.peek()
            s.pop()
            v2 = s.peek()
            s.pop()
            s.push(str(int(v2)**int(v1)))
        else:
            v1 = s.peek()
            s.pop()
            v2 = s.peek()
            s.pop()
            s.push(str(eval(v2+i+v1)))
print(s.display())