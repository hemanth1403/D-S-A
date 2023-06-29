def gcd(m,n):
    while(n>0):
        r = m
        m = n
        n = r%n
    return m
print(gcd(60,24))