def skipApla(s, ind, skip, res=""):
    if(ind == len(s)):
        return res
    # if()
    if(ind == s.index(skip)):
        for i in range(ind, len(s)):
            if(s[i]==skip[-1]):
                break
        return skipApla(s, i+1, skip, res)
    else:
        res += s[ind]
        return skipApla(s, ind+1, skip, res)

print(skipApla("bbbcaaaacccapplezzz", 0, 'apple'))

# s = "helloaaaapple"
# print(s.index("apple"))