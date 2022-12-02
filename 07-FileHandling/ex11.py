film_titles = ["Psy", "Chłopaki nie płaczą", "Killer", "Symetria", "Kapitan Bomba"]

file = open("films.txt", "w")

for title in film_titles:
  file.write(f"{title}\n")

file.close()