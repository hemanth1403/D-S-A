# Boyer-Moore Majority vote algorithm

def majority(ls):
    ansInd = 0
    count = 1
    for i in range(1, len(ls)):
        if ls[i] == ls[ansInd]:
            count += 1
        else:
            count -= 1
        if (count == 0):
            ansInd = i
            count = 1
    c = 0
    for i in range(len(ls)):
        if (ls[i] == ls[ansInd]):
            c += 1
    if (c > (len(ls)//2)):
        print(ls[ansInd])
    else:
        print("None")


ls = [2, 2, 1, 1, 1, 2, 2]
majority(ls)
