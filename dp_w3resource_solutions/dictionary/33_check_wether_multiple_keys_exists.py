"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 06/06/20
* @decription: Write a Python program to check multiple keys exists in a dictionary.
"""

student = {'name': 'Alex', 'class': 'V', 'roll_id': '2'}

print(student.keys() >= {'name', 'roll_id'})
print(student.keys() >= {'class', 'roll_id'})
print(student.keys() >= {'name', 'patel'})
