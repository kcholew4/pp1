from random import randint

with open("numbers.txt", "w") as file:
  for i in range(100):
    file.write(f"{randint(1, 50)}\n")