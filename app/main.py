from bs4 import BeautifulSoup
import requests

url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(url=url)
website_html=response.text

soup=BeautifulSoup(website_html,'html.parser')

print(soup.title.text)
movie_title=[movie_name.getText() for movie_name in soup.find_all(name="h3",class_="title")]

movie=movie_title[::-1]

# with open("100_Movie_name.txt",mode="w") as file:
#     for movies in movie:
#         file.write(f"{movies}\n")

'''
🧠 Why This Works:
encoding="utf-8" ensures that all characters, including emojis and accented letters, are written correctly.
Without specifying this, Windows uses cp1252 by default, which doesn’t support all characters.
'''

with open("100_Movie_name.txt", mode="w", encoding="utf-8") as file:
    for movies in movie:
        file.write(f"{movies}\n")




