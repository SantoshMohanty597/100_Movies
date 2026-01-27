from app.scraper import scrape_movies

def test_scrape_movies():
    movies = scrape_movies()

    assert isinstance(movies, list)
    assert len(movies) > 0
    assert "The Godfather" in movies