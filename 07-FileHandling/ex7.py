file = open("countries.txt", "r")

for index, line in enumerate(file):
  print(f"{index+1}. {line}", end="")

print()

file.close()