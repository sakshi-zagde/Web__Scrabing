import requests
from bs4 import BeautifulSoup
import json

def scrape_top_list():
    adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    adventure_api=requests.get(adventure_url)
    soup = BeautifulSoup(adventure_api.text,"html.parser")
    table_tag = soup.find("table", class_="table")
    tr = table_tag.find_all("tr")
    top_movie=[] 
    for i in tr[1:]:
        movie_rank=i.find("td",class_="bold")
        rank1=movie_rank.get_text()
        rank=rank1
        movie_rating=i.find("span",class_="tMeterScore")
        rating=movie_rating.get_text().strip()
        movie_name = i.find("a",class_="unstyled articleLink")
        title=movie_name.get_text().strip()
        list=title.split()
        year=list[-1][1:5]
        year1=int(year)
        name_length=len(list)-1
        name=""
        for l in range(name_length):
            name+=" "
            name+=list[l]
        MovieName=name                
        movie_Reviews = i.find("td",class_="right hidden-xs")
        reviews=movie_Reviews.get_text()
        url=i.find("a",class_="unstyled articleLink")
        link=url.get_text() 
        link=url["href"]
        movie_link="https://www.rottentomatoes.com"+link
        details={}
        details["Movie Rank"]=rank
        details["Movie Rating"]=rating
        details["Movie Name"]=MovieName
        details["Movie Reviews"]=reviews
        details["Movie URL"]=movie_link
        details["Year"]=year1
        top_movie.append(details)
    with open("top_movie1.json","w") as file:
        json.dump(top_movie,file,indent=3)  
    return top_movie                 
scrapped=scrape_top_list()