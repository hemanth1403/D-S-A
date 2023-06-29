def selectionSort(ls):
    n = len(ls)
    for i in range(n):
        min = ls[i]
        for j in range(i+1, n):
            if(min>ls[j]):
                min = ls[j]
        ind = ls.index(min)
        ls[i], ls[ind] = ls[ind], ls[i]
    return ls
print(selectionSort([8, 2, 1]))