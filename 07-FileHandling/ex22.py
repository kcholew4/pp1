import csv

with open("students.txt", newline="") as file:
  reader = csv.DictReader(file)

  for row in reader:
    if int(row["age"]) < 30:
      print(row["first_name"], row["last_name"], row["email"])