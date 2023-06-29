
# One way

# def find(arr, target, index, ls):
#     if(index == len(arr)):
#         return ls
#     if(arr[index] == target):
#         ls.append(index)
#     return find(arr, target, index+1, ls)
# print(find([1, 2, 3, 4, 4, 5, 6], 4, 0, []))

# Other way

def find(arr, target, index):
    ls = []
    if(index == len(arr)):
        return ls
    if(arr[index] == target):
        ls.append(index)
    temp = find(arr, target, index+1)
    ls.extend(temp)
    return ls

print(find([1, 2, 3, 4, 4, 5, 6], 4, 0))