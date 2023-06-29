ls = [1, 2, 3]
subsets = [[]]
for i in range(len(ls)+1):
    for j in range(i):
        subsets.append(ls[j:i])
print(subsets)
