"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to get the key, value and item in a dictionary.
"""

# Sample data: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key  value  count
# 1     10      1
# 2     20      2
# 3     30      3
# 4     40      4
# 5     50      5
# 6     60      6

counter = 1
adict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print('key', 'value', 'count')

for key in adict:
    print(key, '\t', adict[key], '\t', counter)
    counter += 1
