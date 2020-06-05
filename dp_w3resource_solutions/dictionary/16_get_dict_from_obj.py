"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to get a dictionary from an object's fields.
"""


class Employee:
    def __init__(self):
        self.name = 'Divyesh'
        self.email = 'email@example.com'
        self.salary = 1000

    def class_meth(self):
        pass


newobj = Employee()
print(newobj.__dict__)

