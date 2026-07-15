# Import pydantic BaseModel and Field for data validation and model definition
from pydantic import BaseModel, Field

# Create a Film model that inherits from BaseModel
class FilmSearchResult(BaseModel):
    """
    Represents a film returned by the Culture Engine film search service.
    """
    tmdb_id: int = Field(..., description="The unique identifier for the film in TMDB.")
    title: str = Field(..., description="The title of the film.")
    release_date: str | None = Field(..., description="The release date of the film in YYYY-MM-DD format.") 
    overview: str | None = Field(..., description="A brief summary or overview of the film.") 
    poster_path: str | None = Field(..., description="The path to the poster image for the film.") 


