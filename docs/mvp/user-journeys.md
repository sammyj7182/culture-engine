# Aim
This document aims to to outline the key user journeys that will take place inside the platform, it will not document them in technical detail but it will show clearly what a user will do. 

# User Flows
## Film Search
A user will be able to search using free text, for the name of a film and it will return all films with that name. 

- It will be it's own tab on the platform
- This tab will contain a search bar which can take text 
- Users will be able to click a "viewed" button (can rename the button) which will take them to a screen to add an optional rating out of 100 (we will come back to this later)
- To help users differentiate films with the same name it will return the date of release where possible
- It will provide suggestions based on the words/letters already in the search bar

## Tagging a film as viewed
A user will be able to tag a searched film as "viewed" this will bring up a pop up page which will allow the user to enter:

- A score from 0-100
- A written review (x amount of characters max)
- A date watched

All of this will be optional, the user can fill in all of it or none of it. 

## Seeing viewed films
A user will be able to see all the films they've tagged as viewed in a separate tab on the platform. They will be able to:

- See the film name
- Some basic film metadata
- Their score out of 100
- Their review (shortened in visibility only)
- Their viewed date

The user can also do sub actions on these viewed films:

### Delete viewed films
A user will be able to delete one or multiple films from their viewed list.

- This will trigger a pop up asking the user to confirm they want to delete the films from their viewed list
- This will then remove all of the items that were deleted

### Viewed Films updates
A user will be able to update specific films in their list of viewed films. These are only user created data:

- Viewed date (can be updated to any day in the past or today)
- Rating (can update to be anything between 0-100)
- Review (can update the review text)

### Adding viewed films
Users should be able to add additional films from the "seeing viewed films" screen as well as from the search functionality. The idea here would be:

- Simple add box in the corner of the screen
- Brings up a search box which uses the same search functionality as the search screen

