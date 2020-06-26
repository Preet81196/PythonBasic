from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import re

url = 'https://www.python.org/'

reqs = urllib.request.urlopen(url).read()

soup = BeautifulSoup(reqs,'lxml')

print(soup.select_one('#python-network'))