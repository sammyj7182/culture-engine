from .tmdb_client import search_films_tmdb
from .models.film import FilmSearchResult

# define a function to format the JSON response from the TMDB API into a more readable format with specific columns
def transform_film_response (results: list[dict]) -> list[FilmSearchResult]:
    """
    Inputs:
        results (list[dict]): List of dictionaries containing the raw JSON response from the TMDB API.

    Transform the raw JSON response into specific columns that are currently hardcoded below

    Returns:
        list[FilmSearchResult]: List of FilmSearchResult objects
    
    """   
    # define formatted results as an empty list to append to, explicitly defining the type as a list of FilmSearchResult objects for clarity and type checking
    formatted_results: list[FilmSearchResult] = []
    
    # Loop through each result in the JSON response
    for result in results:
        # Create a dictionary to hold the formatted result
        formatted_result = {
            "tmdb_id"       : result.get("id"),
            "title"         : result.get("title"),
            "release_date"  : result.get("release_date"),
            "overview"      : result.get("overview"),
            "poster_path"   : result.get("poster_path")
        }
        # Append the formatted result to the list of formatted results and validate against my FilmSearchResult model
        formatted_results.append(FilmSearchResult(**formatted_result))
    
    return formatted_results

def search_films(query: str) -> list[FilmSearchResult]:
    """
    Inputs:
        query (str): The search query for the film. Usually the title of the film.
    Search TMDB for films matching the supplied query and return the formatted JSON response.
    Outputs:
        list[FilmSearchResult]: List of FilmSearchResult objects containing the formatted JSON response."""
    raw_results = search_films_tmdb(query)
    return transform_film_response(raw_results)