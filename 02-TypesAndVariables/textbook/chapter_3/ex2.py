try:
  hours = float(input("Enter Hours: "))
  rate = float(input("Enter Rate: "))
except: 
  print("Error, please enter numeric input")
  exit(1)


if hours > 40:
  bonusPay = (hours - 40) * rate * 1.5
  pay = 40 * rate + bonusPay
else:
  pay = hours * rate

print("Pay:", pay)