"""
Unit tests for the tmdb_client module.
"""
# Import my modules
import pytest
import culture_engine.tmdb_client as tmdb_client
from unittest.mock import patch
from culture_engine.exceptions import TMDBAuthenticationError, TMDBUnavailableError

# create my patch for the httpx.get method to mock the response from the TMDB API
def test_search_films_tmdb_success():    

    #define my mock response to return from the TMDB API
    mock_response = {
        "results": [
            {
                "id": 12345,
                "title": "Shoplifters",
                "release_date": "2023-01-01",
                "overview": "One of the best films ever made.",
                "poster_path": "/test_poster.jpg",
            }
        ]
    }

    # create my patch for the httpx.get method to mock the response from the TMDB API
    with patch("culture_engine.tmdb_client.httpx.get") as mock_get:
        # define successful response for the mock get request
        mock_get.return_value.status_code = 200
        # define the json method of the mock response to return my mock response
        mock_get.return_value.json.return_value = mock_response

        # call the search_films_tmdb function with a test query and store the results in a variable
        results = tmdb_client.search_films_tmdb("Shoplifters")

    # check my results match the mock response and that the mock get method was called once
    assert results == mock_response["results"]
    mock_get.assert_called_once()

# now I will create a test for the TMDBAuthenticationError exception
def test_search_films_tmdb_authentication_error():
    # create my patch for the httpx.get method to mock the response from the TMDB API
    with patch("culture_engine.tmdb_client.httpx.get") as mock_get:
        # define failed authentication response for the mock get request
        mock_get.return_value.status_code = 401

        # check that the TMDBAuthenticationError exception is raised when the status code is 401
        with pytest.raises(TMDBAuthenticationError):
            tmdb_client.search_films_tmdb("Shoplifters")

# now I will create a test for the TMDBUnavailableError exception
def test_search_films_tmdb_unavailable_error_code():
    # create my patch for the httpx.get method to mock the response from the TMDB API
    with patch("culture_engine.tmdb_client.httpx.get") as mock_get:
        # define unavailable response for the mock get request
        mock_get.return_value.status_code = 503

        # check that the TMDBUnavailableError exception is raised when the status code is 503
        with pytest.raises(TMDBUnavailableError):
            tmdb_client.search_films_tmdb("Shoplifters")

# now another one for the TMDBUnavailableError exception but this time for a request error
def test_search_films_tmdb_unavailable_error_request():
    # create my patch for the httpx.get method to mock the response from the TMDB API
    with patch("culture_engine.tmdb_client.httpx.get") as mock_get:
        # define a request error for the mock get request
        mock_get.side_effect = tmdb_client.httpx.RequestError("Request failed")

        # check that the TMDBUnavailableError exception is raised when a request error occurs
        with pytest.raises(TMDBUnavailableError):
            tmdb_client.search_films_tmdb("Shoplifters")


