quantity, sum = 0, 0

while True:
  number = int(input("Enter a number: "))

  if number == 0:
    break
  
  quantity += 1
  sum += number

mean = sum / quantity

print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")