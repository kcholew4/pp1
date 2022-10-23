pin = "0805"

for i in range(0, 3):
  userInput = input("Enter the PIN code: ")

  if userInput == pin:
    print("Correct!")
    exit()

  print("Incorrect...")

print("Sorry, your payment card has been blocked.")