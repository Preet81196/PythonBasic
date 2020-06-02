"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to retrieve all descendants of the body tag from a given web page.
"""

from sample_htmls import sample_html
from bs4 import BeautifulSoup as bs4


soup = bs4(sample_html, features='lxml')

body_tag = soup.html.body

print([each.name for each in body_tag.descendants if each.name is not None])
