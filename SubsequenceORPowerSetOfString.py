def powerSet(s, i, res =""):
    if(i == len(s)):
        print(res)
        return 
    powerSet(s, i+1, res+s[i])
    powerSet(s, i+1, res)

powerSet("abc", 0)