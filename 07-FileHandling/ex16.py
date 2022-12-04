with open("random.txt") as file:
  with open("copy.txt", "w") as fileCopy:
    fileCopy.write(file.read())