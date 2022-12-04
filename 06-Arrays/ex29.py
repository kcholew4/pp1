arr = [1, 3, 4, 5, 7, 123, 12, 34]

_min = int(input("Greater than: "))

count = len([i for i in arr if i > _min])

print(count)