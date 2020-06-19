t1 = (("a","b"),(1,2))
print(t1)
print(type(t1))
print()   # for space in output
dict1 = dict((x,y)for x,y in t1)
print(dict1)
print(type(dict1))


# 2nd convert into dictionary

t2 = ('preet', 1), ('divlo', 2), ('sagar',3)
print(dict([('preet', 1), ('divlo', 2), ('sagar',3)]))
