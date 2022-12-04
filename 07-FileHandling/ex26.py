import re

with open("shoppinglist.txt") as file:
  content = file.read()

words = re.findall(r"\w{6,}", content)

for word in words:
  print(word)