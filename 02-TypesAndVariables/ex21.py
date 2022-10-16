import random

roll = random.randrange(1, 6);

guess = int(input("Your guess: "))

if roll == guess:
  print(True)