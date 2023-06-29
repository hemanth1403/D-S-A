n = int(input())
ls = list(map(int, input().split()))
profit = 0
for i in range(1, n):
    if (ls[i] > ls[i-1]):
        profit += ls[i] - ls[i-1]
print(profit)
