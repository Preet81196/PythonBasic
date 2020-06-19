dict1 = {"preet":100,"sagar":200,"divlo":300}
dict2 = {"preet":100,"sagar":200,"divlo":300}

for i in dict2:
    if i in dict1:
        dict2[i] = dict2[i] + dict1[i]
print(dict2)

#2nd method
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)

