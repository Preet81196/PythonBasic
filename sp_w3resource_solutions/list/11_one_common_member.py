"""  Write a Python function that takes two lists and returns True if they have at least one common member"""
list1 = [8,5,2]
list2 = [9,1,14]
res = False
for each in list1:
    for all in list2:
        if each == all:
            res = True
print(res)
