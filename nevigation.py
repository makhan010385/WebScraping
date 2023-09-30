import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
url ="https://www.dauniv.ac.in/new/sfsp/"
r=requests.get(url)
soup =BeautifulSoup(r.text,"lxml")
product=soup.find("div",class_= "column").text
# print(len(product))
# name =product.find("a").text
print(product)