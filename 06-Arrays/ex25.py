def occurs(number, array):
  return True if number in array else False

arr = [15, 38, 7, 23, 14]

num = int(input("Number: "))
print(f"Array: {arr}")
print(f"number {num} {'appears' if occurs(num, arr) else 'does not appear'} in the array")