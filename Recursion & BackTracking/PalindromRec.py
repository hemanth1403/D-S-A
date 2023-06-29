import math

def helper(n, digits):
    if(n%10 == n):
        return n
    return (n%10)*math.pow(10, digits-1) + helper(n//10, digits - 1)

def rev(n):
    digits = int(math.log10(n)) + 1
    return int(helper(n, digits))

def palindrom(n):
    if(n == rev(n)):
        print("palindrom")
    else:
        print("Not a plaindrom")

palindrom(1234321)