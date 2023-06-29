def prodSumRec(n):
    if(n<=0):return 1
    return (n%10)*prodSumRec(n//10)
print(prodSumRec(12034))