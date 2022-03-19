"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to get the number of paragraph tags of a given html document.
"""

from sample_htmls import sample_html
from bs4 import BeautifulSoup as bs4

soup = bs4(sample_html, features='lxml')
total_p = soup.find_all('p')

print('total p tags:', len(total_p))
