def rotatedBinarySearch(ls, key, s, e):
    if(s>e):
        return -1
    m = (s+e)//2
    if(ls[m] == key):
        return m
    if(ls[s] <= ls[m]):
        if(key >= ls[s] and key <= ls[m]):
            return rotatedBinarySearch(ls, key, s, m-1)
        else:
            return rotatedBinarySearch(ls, key, m+1, e)
    if(key >= ls[m] and key <= ls[e]):
        return rotatedBinarySearch(ls, key, m+1, e)
    else:
        return rotatedBinarySearch(ls, key, s, m-1)

ls = [5, 6, 7, 8, 1, 2, 3]
print(rotatedBinarySearch(ls, 8, 0, len(ls)-1))