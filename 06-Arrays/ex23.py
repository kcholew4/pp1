arr1 = [23, 42, 54, 12, 2, 65, 56, 33, 33, 24, 0, 5, 23]
arr2 = [5, 2, 6, 23, 1, 5]
arr3 = [1234, 12, 1234, 123, 3]

# Returns sorted copy of an array
def bubblesort(_array):
  array = _array.copy()
  while True:
    changed = False
    for i in range(len(array) - 1):
      if array[i] > array[i+1]:
        # Swap elements in an array (python way)
        array[i], array[i+1] = array[i+1], array[i]
        changed = True

    if changed == False:
      return array


print(bubblesort(arr1))
print(bubblesort(arr2))
print(bubblesort(arr3))