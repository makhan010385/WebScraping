# import requests
# from bs4 import BeautifulSoup
# # Making a GET request
# r = requests.get('https://www.dauniv.ac.in/new/sfsp/')
# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
#  # Getting the title tag
# print(soup.title)
#  # Getting the name of the tag
# print(soup.title.name)
# # Getting the name of parent tag
# print(soup.title.parent.name)
# # use the child attribute to get
# # the name of the child tag




# ----------------------------------------------------------

import requests
from bs4 import BeautifulSoup
 
# Making a GET request
r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'lxml')
 
s = soup.find('div', class_='entry-content')
content = s.find_all('p')
 
print(content)