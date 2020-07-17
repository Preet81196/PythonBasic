from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

url = "https://www.flipkart.com/search?q=poco&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "bhgxx2 col-12-12"})
length = len(containers)
print("total numbers of devices:",length)

print(soup.prettify(containers[0]))

container = containers[0]
name = container.div.img["alt"]
print("Name of first device:",name)

price = page_soup.findAll("div", {"class": "_2mPS7z"})
print("price :",price[0].text)

filename ="poco.csv"
f = open(filename,"w")

headers = "Product_Name,pricing\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class": "_2mPS7z"})
    price = price_container[0].text.strip()

    print(product_name)
    print(price)

    