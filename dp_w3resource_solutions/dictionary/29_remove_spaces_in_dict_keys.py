"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to remove spaces from dictionary keys.
"""

# Sample data: {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# Output: {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}

adict = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

curated_adict = {key.replace(' ', ''): value for key, value in adict.items()}

print(curated_adict)
