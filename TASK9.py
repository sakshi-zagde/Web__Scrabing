import json
import os
import random
import time
from TASK4 import scrapped_movie_details
from TASK1 import scrapped

def  movie_list():             
    for i in range(10):  
        ab=scrapped[i]['Movie URL']                     
        Url=scrapped[i]["Movie URL"][33:]
        NAME=scrapped[i]['Movie Name']
        uRL="/home/sakshi/Desktop/Web_Scrabing/"+ Url +".json"
        file=os.path.exists(uRL) 
        if file==True:
           with open(file,"r") as f:
              var=json.load(f)
        else:
           print("file doesnt exits")
           data=scrapped_movie_details(ab,NAME)
           r=random.randint(1,3) 
           time.sleep(r)
           with open (uRL,"a") as s:
               json.dump(data,s,indent=4)
movie_list()   