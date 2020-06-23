from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error

url = 'https://www.python.org/'

reqs = urllib.request.urlopen(url).read()

soup = BeautifulSoup(reqs,'lxml')

print(soup.title)
print(soup.title.text)
print(soup.title.parent)

