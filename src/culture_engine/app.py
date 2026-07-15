# import FastAPI class from the fastapi module
from fastapi import FastAPI
# Import my FilmSearchResult model from the models.film module
from .models.film import FilmSearchResult
# import the film_search function from the film_service module
from .film_service import search_films

# create an instance of the FastAPI class
app = FastAPI()

# get endpoint for searching films - using my response model FilmSearchResult to validate the response data
@app.get("/films/search", response_model=list[FilmSearchResult])
async def film_search(query: str) -> list[FilmSearchResult] :
    """
        Inputs:
            query (str): The search query for the film. Usually the title of the film.

        Outputs:
            list[FilmSearchResult]: List of FilmSearchResult objects containing the formatted JSON response.
    """
    # output my film dictionary to a variable
    films = search_films(query)
    # films might be empty if no results, but that design is nice for now! 
    return films
