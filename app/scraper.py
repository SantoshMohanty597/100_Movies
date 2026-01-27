from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

def scrape_movies():
    response = requests.get(url=URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    movie_titles = [
        movie.getText()
        for movie in soup.find_all(name="h3", class_="title")
    ]

    return movie_titles[::-1]