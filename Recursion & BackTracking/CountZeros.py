def countZero(n):
    return countZeroHelper(n, 0)
def countZeroHelper(n, c):
    if(n%10 == n):
        if(n == 0):
            return c+1
        else:
            return c
    rem = n%10
    if(rem == 0):
        return countZeroHelper(n//10, c+1)
    else:
        return countZeroHelper(n//10, c)

print(countZero(12030))