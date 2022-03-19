"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to find the length of the text of the first <h2> tag of a given html document.
"""

from sample_htmls import sample_html
from bs4 import BeautifulSoup as bs4


soup = bs4(sample_html, features='lxml')
first_h2 = soup.find('h2')

print('length of text of first h2:', len(first_h2.text))
