# def isSafe(grid, r, c, n):
#     d1, d2 = r, c
#     while (d1 > 0 and d2 > 0):
#         if (grid[d1-1][d2-1] == 1):
#             return False
#         d1 = d1-1
#         d2 = d2-1
#     d3, d4 = r, c
#     while (d3 < n-1 and d4 < n-1):
#         if (grid[d3+1][d4+1] == 1):
#             return False
#         d3 += 1
#         d4 += 1
#     d5, d6 = r, c
#     while (d5 > 0 and d6 < n-1):
#         if (grid[d5-1][d6+1] == 1):
#             return False
#         d5 -= 1
#         d6 += 1
#     d7, d8 = r, c
#     while (d7 < n-1 and d8 > 0):
#         if (grid[d7+1][d8-1] == 1):
#             return False
#         d7 += 1
#         d8 -= 1
#     for i in range(n):
#         if (i != r):
#             if (grid[i][c] == 1):
#                 return False
#     return True


# def NQueens(grid, r):
#     if r == len(grid):
#         return True
#     for c in range(len(grid[0])):
#         if (isSafe(grid, r, c, len(grid))):
#             grid[r][c] = 1
#             if NQueens(grid, r+1):
#                 return True
#             grid[r][c] = 0
#     return False


# q = int(input("No of Queens : "))
# n = int(input("Size of Grid : "))
# grid = [[0 for _ in range(n)] for _ in range(n)]
# print(NQueens(grid, 0))
# print(grid)

class Solution:
    def isSafe(self, grid, r, c, n):
        self.d1, self.d2 = r, c
        while (self.d1 > 0 and self.d2 > 0):
            if (grid[self.d1-1][self.d2-1] == 1):
                return False
            self.d1 = self.d1-1
            self.d2 = self.d2-1
        self.d3, self.d4 = r, c
        while (self.d3 < n-1 and self.d4 < n-1):
            if (grid[self.d3+1][self.d4+1] == 1):
                return False
            self.d3 += 1
            self.d4 += 1
        self.d5, self.d6 = r, c
        while (self.d5 > 0 and self.d6 < n-1):
            if (grid[self.d5-1][self.d6+1] == 1):
                return False
            self.d5 -= 1
            self.d6 += 1
        self.d7, self.d8 = r, c
        while (self.d7 < n-1 and self.d8 > 0):
            if (grid[self.d7+1][self.d8-1] == 1):
                return False
            self.d7 += 1
            self.d8 -= 1
        for i in range(n):
            if (i != r):
                if (grid[i][c] == 1):
                    return False
        return True

    def Solver(self, grid, n):
        if (n == len(grid)):
            return True
        for i in range(len(grid[0])):
            if (self.isSafe(grid, n, i, len(grid))):
                grid[n][i] = 1
                if (self.Solver(grid, n+1)):
                    return True
                grid[n][i] = 0
        return False

    def NQueens(self, n):
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.val = self.Solver(self.grid, 0)
        print(self.grid)


queens = Solution()
queens.NQueens(4)
