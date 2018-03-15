# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 23:00:35 2018

@author: prem
"""

from requests import get
from bs4 import BeautifulSoup

url = "https://www.naukri.com/data-analyst-jobs-in-chennai"
response =  get(url)
soup = BeautifulSoup(response.text,"html.parser")
type(soup)

soup
container1 = soup.find_all("div", {"itemtype":"http://schema.org/JobPosting"})
len(container1)
print(container1)

design = item.find(class_ = "desig").get_text()
print (design)
