from bs4 import BeautifulSoup
import requests
import html

url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(url=url)
website_html=response.text

soup=BeautifulSoup(website_html,'html.parser')

print(soup.title.text)
movie_title=[movie_name.getText() for movie_name in soup.find_all(name="h3",class_="title")]

movie=movie_title[::-1]
print(movie)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Top 100 Movies</title>
    <style>
    body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }}
    h1 {{ text-align: center; color: #333; }}
    ul {{ max-width: 600px; margin: auto; padding: 0; list-style-type: decimal; }}
    li {{ background: white; margin: 8px 0; padding: 10px; border-radius: 5px; box-shadow: 0 0 5px #ccc; }}
    </style>
</head>
<body>
    <h1>Empire's 100 Greatest Movies</h1>
    <ul>
        {movie_list}
    </ul>
</body>
</html>
"""


print()
print("******************************************")
# Build the HTML list
movie_list_items = "\n".join([f"<li>{title}</li>" for title in movie])
print(movie_list_items)

# Final HTML
final_html = html_template.format(movie_list=movie_list_items)

# Write to an HTML file
with open("100_Movies.html", mode="w", encoding="utf-8") as file:
    file.write(final_html)

print("HTML file created: 100_Movies.html")


