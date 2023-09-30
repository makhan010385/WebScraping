import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soup =BeautifulSoup(r.text,"lxml")
product=soup.find_all("a",class_= "title")
Product_name=[]
for i in product:
    name=i.text
    Product_name.append(name)

print(Product_name)
# print(data)
desc=soup.find_all("p",class_= "description")
Product_desc=[]
for i in desc:
    name=i.text
    Product_desc.append(name)

print( Product_desc)

rating=soup.find_all("p",class_= "pull-right")
Product_rating=[]
for i in rating:
    name=i.text
    Product_rating.append(name)

print(Product_rating)
df= pd.DataFrame({"Product":Product_name,"Product_Desc":Product_desc,"Product_rating":Product_rating})
print(df)