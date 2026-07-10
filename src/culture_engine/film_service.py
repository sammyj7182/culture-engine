


def search_film(query: str):
    """
    Search for a film based on the provided query value input.
    For now this only has one "successful" route which is searching alien - we will add to this later.
    """
    # simple hard-coded message to return if someone searches for the film "Alien"
    if query.lower() == "alien":
        return {
                    "title": "Alien",
                    "year": 1979,
                    "director": "Ridley Scott"
                }
            
    # if not alien then return nada
    return None

    