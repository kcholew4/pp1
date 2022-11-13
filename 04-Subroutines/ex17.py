def letterCount(text, letter):
  count = 0

  for char in text:
    count = count + 1 if char == letter else count

  return count

print(letterCount("You never get a second chance to make a first impression", "e"))