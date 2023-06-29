def stringPermu(proc, unproc):
    if (len(unproc) == 0):
        print(proc)
        return
    char = unproc[0]
    for i in range(len(proc)+1):
        front = proc[:i]
        back = proc[i:]
        stringPermu(front+char+back, unproc[1:])


def stringPermuRetList(proc, unproc, ls):
    if (len(unproc) == 0):
        # print(proc)
        ls.append(proc)
        return
    char = unproc[0]
    for i in range(len(proc)+1):
        front = proc[:i]
        back = proc[i:]
        stringPermuRetList(front+char+back, unproc[1:], ls)


l = []
stringPermuRetList("", "abc", l)
print(l)
