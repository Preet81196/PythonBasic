"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to retrieve children of the html tag from a given web page.
"""

import requests
from bs4 import BeautifulSoup as bs4

python_site_code = requests.get('https://python.org').text.strip()

soup = bs4(python_site_code, features='lxml')

root_html_tag = soup.find('html')  # soup.html
print([each.name for each in root_html_tag.children if each.name is not None])
