"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to retrieve the HTML code of the title, its text, and the HTML code of its parent
"""

from sample_htmls import sample_html
from bs4 import BeautifulSoup as bs4

soup = bs4(sample_html, features='lxml')

print('title:', soup.html.title)
print('title text:', soup.html.title.text)
print('title parent:', soup.html.title.parent)
