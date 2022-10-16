def count(word, letter):
  count = 0

  for char in word:
    if char == letter:
      count = count + 1

  return count

print(count("banana", "a"))