import requests
from bs4 import BeautifulSoup
url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soup =BeautifulSoup(r.text,"lxml")
Desc =soup.find_all("p",class_="description")
# print(Desc[2])
for i in Desc:
    print(i.text)
 