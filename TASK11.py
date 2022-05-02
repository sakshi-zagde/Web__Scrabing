from TASK5 import all_movies
import json

def analyse_movies_genre():
    dict1={} 
    list1=[] 
    for i in all_movies:
       genre= i["Genre:"].split(",") 
       for s in genre:
          list1.append(s)
       count=0
       for j in list1:
           count=count+1   
           dict1.update({j:count})         
       with open("analyse_movies11.json","w") as file:
            json.dump(dict1,file,indent=4)       
analyse_movies_genre() 