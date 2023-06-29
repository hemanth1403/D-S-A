# Given a integer N, find the number of positive integers X such that X<=N and N+X = N^X (N xor X).

# Input Format

# First line of input contains T - number of test cases. Its followed by T lines, each line contains a single integer N.

# Constrains
# 1 <= T <= 10^4
# 0 <= N <= 10^18

# input
# 2
# 5
# 10

# output
# 1
# 3

for _ in range(int(input())):
    n = int(input())
    # c = 0
    # for i in range(n+1):
    #     if(i+n == i^n):
    #         c += 1
    # print(c-1)
    c = 0
    while (n > 0):
        # print(n)
        if (n & 1 == 0):
            c += 1
        n = n >> 1
    print(2**c - 1)
