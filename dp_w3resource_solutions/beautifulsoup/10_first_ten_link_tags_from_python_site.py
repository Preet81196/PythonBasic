"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to find all the link tags and list the first ten from the webpage python.org.
"""

import requests
from bs4 import BeautifulSoup as bs4

python_site = requests.get('https://python.org').text

soup = bs4(python_site, features='lxml')

all_links = soup.find_all('a')[:10]

for each_link in all_links:
    print(each_link)
