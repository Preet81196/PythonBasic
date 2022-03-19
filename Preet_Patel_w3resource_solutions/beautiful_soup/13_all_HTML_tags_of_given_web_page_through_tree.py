from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error

url = 'https://www.python.org'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')

for each in soup.find_all():
    print(each.name)
