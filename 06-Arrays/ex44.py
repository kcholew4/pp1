def display(m):
  for i in m:
    for j in i:
      print(j, end=" ")

    print()

  print()


def transpose_matrix(m: list):
  transposed = [
    [0 for i in m] for j in m[0]
  ]

  for iidx, i in enumerate(m):
    for jidx, j in enumerate(i):
      transposed[jidx][iidx] = j
  
  return transposed
 

display(transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
display(transpose_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]))
display(transpose_matrix([[5, 6, 7, 8]]))