# import FastAPI class from the fastapi module
from fastapi import FastAPI, HTTPException
# import the film_search function from the film_service module
from .film_service import search_films

# create an instance of the FastAPI class
app = FastAPI()

# get endpoint for searching films
@app.get("/films/search")
async def film_search(query: str):
    # output my film dictionary to a variable
    films = search_films(query)
    # films might be empty if no results, but that design is nice for now! 
    return films
