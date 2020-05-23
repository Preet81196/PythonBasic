"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 20/05/20
* @decription: Write a Python program to get the current username
"""

import os
print('username:', os.environ['USER'])  # Another way, getpass.getuser() (from getpass built-in package)
