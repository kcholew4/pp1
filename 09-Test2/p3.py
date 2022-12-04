def f(array2D: list):
  array1D = [0 for i in array2D[0]]

  for i in array2D:
    for idx, j in enumerate(i):
      array1D[idx] += j

  return array1D
