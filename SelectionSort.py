ls = list(map(int, input().split()))
for i in range(len(ls)-1):
    mini = i
    for j in range(i, len(ls)):
        if (ls[j] < ls[mini]):
            mini = j
    if (mini != i):
        ls[i], ls[mini] = ls[mini], ls[i]
print(ls)
