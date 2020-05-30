"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 20/05/20
* @decription: Write a Python program to locate Python site-packages.
"""

from distutils.sysconfig import get_python_lib

print("Site Packages:", get_python_lib())
