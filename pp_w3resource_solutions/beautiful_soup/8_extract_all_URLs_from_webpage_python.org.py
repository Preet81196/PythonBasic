from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.python.org'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')

data = (soup.find_all('li'))

for h in data:
    a = h.find('a')
    print(a['href'])