from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error

url = 'https://www.python.org/'

reqs = urllib.request.urlopen(url).read()

soup = BeautifulSoup(reqs,'lxml')

tag = soup.find_all('li')

print(tag)
