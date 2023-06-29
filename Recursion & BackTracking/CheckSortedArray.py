def check(ls, index):
    if(index == len(ls)-1):
        return True
    if(ls[index] < ls[index+1]):
        return check(ls, index+1)
    else:
        return False

print(check([1, 2, 3, 4], 0))    