"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to extract all the URLs from the webpage python.org
            that are nested within <li> tags from.
"""

import urllib.request
from bs4 import BeautifulSoup as bs4

with urllib.request.urlopen('https://python.org') as handle:
    python_site = handle.read().decode()

soup = bs4(python_site, features='lxml')

all_links = soup.find_all('a')

for each_link in all_links:
    if each_link.parent.name == 'li':
        print(each_link['href'])
