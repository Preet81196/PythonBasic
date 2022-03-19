"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to a list of all the h1, h2, h3 tags from the webpage python.org.
"""

import requests
from bs4 import BeautifulSoup as bs4

python_code = requests.get('https://python.org').text.strip()

soup = bs4(python_code, features='lxml')

header_tags = soup.find_all(['h1', 'h2', 'h3'])

for each in header_tags:
    print(each.name, each.text.strip())
