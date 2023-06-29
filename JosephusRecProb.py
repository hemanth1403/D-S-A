def josephSolution(n, k):
    if(n == 1):
        return 0
    return (josephSolution(n-1, k)+k)%n

print(josephSolution(5, 3))