from TASK1 import scrapped
import json

def group_by_year(movies):             
    years=[]
    for i in movies:
        year=i['Year']
        if year not in years:
            years.append(year)
    # movie_dict={j:[] for j in years} 
    movie_dict={} 
    for j in years:
        movie_dict.update({j:[]})                 
    for i in movies:
        year=i['Year']
        for j in years:
            if j==year:
                movie_dict[j].append(i)
    with open("movie_by_year.json","w") as d:
        json.dump(movie_dict,d,indent=4)

    return movie_dict
dec=group_by_year(scrapped)