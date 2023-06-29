class Stack():
    def __init__(self, s):
        self.size = s
        self.st = []
        self.top = -1
    def push(self, ele):
        if(self.top<self.size-1):
            self.st.append(ele)
            self.top += 1
        else:
            print("Stack is Full")
    def pop(self):
        if(self.top >= 0):
            del self.st[self.top]
            self.top -= 1
        else:
            print("Stack is Empty")
    def peek(self):
        return self.st[self.top]
    def isEmpty(self):
        return self.top < 0


def parenthesis(s):
    sta = Stack(len(s))
    for i in s:
        if i in "({[":
            sta.push(i)
        elif i in ")}]":
            pe = sta.peek()
            sta.pop()
            if(pe != "(" and i == ')') or (pe != "[" and i == ']') or (pe != '{' and i == '}'):
                return False
    if sta.isEmpty():
        return True
    else:
        return False


n = input()
if parenthesis(n):
    print("balenced")
else:
    print("Not Balenced")