with open("random.txt") as file:
  lines = 0
  for line in file:
    if lines == 5:
      input("Press enter to continue...")
      lines = 0
    
    print(line, end="")

    lines += 1