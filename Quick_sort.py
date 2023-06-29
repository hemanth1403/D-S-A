def QuickSort_Partion(ls, idx, height):
    i = idx
    j = height
    pivot = ls[i]
    while(i<j):
        while(ls[i]<pivot): i+=1
        while(ls[j]>pivot):j-=1
        if(i<j): ls[i] , ls[j] = ls[j], ls[i]
    ls[j] = pivot
    return j

def QuickSort(ls, idx, height):
    if(idx<height):
        p = QuickSort_Partion(ls, idx, height)
        QuickSort(ls, idx, p-1)
        QuickSort(ls, p+1, height)
        return ls
ls = [8, 2, 1]
print(QuickSort(ls, 0, 2))
# print(ls)