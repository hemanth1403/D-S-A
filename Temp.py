# 9
# 34 35 27 42 5 28 39 20 28

n = int(input())
ls = list(map(int, input().split()))[::-1]
stack = []
ans = [-1]*n
for i in range(n):
    if (len(stack) == 0):
        stack.append(i)
    else:
        if ls[stack[-1]] < ls[i]:
            stack.append(i)
        else:
            while (len(stack) > 0):
                ele = ls[stack[-1]]
                if (ele <= ls[i]):
                    stack.append(i)
                    break
                else:
                    ans[stack[-1]] = ls[i]
                    stack.pop()
            stack.append(i)
print(ans[::-1])
