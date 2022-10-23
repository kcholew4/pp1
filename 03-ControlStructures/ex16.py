first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("Numbers in ascending order: ", end="")

if first < second:
  print(f"{first}, {second}")
else:
  print(f"{second}, {first}")