#1
"""
test = "gogle.com"
dict = {}
for n in test:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
print(dict)"""

#2 
"""
from collections import Counter                        #using import method
test = "preetpatel"
result = Counter(test)
print("characters in preetpatel :\n",result)"""

#3
test = "preetpatel"
result = {}                                 #using dr.chuck
for keys in test:
    result[keys] = result.get(keys,0) + 1           # using dict.get() to get count 
print("characters in preetpatel :\n",result)