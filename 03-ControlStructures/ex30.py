def isPrime(number):
  if number <= 1:
    return False

  for i in range(2, number):
    if number % i == 0:
      return False

  return True


#Prints prime numbers from 1 to N

n = int(input("Enter the value of N: "))

print("Prime numbers: ", end="")

for i in range(1, n + 1):
  if isPrime(i):
    print(i, end=" ")

print()
