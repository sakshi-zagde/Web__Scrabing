import json
from TASK5 import all_movies
def analyse_movies_language(movies_list):
    language1={}             
    for i in movies_list:  
        count=0
        for j in movies_list:          
            if i["Original Language:"]==j["Original Language:"]:
               count=count+1
            language1.update({i["Original Language:"]:count})

    with open("language_6.json","w") as d:
        json.dump(language1,d,indent=4)  
    return language1

analyse_movies_language(all_movies)