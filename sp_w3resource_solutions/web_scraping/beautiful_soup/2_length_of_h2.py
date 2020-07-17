"""Write a Python program to find the length of the text of the first <h2> tag of a given html document."""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

url = "https://www.tutorialspoint.com/index.htm"

uClient = uReq(url)
page_html = uClient.read()
uClient.close()

soup = soup(page_html, 'html.parser')
print("Length of the text of the first <h2> tag:")
print(len(soup.find('h2').text))