# from math import sqrt


# class Solution:
#     def primeSet(self, A):
#         self.ls = [1]*(A+1)
#         self.ls[0] = 0
#         self.ls[1] = 0
#         for i in range(2, int(sqrt(A))+1):
#             self.j = i*i
#             while (self.j <= A):
#                 self.ls[self.j] = 0
#                 self.j += i
#         self.ps = []
#         for i in range(2, len(self.ls)):
#             if (self.ls[i] == 1):
#                 self.ps.append(i)
#         return self.ps

#     def primesum(self, A):
#         self.p = self.primeSet(A)
#         # print(p)
#         for i in range(len(self.p)):
#             for j in range(len(self.p)):
#                 if (self.p[i] + self.p[j] == A):
#                     return [self.p[i], self.p[j]]


# s = Solution()
# print(s.primesum(20))

########   LeetCode : https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/   #########
def rotation(arr):
    s = 0
    e = len(arr)-1
    n = len(arr)
    # ans = -1
    while (s <= e):
        mid = (s+e)//2
        if (arr[mid] <= arr[n-1]):
            e = mid - 1
        else:
            ans = mid
            s = mid+1
    try:
        return ans
    except:
        return e


def bs(ls, key, br):
    if (key <= ls[br] and key > ls[len(ls)-1]):
        s = 0
        e = br
    else:
        s = br+1
        e = len(ls)-1
    # print(s, e)
    while (s <= e):
        mid = (s+e)//2
        if (ls[mid] == key):
            return mid
        elif (ls[mid] > key):
            e = mid-1
        else:
            s = mid + 1
    return -1


ls = [1]
br = rotation(ls)
print(bs(ls, 0, br))
