# def BS(arr, start, end, query):
#     if(start > end):
#         return -1
#     mid = (start + end)//2
#     if(arr[mid] == query):
#         return mid
#     elif(arr[mid] < query):
#         return BS(arr, mid+1, end, query)
#     else:
#         return BS(arr, start, mid-1, query)
# ls = [1, 2, 3, 4, 5]
# print(BS(ls, 0, len(ls)-1, 0))

def binarySearch(ls, s, e, key):
    if(s > e):
        return False
    mid = (s+e)//2
    if(ls[mid] == key):
        return True
    elif(ls[mid]>key):
        return binarySearch(ls, s, mid-1, key)
    else:
        return binarySearch(ls, mid+1, e, key)
n, key = map(int, input().split())
ls = list(map(int, input().split()))
if(binarySearch(ls, 0, n-1, key)):
    print("true")
else:
    print("false")