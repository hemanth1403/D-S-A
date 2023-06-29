def trailingZeros(n):
    zeros = 0
    i = 5
    while(i<=n):
        zeros = zeros + (n//i)
        i *= 5
    return zeros
# Trailing Zeros of 20! 
print(trailingZeros(20))