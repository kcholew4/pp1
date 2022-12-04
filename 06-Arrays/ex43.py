def identity_matrix(n):
  return [
      [1 if j == i else 0 for j in range(n)] for i in range(n)
  ]


def display(arr):
  for i in arr:
      for j in i:
          print(j, end=" ")

      print()

  print()


display(identity_matrix(3))
display(identity_matrix(5))
display(identity_matrix(8))
