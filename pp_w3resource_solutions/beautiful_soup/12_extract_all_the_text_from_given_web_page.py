import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = urllib.request.urlopen(url).read()
soup = BeautifulSoup(reqs, 'lxml')
print("Text from the said page:")
print(soup.get_text())

