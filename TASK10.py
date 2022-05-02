from TASK5 import all_movies
import json

def analyse_language_and_directors(all_movies):           
    director={}
    for i in all_movies:
        count=0                 
        for j in all_movies:             
            if i["Director:"]==j["Director:"]:
                if i["Original Language:"]==j["Original Language:"]:
                    count=count+1  

            director.update({i["Director:"]:{i["Original Language:"]:count}})
    with open("language10.json","w") as d:
        json.dump(director,d,indent=4)

    return director
analyse_language_and_directors(all_movies)