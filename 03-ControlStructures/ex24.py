maxHeight = 5

for i in range(0, maxHeight):
  for j in range(0, i + 1):
    print("*", end=" ")

  print()

for k in range(maxHeight - 1, 0, -1):
  for l in range(k, 0, -1):
    print("*", end=" ")

  print()