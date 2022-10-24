import mymath

randNum = mymath.generate_number()

i = 1

while True:
  num = mymath.read_number()

  if num == randNum:
    break

  i += 1

print(f"Guessed at {i} try!")