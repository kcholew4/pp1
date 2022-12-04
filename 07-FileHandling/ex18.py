with open("MeatAndFish.txt") as meatAndFishFile:
  meatAndFish = meatAndFishFile.read()

with open("GrainsAndBread.txt") as grainsAndBreadFile:
  grainsAndBread = grainsAndBreadFile.read()

with open("shoppinglist.txt", "w") as file:
  file.write(meatAndFish)
  file.write(grainsAndBread)