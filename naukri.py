from requests import get
from bs4 import BeautifulSoup

url = "https://www.naukri.com/data-analyst-jobs-in-chennai"
response =  get(url)
soup = BeautifulSoup(response.text,"html.parser")
type(soup)

container1 = soup.find_all("div", {"itemtype":"http://schema.org/JobPosting"})
len(container1)
print(container1)

first_cont = container1[0]
first_cont

first_title = first_cont.find("li",class_ = "desig").get_text()
print (first_title)

firt_organisation = first_cont.find("span", class_ = "org").get_text()
print(firt_organisation)

first_exp = first_cont.find("span", class_ = "exp").get_text()
print(first_exp)

first_loc = first_cont.find("span", class_ = "loc").get_text()
print(first_loc)

first_keyskills = first_cont.find("span", class_ = "skill").get_text()
print(first_keyskills)

first_postdate = first_cont.find("span", class_ = "date").get_text()
print(first_postdate)

# Lists to store the scraped data in
title = []
organisation =[]
experience =[]
location = []
keyskills =[]
posted_date =[]

#loop to get all the data
for container in container1:
    title1 = container.find("li",class_ = "desig").get_text()
    title.append(title1)
    
    org = container.find("span", class_ = "org").get_text()
    organisation.append(org)
    
    exp = container.find("span", class_ = "exp").get_text()
    experience.append(exp)
    
    loc = container.find("span", class_ = "loc").get_text()
    location.append(loc)
    
    skills = container.find("span", class_ = "skill").get_text()
    keyskills.append(skills)
    
    date = container.find("span", class_ = "date").get_text()
    posted_date.append(date)
    
import pandas as pd
alldata = pd.DataFrame({"title" : title,
                        "organisation" : organisation,
                        "experience" : experience,
                        "location" : location,
                        "keyskills" : keyskills,
                        "posted_date" : posted_date})

newdata = alldata[["title","organisation","experience","location","keyskills","posted_date"]]

newdata.to_csv("naukri_scrapped.csv",index = False)
