
# One method
# def subSeq(s, i, ans=""):
#     if (i == len(s)):
#         if (len(ans) > 0):
#             print(ans)
#             return
#         else:
#             return
#     subSeq(s, i+1, ans+s[i])
#     subSeq(s, i+1, ans)


# subSeq("abc", 0)


# Another method


def subSeq(s, res):
    if (len(s) == 0):
        print(res)
        return
    subSeq(s[1:], res+s[0])
    subSeq(s[1:], res)


subSeq("abc", "")
