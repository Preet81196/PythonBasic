"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 06/06/20
* @decription: Write a Python program to sort Counter by value.
"""

# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

adict = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

result = sorted(adict.items(), key=lambda pair: pair[1], reverse=True)

print(result)
