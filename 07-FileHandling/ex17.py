with open("random.txt") as file:
  with open("copylines.txt", "w") as fileCopy:
    for line in file:
      fileCopy.write(line)