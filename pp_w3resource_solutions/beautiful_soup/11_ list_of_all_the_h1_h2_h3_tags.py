from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.python.org'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')


for tag in soup.find_all(['h1' ,'h2','h3']):
    print(tag.name + '-->' + tag.text.strip())