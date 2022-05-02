import requests
from bs4 import BeautifulSoup
import json
from TASK1 import scrapped
def scrape_movie_cast(api):
    list1=[]                   
    req=requests.get(api)
    soup=BeautifulSoup(req.text,"html.parser")
    table=soup.find("div",class_="castSection")
    tr=table.find_all("div",class_="cast-item media inlineBlock")
    for i in tr[1:]:               
        url=i.find("a",class_="unstyled articleLink") 
        link1=url.get_text()
        link=url["href"]
        crew_link="https://www.rottentomatoes.com"+link
        name=i.find("span")
        Name=name.get_text().strip()
        dict1={}
        dict1["url"]=crew_link
        dict1["name"]=Name

        list1.append(dict1)
    with open("movie_cast12.json","w") as file:
            json.dump(list1,file,indent=4)
    return list1         
api=scrapped[0]['Movie URL']                 
scrape_movie_cast(api)