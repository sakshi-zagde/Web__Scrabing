from TASK2 import dec
import json       

def group_by_decade(movies):
    moviedec={}
    list=[]
    for i in movies:               
        mod=i%10
        decade=i-mod
        if decade not in list:
           list.append(decade)
    list.sort()
    for i in list:
        moviedec[i]=[]
    for i in moviedec:
        decade10=i+9
        for x in movies:            
            if x<=decade10 and x>=i:
                for v in movies[x]:                 
                    moviedec[i].append(v) 

    with open("movie_by_decade3.json","w") as s:
        json.dump(moviedec,s,indent=4)      
    return (moviedec)                                                    
group=group_by_decade(dec) 