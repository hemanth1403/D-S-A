def insertionSort(ls):
    for i in range(len(ls)):
        temp = ls[i]
        j = i-1
        while(j>=0 and ls[j]>temp):
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = temp
    return ls

print(insertionSort([8, 2, 1])) 