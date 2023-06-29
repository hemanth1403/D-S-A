for _ in range(int(input())):
    n, k = map(int, input().split())

    ls = list(map(int, input().split()))
    dequ = []
    ans = []
    for i in range(0, k):
        if (len(dequ) == 0):
            dequ.append(ls[i])
        else:
            while (len(dequ) > 0):
                ele = dequ[-1]
                if (ele < ls[i]):
                    dequ.pop()
                    dequ.append(ls[i])
                    beak
                else:
                    dequ.append(ls[i])
                    break
        ans.append(dequ[0])
    print(ans)
    # for i in range(n-k+1):
    #     temp = ls[i:i+k]
    #     for j in temp:
    #         if(len(dequ[0]) == 0):
    #             dequ.append(j)
    #         else:

    #     if (len(dequ) > 0):
    #         if (dequ[0] == ls[i-1]):
    #             del dequ[0]
    #     for j in temp:
    #         if len(dequ) == 0:
    #             dequ.append(j)
    #         else:
    #             while (len(dequ) > 0):
    #                 ele = dequ[-1]
    #                 if (ele < j):
    #                     dequ.pop()
    #                     dequ.append(j)
    #                 else:
    #                     dequ.append(j)
    #                     break
    #     ans.append(dequ[0])
    # print(ans)
