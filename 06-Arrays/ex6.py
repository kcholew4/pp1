arr = [2, 3, 7, 5, 4]

print(f"a. {arr}")
print(f"b. {len(arr)}")
print(f"c. {arr[0]}")
print(f"d. {arr[1]}")
print(f"e. {arr[len(arr)-1]}")
print(f"f. {arr[len(arr)-2]}")
print(f"g. {arr[0] + arr[len(arr) - 1]}")
print(f"h. {arr[int(len(arr) // 2)]}")

print("i. ", end="")

for i in arr:
  print(i, " ", end="")

print("\nj. ", end="")

for j in arr[:int((len(arr) - 1) / 2)]:
  print(j, " ", end="")

print()