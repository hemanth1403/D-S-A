n = int(input())
ls = list(map(int, input().split()))
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
                if (ele < ls[i]):
                    stack.append(i)
                    break
                else:
                    ans[stack[-1]] = ls[i]
                    stack.pop()
print(ans)

# input =
# 12
# 10 13 18 15 20 18 25 12 15 6 10 8
