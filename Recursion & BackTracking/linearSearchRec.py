def linearSearch(arr, target, index):
    if(index == len(arr)):
        return False
    return arr[index] == target or linearSearch(arr, target, index+1)

print(linearSearch([1, 2, 4, 18, 9], 18, 0))