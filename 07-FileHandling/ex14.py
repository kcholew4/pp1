name = input("File name: ")

with open(name) as file:
  lines = 0
  for line in file:
    lines += 1

print(f"Number of lines: {lines}")