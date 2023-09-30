import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soup =BeautifulSoup(r.text,"lxml")
product=soup.find_all("div",class_= "col-sm-4 col-lg-4 col-md-4")[3]
# print(len(product))
name =product.find("a").text
# desc=product.find("p",class_="description").text
print(name)
# print(product)
