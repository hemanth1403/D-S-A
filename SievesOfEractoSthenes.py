from math import sqrt

def sievesOfEractoSthenes(n):
    ls = [1]*(n+1)
    ls[0] = 0
    ls[1] = 0
    for i in range(2,int(sqrt(n)+1)):
        j = i*2
        while(j<=n):
            ls[j] = 0
            j += i
    return ls
# Return the prime numbers from the range 1 to 12
print(sievesOfEractoSthenes(12))