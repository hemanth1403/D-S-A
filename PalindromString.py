def palindrom(s,l,r):
    if(l>=r):
        return True
    if(s[l] != s[r]):
        return False
    else:
        return palindrom(s, l+1, r-1)
    
print(palindrom("aba", 0, 2))