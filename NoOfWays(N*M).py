def ways(sn, sm, en, em):
    if(sn == en or sm == em):
        return 1
    return ways(sn+1, sm, en, em) + ways(sn, sm+1, en, em)

print(ways(1, 1, 3, 3))