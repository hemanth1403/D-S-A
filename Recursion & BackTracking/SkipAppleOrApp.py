def skipApla(s, ind, skip, res=""):
    if(ind == len(s)):
        return res
    if(skip in s):
        if(ind == s.index(skip)):
            for i in range(ind, len(s)):
                if(s[i]==skip[-1]):
                    break
            return skipApla(s, i+1, skip, res)
        else:
            res += s[ind]
            return skipApla(s, ind+1, skip, res)
    else:
        skip = "app"
        if(ind == s.index(skip)):
            # for i in range(ind, len(s)):
            #     if(s[i]==skip[-1]):
            #         break
            print(s.index(skip))
            skip="apple"
            print()
            return skipApla(s, ind+3, skip, res)
        else:
            res += s[ind]
            skip="app"
            return skipApla(s, ind+1, skip, res)
        

print(skipApla("bbbcaaaacccappleapplezzapp", 0, 'apple'))
