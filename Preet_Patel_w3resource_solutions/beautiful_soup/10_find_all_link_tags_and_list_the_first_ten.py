from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.python.org'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')


data = (soup.find_all('a')[0:10])
print(data)