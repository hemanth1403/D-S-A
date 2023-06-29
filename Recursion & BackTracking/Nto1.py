def fun(n):
    if(n == 0): return 
    print(n)
    fun(n-1)
    # print(n)

def funRev(n):
    if(n == 0): return
    fun(n-1)
    print(n)

def funBoth(n):
    if(n==0): return
    print(n) 
    funBoth(n-1)
    print(n)

# fun(5)
# print("******")
# funRev(5)
funBoth(5)