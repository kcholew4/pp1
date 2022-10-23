a = int(input("a = "))
b = int(input("b = "))

for i in range(0, a):
  if i == 0 or i == a - 1:
    printChar = "*"
  else:
    printChar = " "

  for j in range(0, b):
    if j == 0 or j == b - 1:
      print("*", end="")
    else:
      print(printChar, end="")

  print()