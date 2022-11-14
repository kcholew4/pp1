arr = [[2,5,4],[9,0,3]]

print(f"a. {arr}")
print(f"b. rows: {len(arr)}, columns: {len(arr[0])}")
print(f"c. {arr[0][1]}")
print(f"c. {arr[1][2]}")

print("e. ", end="")

for i in arr[1]:
  print(i, end=" ")

print()