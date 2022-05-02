import requests
from bs4 import BeautifulSoup
import json
from TASK1 import scrapped

def scrapped_movie_details(url_1,name):
   adventure_url=url_1                          
   adventure_api=requests.get(adventure_url)
   soup = BeautifulSoup(adventure_api.text,"html.parser")
   table_tag = soup.find('ul',class_="content-meta info")
   li=table_tag.find_all("li",class_="meta-row clearfix")
   movie_dict={}  
   for i in li:
      dic1=i.find("div",class_="meta-label subtle").text.strip() 
      dic2=i.find("div",class_="meta-value").text.replace(" ","").replace("\n","").strip()              
      movie_dict[dic1]=dic2 
      movie_dict["name"]=name
   with open ("director_4.json","w") as s:
      json.dump(movie_dict,s,indent=4)
   return movie_dict

for j in scrapped:
   url_1=scrapped[0]['Movie URL']   
   name_1=scrapped[0]['Movie Name']              
scrapped_movie_details(url_1,name_1)