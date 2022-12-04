arr1 = [
  [2, 3],
  [1, 5]
]

arr2 = [
  [5, 0, 3, 7, 5],
  [9, 0, 9, 1, 2]
]

arr3 = [
  [2, 1],
  [3, 5],
  [7, 4],
  [2, 6]
]

def flatten(array):
  return [j for i in array for j in i]

print(flatten(arr1))
print(flatten(arr2))
print(flatten(arr3))