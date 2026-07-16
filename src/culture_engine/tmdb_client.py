# import the httpx library for making HTTP requests
import httpx
# import the os library to access environment variables
import os
# import the load_dotenv function from the dotenv library to load environment variables from a .env file
from dotenv import load_dotenv

# import exceptions module to handle custom exceptions
from culture_engine.exceptions import TMDBAuthenticationError

# load the environment variables from the .env file
load_dotenv()

# load the TMDB API bearer token from the environment variables
TMDB_BEARER_TOKEN = os.getenv("TMDB_BEARER_TOKEN")

# Hard code URL for now but in future will live somewhere else (maybe config)
TMDB_API_URL = "https://api.themoviedb.org/3"

# define a function to search for films using the TMDB API
def search_films_tmdb(query: str) -> list[dict]:
    """
    Inputs:
        Query (str): The search query for the film. Usually the title of the film.

    Search TMDB for films matching the supplied query.

    Returns:
        list[dict]: A list of dictionaries representing the search results from the TMDB API.
    
    """
    # Build full film specific URL for the TMDB API search endpoint
    url = f"{TMDB_API_URL}/search/movie"

    # Get response from the TMDB API using the httpx library
    response = httpx.get(url, 
                         params={"query": query}, 
                         headers={"Authorization": f"Bearer {TMDB_BEARER_TOKEN}"})
    
    if response.status_code == 401:
        raise TMDBAuthenticationError("Authentication failed. Please check your TMDB API bearer token.")
    
    # check response status code and raise an exception if the request was not successful
    response.raise_for_status()
    # output formatted JSON response
    return response.json().get("results", [])

