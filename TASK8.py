import os
import json
from bs4 import BeautifulSoup
import requests
from TASK1 import scrapped
from TASK4 import scrapped_movie_details

def scrapped_new_movie_details(URL):
  for i in scrapped:
    if i["Movie URL"]==URL:               
      Url=i["Movie URL"][33:]
      NAME=i['Movie Name']

      file=os.path.exists("/home/sakshi/Desktop/Web_Scrabing/"+ Url +".json") 
      if file==True:
        with open(file,"r") as f:
          var=json.load(f)

      else:
        print("file doesnt exits")
        data=scrapped_movie_details(i["Movie URL"],NAME)  

        with open ("movie_details8.json","w") as s:
          json.dump(data,s,indent=4)

        return data
URL1=scrapped[1]['Movie URL']
scrapped_new_movie_details(URL1)