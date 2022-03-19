"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 02/06/20
* @decription: Write a Python program to extract the text in the first paragraph tag of a given html document.
"""

from sample_htmls import sample_html
from bs4 import BeautifulSoup as bs4


soup = bs4(sample_html, features='lxml')
first_para = soup.find('p')

print('The Text of first para...')
print(first_para.text)
