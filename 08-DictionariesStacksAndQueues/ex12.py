import json

film = {
  "name": "Scary Movie",
  "year": 1999,
  "rating": "8.6",
  "in_theaters": False,
  "director": "John Doe"
}

with open("favourite.json", "w") as file:
  json.dump(film, file, indent="  ")