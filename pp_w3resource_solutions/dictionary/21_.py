"""Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
"""
d ={'1':['a','b'],
    '2':['c','d']}
items = d.items()
l1 = list(items)

print(l1[0][1][0] + l1[1][1][0])
print(l1[0][1][0] + l1[1][1][1])
print(l1[0][1][1] + l1[1][1][0])
print(l1[0][1][1] + l1[1][1][1])

