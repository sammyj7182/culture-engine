# Import funtions from my specific modules to test
from pydantic import ValidationError
import pytest

from culture_engine.film_service import transform_film_response
from culture_engine.models.film import FilmSearchResult


# define a test function to check if the transformed response matches the expected output
def test_transform_film_response():

    # define a sample tmdb JSON response to use in the test
    test_tmdb_response = [
        {
            "id": 12345,
            "title": "Shoplifters",
            "release_date": "2023-01-01",
            "overview": "One of the best films ever made, a masterpiece of storytelling and character development.",
            "poster_path": "/test_poster.jpg"
        }
    ]

    # then call my function to transform the test JSON response and store the result in a variable
    film_response_transformed = transform_film_response(test_tmdb_response)   
    
    # assert that the transformed response is a list of FilmSearchResult objects
    assert isinstance(film_response_transformed, list)

    # assert the length of the transformed response matches the expected output
    assert len(film_response_transformed) == 1

    # assert output is of type FilmSearchResult
    assert isinstance(film_response_transformed[0], FilmSearchResult)

    # assert that the transformed response matches the expected output
    assert film_response_transformed[0].tmdb_id         == 12345
    assert film_response_transformed[0].title           == "Shoplifters"
    assert film_response_transformed[0].release_date    == "2023-01-01"
    assert film_response_transformed[0].overview        == "One of the best films ever made, a masterpiece of storytelling and character development."
    assert film_response_transformed[0].poster_path     == "/test_poster.jpg"


def test_transform_film_response_missing_title_raises_validation_error():
    # define a sample tmdb JSON response with missing title to use in the test
    test_tmdb_response = [
        {
            "id": 12345,
            "release_date": "2023-01-01",
            "overview": "One of the best films ever made, a masterpiece of storytelling and character development.",
            "poster_path": "/test_poster.jpg"
        }
    ]

    # check that a validationerror is raised when the title is missing
    with pytest.raises(ValidationError):
        # check if this raises a validation error when the title is missing
        transform_film_response(test_tmdb_response)

    
    
def test_transform_film_response_missing_id_raises_validation_error():
    # define a sample tmdb JSON response with missing title to use in the test
    test_tmdb_response = [
        {
            "title": "Shoplifters",
            "release_date": "2023-01-01",
            "overview": "One of the best films ever made, a masterpiece of storytelling and character development.",
            "poster_path": "/test_poster.jpg"
        }
    ]

    # check that a validationerror is raised when the title is missing
    with pytest.raises(ValidationError):
        # check if this raises a validation error when the title is missing
        transform_film_response(test_tmdb_response)




