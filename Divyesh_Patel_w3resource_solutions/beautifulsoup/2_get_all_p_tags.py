"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to retrieve all the paragraph tags from a given html document.
"""

from sample_htmls import sample_html
from bs4 import BeautifulSoup as bs4

soup = bs4(sample_html, features='lxml')

all_p_tags = soup.find_all('p')
for each in all_p_tags:
    print('>', each.text.strip())
