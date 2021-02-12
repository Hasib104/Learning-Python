
from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-century-page-10/")
web_page = response.text
#print(web_page)

soup = BeautifulSoup(web_page, "html.parser")
#print(soup.prettify())
movies = soup.select(selector="p strong")

movies_name = [movie.getText() for movie in movies][::-1]
print(movies_name)

#movies_name_list = []
# for item in range(len(movies) - 1, -1, -1):
#     movies_name = movies[item].getText()
#     movies_name_list.append(movies_name)
# #print(movies_name_list)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for item in movies_name:
        file.write(f"{item}\n")