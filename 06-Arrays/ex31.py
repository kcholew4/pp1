arr = [2, 3, 45, 20, 15, 44, 40, 52, 50, 11, 17, 31, 183]

even = [i for i in arr if i % 2 == 0]
odd = [i for i in arr if i % 2 != 0]

separated = [*even, *odd]

print(separated)