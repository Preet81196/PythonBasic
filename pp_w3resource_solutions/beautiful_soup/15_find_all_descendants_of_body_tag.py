from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error

url = 'https://www.python.org/'

reqs = urllib.request.urlopen(url).read()

soup = BeautifulSoup(reqs,'lxml')
root = soup.html

body = [each.name for each in root.descendants if each.name is not None]

print(body)