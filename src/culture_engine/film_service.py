from .tmdb_client import search_films_tmdb

# define a function to format the JSON response from the TMDB API into a more readable format with specific columns
def transform_film_response (results: list[dict]) -> list[dict]:
    """
    Inputs:
        results (list[dict]): List of dictionaries containing the raw JSON response from the TMDB API.

    Transform the raw JSON response into specific columns that are currently hardcoded below

    Returns:
        list: List of dictionaries containing the formatted JSON response.
    
    """   
    # Create a list to hold the formatted results
    formatted_results = []
    
    # Loop through each result in the JSON response
    for result in results:
        # Create a dictionary to hold the formatted result
        formatted_result = {
            "tmdb_id": result.get("id"),
            "title": result.get("title"),
            "release_date": result.get("release_date"),
            "overview": result.get("overview"),
            "poster_path": result.get("poster_path")
        }
        # Append the formatted result to the list of formatted results
        formatted_results.append(formatted_result)
    
    return formatted_results

def search_films(query: str) -> list[dict]:
    """
    Inputs:
        query (str): The search query for the film. Usually the title of the film.
    Search TMDB for films matching the supplied query and return the formatted JSON response.
    Outputs:
        list[dict]: List of dictionaries containing the formatted JSON response."""
    raw_results = search_films_tmdb(query)
    return transform_film_response(raw_results)