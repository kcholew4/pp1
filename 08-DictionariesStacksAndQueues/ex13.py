import json

student = {
  "name": "Janusz",
  "surname": "Kowalski",
  "iq": 100,
  "male": True,
  "height": 180,
  "hobbies": ["gaming", "netflix", "watching tv"],
  "friends": 312
}

with open("student.json", "w") as file:
  json.dump(student, file, indent="  ")