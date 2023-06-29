# There is a full day farewell party at your college. A number of guests will arrive at the party during their preferred time slots. You have to analyse the guest list and report the minimum capacity room required to host the event successfully.

# Input Format

# First line of input contains T - number of test cases. The first line of each test case contains N - number of guests. Its followed by N lines each containing 2 integers - A(the arrival time) and D(the departure time) of the guest in seconds

# constrains
# 1 <= T <= 100
# 1 <= N <= 10000
# 1 <= A[i] <= D[i] <= 86400

# Output Format

# For each test case, print the the minimum capacity room required to accomodate all the guests, separated by newline.

# Sample Input
# 3
# 3
# 1 5
# 5 10
# 15 20
# 7
# 30 50
# 1 70
# 20 25
# 50 100
# 80 90
# 15 65
# 25 70
# 4
# 16 58
# 4 16
# 12 71
# 57 72

# Sample OutPut
# 2
# 5
# 3

arr = [0 for i in range(86402)]
for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        arr[a] += 1
        arr[b+1] += -1
    for i in range(1, 86402):
        arr[i] += arr[i-1]
    print(max(arr))
    for i in range(1, 86401):
        arr[i] = 0
