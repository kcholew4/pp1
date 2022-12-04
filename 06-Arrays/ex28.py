def median(array):
  if len(array) % 2 == 0:
    return (array[int(len(array) / 2 - 1)] + array[int(len(array) / 2)]) / 2
  else:
    return array[int((len(array) - 1) / 2)]

arr1 = [1, 0, 9, 4, 6]
arr2 = [6, 8, 3, 1, 0, 5, 7]

print(median(arr1))
print(median(arr2))