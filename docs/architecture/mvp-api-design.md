# Aim
This document outlines the specific data that needs to be passed for each of our distinct actions. Our actions are:

- Search Films
- Add new viewed film
- Delete viewed film
- Update viewed film
- View watched films

# Search Films
User Goal: 
- Find a film by name

Input:
- Search Text

Output:
- Matching films with basic metadata (director, release date)

Notes:
- Results come from external movie DB
- We should return enough info for the user to tell the films apart

# Add new viewed film
User Goal:
- Add a specific film to that users list of viewed films

Input:
- Selected film from film search function 

Output:
- Film added to their films viewed data with data:
    - Film metadata
    - User Film Rating
    - User film review
    - User film watched date

Notes:
- This should now be viewable on their "viewed" page
- We should be having a link here between a unique film_id and user_id

# Delete viewed film
User Goal:
- Remove a viewed film from their list

Input:
- Selected watched film entry

Output:
- Film removed from viewed list

Notes:
- Decision needed: do deleted watched films disappear completely, or are they soft-deleted for history?
- We should put a pop up on the screen so a user doesn't delete by accident

# Update Viewed Film
User Goal:
- Update user inputted data on a specific viewed film entry

Input:
- Select which items to update from a small list (rating, review, watched date)

Output:
- Updated data based on entry from user

Notes:
- Can only update user-inputted data
- Cannot update film specific data

# View Watched Films
User Goal:
- To view all watched films logged so far, including film metadata and user specific data

Input:
- Go to "films watched" page (this is too technical but alas)

Output:
- Tabular view of all watched films including film metadta and user specific data

Notes:
- This should be only this users data
- It should only return a tabular view of the dataset

