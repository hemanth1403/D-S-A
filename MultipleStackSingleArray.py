class Stack:
    def __init__(self, n):
        self.ls = []
        self.top = -1
        self.size = n

    def push(self, ele):
        if (self.top <= self.size-1):
            self.ls.append(ele)
            self.top += 1
        else:
            print("Stack Overflow")

    def pop(self):
        if (self.top >= 0):
            del self.ls[self.top]
            self.top -= 1
        else:
            print("Stack UnderFlow")

    def peek(self):
        return self.ls[self.top]

    def display(self):
        # self.temp = self.top
        for i in range(self.top, -1, -1):
            print(self.ls[i], end=" ")
        print()


# s = Stack(5)
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.pop()
# print(s.peek())
# s.display()

def add(stackNo, ele, ls, pre, aval, top):
    if (len(aval) > 0):
        address = aval.pop()
        ls[address] = ele
        prev = top[stackNo]
        top[stackNo] = address
        pre[top[stackNo]] = prev

# Should Figure out (references) -> Code rough book, smartInterviews book


def solv(n, nstack, q):
    ls = [0]*n
    pre = [-1]*n
    aval = [i for i in range(0, n)]
    top = [-1]*nstack
    while (q > 0):
        stackNo, ele = map(int, input().split())
        add(stackNo, ele, ls, pre, aval, top)
        print(stackNo, ele, ls, pre, aval, top)
        q -= 1


n = int(input())
nstack = int(input())
q = int(input())
solv(n, nstack, q)
