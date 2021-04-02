import requests
from bs4 import BeautifulSoup

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"
# URL = "https://www2.bfi.org.uk/greatest-films-all-time"
response = requests.get(url=URL)
website = response.text
soup = BeautifulSoup(website, 'html.parser')
titles_tag = soup.select(selector="h3 a")
titles_text = [movie.getText() for movie in titles_tag]

# print(titles_text)
movies = titles_text[99::-1]
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
