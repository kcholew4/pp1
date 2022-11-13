def digitSum(number):
  sum = 0

  for digit in str(number):
    sum += int(digit)

  return sum

print(digitSum(7182))