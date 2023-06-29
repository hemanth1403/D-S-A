# One method

# def subseq(s, ls, ans=""):
#     if (len(s) == 0):
#         ls.append(ans)
#         return
#     subseq(s[1:], ls, ans+s[0])
#     subseq(s[1:], ls, ans)


# ls = []
# subseq('abc', ls)
# print(ls)

# Another Method


def subseq(s, ans=""):
    if (len(s) == 0):
        l0 = []
        l0.append(ans)
        return l0
    l1 = subseq(s[1:], ans+s[0])
    l2 = subseq(s[1:], ans)
    return l1+l2


print(subseq("abc"))

# Not sure about this method
