import json
from TASK5 import all_movies

def analyse_movies_directors(movies_detail_list):
    dict1={}          
    for i in movies_detail_list: 
       count=0              
       for j in movies_detail_list:              
          if i["Director:"]==j["Director:"]:
             count=count+1              
       dict1.update({i["Director:"]:count})

    with open ("analyse_director7.json","w") as s:
         json.dump(dict1,s,indent=4) 
    return dict1            
analyse_movies_directors(all_movies)