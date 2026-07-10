# import FastAPI class from the fastapi module
from fastapi import FastAPI, HTTPException
# import the film_search function from the film_service module
from .film_service import search_film

# create an instance of the FastAPI class
app = FastAPI()

# get endpoint for searching films
@app.get("/films/search")
async def film_search(query: str):
    # output my film dictionary to a variable
    film = search_film(query)

    # if the film is not found, raise an HTTPException with a 404 status code and a detail message
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")

    return film
