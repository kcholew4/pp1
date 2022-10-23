humansYears = int(input("Enter the dog's age in human years: "))

if humansYears <= 2:
  dogsYears = humansYears * 10.5
else:
  dogsYears = 2 * 10.5 + (humansYears - 2) * 4

print(f"The dog's age in dog's yers is {int(dogsYears)} years.")