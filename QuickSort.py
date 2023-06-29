def partion(ls, l, h):
    pivot = l
    i = l
    j = h
    while (i < j):
        while (ls[i] <= ls[pivot]):
            i += 1
        while (ls[j] > ls[pivot]):
            j -= 1
        if (i < j):
            ls[i], ls[j] = ls[j], ls[i]
    ls[j], ls[pivot] = ls[pivot], ls[j]
    return j


def QuickSort(ls, l, h):
    if (l < h):
        p = partion(ls, l, h)
        QuickSort(ls, l, p-1)
        QuickSort(ls, p+1, h)


ls = list(map(int, input().split()))
partion(ls, 0, len(ls)-1)
print(ls)
