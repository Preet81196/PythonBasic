"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to print content of elements that contain a specified string of a given web page.
"""

import requests
from bs4 import BeautifulSoup as bs4

python_site_code = requests.get('https://python.org').text.strip()

soup = bs4(python_site_code, features='lxml')

for each in soup.get_text():
    if 'Python' in each:
        print(each)
