import json

# Json example...
filename = "films.json"

# Read f i l e
with open(filename, "r") as f:
    films = json.load(f)

# We must get user inputs..
genre = input("Enter the genre: ")
year = input("Enter the year: ")
actor = input("Enter the actor: ")

# After, user select film criterias, films filtering..
filtered_films = []
for film in films:
    if genre and genre.lower() not in film["genres"].lower():
        continue
    if year and year != film["year"]:
        continue
    if actor and actor.lower() not in film["actors"].lower():
        continue
    filtered_films.append(film)

# Show filterated film list
if filtered_films:
    for film in filtered_films:
        print(f"{film['title']} ({film['year']})")
        print(f"Genres: {film['genres']}")
        print(f"Actors: {film['actors']}")
        print(f"Plot: {film['plot']}\n")
else:
    print("No films found for the given criteria.")
