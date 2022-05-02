from TASK1 import scrapped
from TASK4 import scrapped_movie_details
import json

def get_movie_list_details(movies_list):
    list1=[]
    for j in movies_list:
        list1.append(j)                                       
        if j["Movie Rank"]=="50.":
            break 

    link_url={}
    for k in list1:
        link_url.update({k['Movie URL']:k['Movie Name']}) 

    list2=[]  
    for a,b in link_url.items():                
        u=scrapped_movie_details(a,b) 
        list2.append(u)    

    with open("url_details5.json","w") as file:
        json.dump(list2,file,indent=4)
    return list2
all_movies=get_movie_list_details(scrapped)  