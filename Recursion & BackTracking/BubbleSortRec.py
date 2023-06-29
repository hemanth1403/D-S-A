def bubbleSortRec(ls, i, j):
    if(j == 0):
        return
    if(i<j):
        if(ls[i] > ls[i+1]):
            ls[i], ls[i+1] = ls[i+1], ls[i]
        bubbleSortRec(ls, i+1, j)
    else:
        bubbleSortRec(ls, 0, j-1)

ls = [2 ,3, 1, 0, 5]
bubbleSortRec(ls, 0, len(ls)-1)
print(ls)