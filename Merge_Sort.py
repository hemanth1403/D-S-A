# 1st method of implementaion using recursion 
def merge(left, right, ls):
    i, j, k= 0, 0, 0
    while(i<len(left) and j< len(right)):
        if(left[i]<right[j]):
            ls[k] = left[i]
            i += 1
        else:
            ls[k] = right[j]
            j += 1
        k += 1
    while(i<len(left)):
        ls[k] = left[i]                             ##########################
        i += 1                                      # Have write this in c++ #
        k += 1                                      ##########################
    while(j< len(right)):
        ls[k] = right[j]
        j += 1
        k += 1

def mergeSort(ls):
    if(len(ls) > 1):
        left = ls[:len(ls)//2]
        right = ls[len(ls)//2:]
        mergeSort(left)
        mergeSort(right)
        merge(left, right, ls)
ls = [3, 2, 1, 4, 5]
mergeSort(ls)
print(ls)

# # 2nd method of Implementation using recursion
# def mergeSort(ls):
#     if(len(ls) > 1):
#         left = ls[:len(ls)//2]
#         right = ls[len(ls)//2:]
#         mergeSort(left)
#         mergeSort(right)
#         i, j, k = 0, 0, 0
#         while (i< len(left) and j< len(right)):
#             if (left[i]<right[j]):
#                 ls[k] = left[i]
#                 i += 1
#             else:
#                 ls[k] = right[j]
#                 j += 1
#             k += 1
#         while(i<len(left)):
#             ls[k] = left[i]
#             k += 1
#             i += 1
#         while(j<len(right)):
#             ls[k] = right[j]
#             k += 1
#             j += 1
# ls = [3, 2, 1, 4, 5]
# mergeSort(ls)
# print(ls)

############      ROUGH      #########
# def test2(ls):
#     ls.append(6)

# def test(ls):
#     ls.append(5)
#     test2(ls)
# ls = [1, 2, 3]
# test(ls)
# print(ls)