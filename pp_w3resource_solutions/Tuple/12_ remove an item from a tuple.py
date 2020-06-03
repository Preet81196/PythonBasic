t1 = (1,2,3,4,5,6)

t1 = t1[:2] + t1[4:]
print(t1)


# 2nd method
l1 = list(t1)
l1.remove(6)

t1 = tuple(l1)
print(t1)
