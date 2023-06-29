def skipChar(s,i,res=""):
    if(i == len(s)):
        return res
    if(s[i] != "a"):
        res += s[i]
        return skipChar(s, i+1, res)
    else:
        return skipChar(s, i+1, res)
print(skipChar("ababab", 0))