"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to get the top three items in a shop.
"""

# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

adict = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

alist = sorted(adict.items(), key=lambda pair: pair[1], reverse=True)[:3]

for each_tuple in alist:
    print(each_tuple[0], each_tuple[1])
