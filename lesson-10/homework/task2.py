import requests
import random

API_KEY = "a2000b6be9918b2bae6ebeb6b05eb458"
BASE_URL = "https://api.themoviedb.org/3"

def get_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    
    if response.status_code == 200:
        genres = response.json().get("genres", [])
        return {genre["name"].lower(): genre["id"] for genre in genres}
    else:
        print("Error fetching genres:", response.text)
        return {}

def get_movies(genre_id):
    """Fetch movies from TMDb based on genre ID."""
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print("Error fetching movies:", response.text)
        return []

def recommend_movie():
    """Ask user for a genre and recommend a random movie."""
    genres = get_genres()
    
    if not genres:
        print("Failed to fetch genres.")
        return
    
    print("\nAvailable genres:", ", ".join(genres.keys()))
    chosen_genre = input("Enter a movie genre: ").strip().lower()
    
    if chosen_genre not in genres:
        print("Invalid genre. Please try again.")
        return
    
    genre_id = genres[chosen_genre]
    movies = get_movies(genre_id)
    
    if not movies:
        print(f"No movies found for the genre '{chosen_genre}'.")
        return
    
    random_movie = random.choice(movies)
    print("Recommended Movie:")
    print(f"Title: {random_movie['title']}")
    print(f"Overview: {random_movie['overview']}")
    print(f"Rating: {random_movie['vote_average']}/10")
    print(f"Release Date: {random_movie['release_date']}")
    print(f"More details: https://www.themoviedb.org/movie/{random_movie['id']}")
recommend_movie()
