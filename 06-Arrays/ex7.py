arr = [i for i in range(1, 6)]

arr[0] -= 1

print(f"a. {arr}")

arr[len(arr) - 1] += 4

print(f"b. {arr}")

arr[int(len(arr) // 2)] *= 2

print(f"c. {arr}")

for index in range(len(arr)):
  arr[index] += 3

print(f"d. {arr}")