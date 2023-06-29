ls = list(map(int, input().split()))
for i in range(len(ls)-1):
    for j in range(len(ls)-i-1):
        if (ls[j] > ls[j+1]):
            ls[j], ls[j+1] = ls[j+1], ls[j]
print(ls)
