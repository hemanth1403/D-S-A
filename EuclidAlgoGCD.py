def EuclidGCD(a,b):
    if(b == 0): return a
    # print(a, b)
    # print(a%b)
    return EuclidGCD(b, a%b)

print(EuclidGCD(24, 60))