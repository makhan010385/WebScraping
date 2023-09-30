import requests
from bs4 import BeautifulSoup
import re
url ="https://www.dauniv.ac.in/new/sfsp/"
r=requests.get(url)
soup =BeautifulSoup(r.text,"lxml")
data=soup.find_all(string= re.compile("M.Tech."))
print(data)
print(len(data))