t1 = (("preet",11),("sagar",12),("divlo",13))
dict1 = dict((i,j) for i,j in t1)
print(dict1)

print()

dict2 = {}
for i, j in t1:
    dict2.setdefault(i, []).append(j)
print(dict2)

