from random import randrange

rand_elem = lambda array: array[randrange(len(array) - 1)]

arr = [4, 5, 13, 654, 5, 243, 23, 234, 5, 12, 3]

print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))