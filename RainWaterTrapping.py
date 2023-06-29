n = int(input())
ls = list(map(int, input().split()))
left = []
right = []
for i in range(n):
    if (len(left) == 0):
        left.append(ls[i])
    else:
        if (left[-1] < ls[i]):
            left.append(ls[i])
        else:
            left.append(left[-1])
# print(left)
for i in range(n-1, -1, -1):
    if (len(right) == 0):
        right.append(ls[i])
    else:
        if (right[0] < ls[i]):
            right.insert(0, ls[i])
        else:
            right.insert(0, right[0])
# print(right)
ans = 0
for i in range(n):
    ans += min(left[i], right[i]) - ls[i]
print(ans)
