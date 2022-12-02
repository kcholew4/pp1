file = open("powers.txt", "w")

for i in range(1, 11):
  file.write(f"{i}, {i**2}, {i**3}")
  file.write("\n")

file.close()