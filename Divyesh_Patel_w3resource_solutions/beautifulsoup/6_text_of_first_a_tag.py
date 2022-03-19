"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to find the text of the first <a> tag of a given html text.
"""

from sample_htmls import sample_html
from bs4 import BeautifulSoup as bs4


soup = bs4(sample_html, features='lxml')
first_a = soup.find('a')

print('<a> text:', first_a.text)
