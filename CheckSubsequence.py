# Given 2 strings A and B, check if A is present as a subsequence in B.

# Input Format

# First line of input contains T - number of test cases. Its followed by T lines, each line contains 2 space separated strings - A and B.

# Constraints

# 1 <= T <= 1000
# 1 <= len(A), len(B) <= 1000
# 'a' <= A[i],B[i] <= 'z'

# Output Format

# For each test case, print "Yes" if A is a subsequence of B, "No" otherwise, separated by new line.

# input
# 2
# data gojdaoncptdhzay
# algo plabhagqogxt

# output
# Yes
# No

for _ in range(int(input())):
    a, b = map(str, input().split())
    i = 0
    j = 0
    while (i < len(a) and j < len(b)):
        if (a[i] == b[j]):
            i += 1
            j += 1
        else:
            j += 1
    if (j == len(b) and i != len(a)):
        print("No")
    else:
        print("Yes")
