"""sample all in one"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

url = "https://docs.python.org/3/index.html"

uClient = uReq(url)
page_html = uClient.read()
uClient.close()

soup = soup(page_html, 'html.parser')

#find paragraph tag
print("All paragraph tags:")
print(soup.find_all("p"))

#find number of paragraph tags
print("Number of all paragraph tags:")
print(len(soup.find_all("p")))


#extract text from paragraph
print("The text in the first paragraph tag:")
print(soup.find_all('p')[0].text)

print("Length of the text of the first <h2> tag:")
print(len(soup.find('h2').text))
