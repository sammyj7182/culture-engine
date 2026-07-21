"""
Module to define custom exceptions for the culture_engine package.
"""

class TMDBAuthenticationError(Exception):
    """
    Exception raised when there is an authentication error with the TMDB API.
    """
    pass

class TMDBUnavailableError(Exception):
    """
    Exception raised when the TMDB API is unavailable.
    """
    pass
