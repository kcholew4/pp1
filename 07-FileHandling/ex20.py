import random

file = open("random.txt", "w")

for i in range(50):
  file.write(str(random.randrange(100, 999)))
  file.write("\n")

file.close()