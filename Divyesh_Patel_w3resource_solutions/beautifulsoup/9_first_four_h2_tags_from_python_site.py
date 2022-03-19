"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to find all the h2 tags and list the first four from the webpage python.org
"""

import urllib.request
from bs4 import BeautifulSoup as bs4

with urllib.request.urlopen('https://python.org') as handle:
    python_site = handle.read().decode()

soup = bs4(python_site, features='lxml')

all_links = soup.find_all('h2')[:4]

for each_link in all_links:
    print(each_link)
