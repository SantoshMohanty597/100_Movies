from scraper import scrape_movies

def main():
    movies = scrape_movies()

    with open("100_Movie_name.txt", mode="w", encoding="utf-8") as file:
        for movie in movies:
            file.write(f"{movie}\n")

    print("✅ Movie list saved successfully")

if __name__ == "__main__":
    main()