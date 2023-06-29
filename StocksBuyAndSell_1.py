n = int(input())
ls = list(map(int, input().split()))
maxPrice = ls[0]
minPrice = ls[0]
maxProfit = 0
for i in range(n):
    if (minPrice < ls[i]):
        profit = ls[i] - minPrice
        if (maxProfit < profit):
            maxProfit = profit
    else:
        minPrice = ls[i]
print(maxProfit)
