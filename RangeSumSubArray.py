# Given an array of integers and a range [A,B], you have to find the number of subarrays whose sum lies in the given range inclusive.

# Input Format

# First line of input contains T - number of test cases. Its followed by 2T lines, the first line of each test case contains N, A, B - size of the array and the range separated by space, the second line contains the elements of the array.

# Constrains
# 1 <= T <= 100
# 1 <= N <= 1000
# -10^7 <= A <= B <= 10^7
# -10^4 <= ar[i] <= 10^4

# input
# 4
# 3 -10 5
# -5 10 -3
# 4 -10000 1000
# 929 -4041 -2470 -6445
# 9 -36116 6820
# 4605 -626 -3454 -2532 -91 3010 -3557 5552 4055
# 6 392 5416
# -4905 -2388 5352 -3231 4902 -7485

# output
# 4
# 8
# 41
# 6

# explanation
# Test Case 1:
# The subarrays are:
# -5 [Sum = -5]
# -5 10 [Sum = 5]
# -5 10 -3 [Sum = 2]
# 10 [Sum = 10]
# 10 -3 [Sum = 7]
# -3 [Sum = -3]
# Hence, there are 4 subarrays whose sum lie in the range [-10,5]

# //////////////////////////////////
# the Below Solutions is a brut Force approach
# /////////////////////////////////

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    ls = list(map(int, input().split()))
    c = 0
    for i in range(n):
        # print(ls[i])
        temp = ls[i]
        if (ls[i] in range(a, b+1)):
            # print(ls[i])
            c += 1
        # else:
        for j in range(i+1, n):
            # print(temp,ls[j])
            temp += ls[j]
            if (temp in range(a, b+1)):
                c += 1
    print(c)
