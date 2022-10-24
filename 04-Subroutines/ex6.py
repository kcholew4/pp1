def row(start):
  for i in range(start, start + 3):
    print(i, end=" ")

  print()

for i in range(1, 3*3+1, 3):
  row(i)