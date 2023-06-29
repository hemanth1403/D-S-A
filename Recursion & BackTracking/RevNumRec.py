import math
# One Way of Reversing the number USING GLOBAL VARIABLE

# rev = 0
# def NumRev(n):
#     if(n == 0):
#         return
#     global rev
#     rev = rev* 10 + n%10
#     NumRev(n//10)
# NumRev(1234)
# print(rev)

# OtherWay using helper function

def helper(n, digits):
    if(n%10 == n):
        return n
    return (n%10)*math.pow(10, digits-1)+helper(n//10, digits-1)

def rev(n):
    digits = int(math.log10(n)) + 1
    return int(helper(n, digits))

print(rev(1234))