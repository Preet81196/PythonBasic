"""Write a Python program to find the text of the first <a> tag of a given html text"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

url = "https://www.tutorialspoint.com/index.htm"

uClient =  uReq(url)
page_html = uClient.read()
uClient.close()

soup = soup(page_html, 'html.parser')
print("Length of the text of the first <a> tag:")
print(soup.find('a').text)



