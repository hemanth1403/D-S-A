def helper(a ,b, result):
    if(b <= 1):
        return result
    if((b&1) == 0):
        result = result*(a*a)
        return helper(a, b>>1, result)
    else:
        result = result*(a)
        return helper(a, b-1, result)

def fastPowers(a, b):
    return helper(a, b, 1)
# Time Complexity -> O(log b)
print(fastPowers(3, 5))