# Convertion of INFIX EXPRESSION to POSTFIX EXPRESSION using stack
# Time Complexity  => O(n^n)
# Space Complexity => O(n)
class Stack:
    def __init__(self,n):
        self.l = []
        self.size = n
        self.top = -1
    def push(self, n):
        if self.top <= self.size - 1:
            self.l.append(n)
            self.top += 1
        else:
            print("Stack is full")
    def pop(self):
        if self.top >= 0:
            del self.l[self.top]
            self.top -= 1
        else:
            print("Stak is empty")
    def peek(self):
        return self.l[self.top] 
    def display(self):
        return self.l[::-1]
    def isEmpty(self):
        return self.top <= -1


pro = ['$','/', '*', '-', '+', '(']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n = input("Enter a INFIX Expression : ")
s = Stack(len(n))
ls = []
for i in n:
    if i.isalnum():         # or can use isalnum()      # or can use (i in num) or (i >= 'a' and i<= 'z') or (i>= 'A' and a<= 'Z')
        ls.append(i)
    else:
        if i == '(':
            s.push(i)
        elif i == ")":
            while True:
                if s.peek() != '(':
                    ls.append(s.peek())
                    s.pop()
                else:
                    s.pop()
                    break
        else:
            if s.isEmpty():
                s.push(i)
            else:
                if pro.index(i) < pro.index(s.peek()):
                    s.push(i)
                else:
                    ls.append(s.peek())
                    s.pop()
                    s.push(i)
if (not s.isEmpty()):
    ls += s.display()
print(ls)
# print(s.display())


# s = Stack(5)
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.pop()
# print(s.peek())
