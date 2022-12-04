arr = [
  [2, 3, 4],
  [2, 6, 1],
  [7, 3, 6],
  [0, 9, 0],
  [6, 2, 1],
]


def display(arr):
  for i in arr:
    for j in i:
      print(j, end=" ")
    
    print()


display(arr)

arr[0], arr[-1] = arr[-1], arr[0]

print()
display(arr)