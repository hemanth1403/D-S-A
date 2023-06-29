ls = list(map(int, input().split()))
for i in range(1, len(ls)):
    temp = ls[i]
    j = i-1
    while (j >= 0 and ls[j] > temp):
        ls[j+1] = ls[j]
        j -= 1
    ls[j+1] = temp
print(ls)
