file = open("numbers.txt", "r")

_sum = 0

for line in file:
  try:
    _sum += int(line)
  except:
    continue

print(_sum)