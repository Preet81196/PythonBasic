"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to print the names of all HTML tags of a given web page
            going through the document tree
"""

import requests
from bs4 import BeautifulSoup as bs4

python_site_code = requests.get('https://python.org').text.strip()

soup = bs4(python_site_code, features='lxml')

for each in soup.find_all():
    print(each.name)
