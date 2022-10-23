amount = int(input("Enter the amount in PLN: "))

print(f"The amount of PLN {amount} in coins:")

pln5 = amount // 5
pln2 = (amount % 5) // 2
pln1 = amount % 5 % 2

print(f"5 zł - {pln5}")
print(f"2 zł - {pln2}")
print(f"1 zł - {pln1}")