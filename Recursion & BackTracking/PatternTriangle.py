def patternNormal(r,c):
    if(r==0):
        return 
    if(r>c):
        patternNormal(r,c+1)
        print("*", end=" ")
    else:
        patternNormal(r-1, 0)
        print()

def pattern(r,c):
    if(r==0):
        return 
    if(r>c):
        print("*", end=" ")
        pattern(r,c+1)
    else:
        print()
        pattern(r-1, 0)

patternNormal(4,0)