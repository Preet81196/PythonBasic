from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.python.org'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')

lst = list()
data = (soup.find_all('h2')[0:4])
print(data)


