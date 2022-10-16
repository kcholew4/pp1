max = None
min = None

while True:
  userInput = input("Enter a number: ");

  if userInput == "done":
    break

  try:
    number = int(userInput)
  except:
    print("Invalid input")
    continue

  if max is None or number > max:
    max = number

  if min is None or number < min:
    min = number

print("Max:", max)
print("Min:", min)

