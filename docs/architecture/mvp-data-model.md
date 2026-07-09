# Aim
The aim of this doc is to write down, at a high level the pieces of data required. 

# Data

## Film
A unique film stored in Culture Engine.

Likely data:
- external film ID
- external source
- title
- release date
- director

## User
This a unique entry for each user, where user is defined by some metric (probably related email or username)
- Unique name or username

## FilmWatched
Status of a film relating to a user, this is likely a bit of either watched or not
- film
- user
- rating
- review
- watched_date


