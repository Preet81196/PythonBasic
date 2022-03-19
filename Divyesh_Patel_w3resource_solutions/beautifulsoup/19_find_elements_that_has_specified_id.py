"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 04/06/20
* @decription: Write a Python program to print the element(s) that has a specified id of a given web page.
"""

import requests
from bs4 import BeautifulSoup as bs4

python_site = requests.get('https://python.org').text

soup = bs4(python_site, features='lxml')

print(soup.select_one('#python-network'))
