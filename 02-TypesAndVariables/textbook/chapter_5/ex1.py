total = 0
count = 0

while True:
  userInput = input("Enter a number: ");

  if userInput == "done":
    break

  try:
    number = int(userInput)
  except:
    print("Invalid input")
    continue

  total = total + number
  count = count + 1
  avg = total / count

print(total, count, avg)

