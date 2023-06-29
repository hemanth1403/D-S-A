n = int(input())
ls = list(map(int, input().split()))
maxSum = 0
curSum = 0
for i in range(n):
    curSum += ls[i]
    if (maxSum < curSum):
        maxSum = curSum
        # print(".. ", maxSum)
    if (curSum < 0):
        curSum = 0
print(maxSum)
