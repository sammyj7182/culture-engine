# import my tmdb_client module to use the search_film function
from .tmdb_client import search_film

response = search_film("Shoplifters")  # Call the search_film function with the query "Parasite"

print(response.status_code)  # Print the status code of the response
print(response.json())  # Print the JSON content of the response
