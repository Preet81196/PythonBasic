t1 = (1,2,3)
t2 = t1 + (4,)
""" we can't add value in tuple 
so here is the trick for adding
items in tuple"""
print(t2)
#2nd method add items in tuple using list
list1 = list(t1)
list1.append(5)
t1 = tuple(list1)
print(t1)