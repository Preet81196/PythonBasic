import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = 'https://www.python.org/'

reqs = urllib.request.urlopen(url)
soup = BeautifulSoup(reqs, 'lxml')

root = soup.html
root_childs = [all.name for all in root.children if all.name is not None]


print(root_childs)

