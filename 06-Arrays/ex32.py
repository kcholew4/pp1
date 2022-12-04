def arrToStr(array):
  return ",".join([str(i) for i in array])

arr = [5, 4, 3, 2, 6, 5]

print(f"Array: {arr}")
print(f"String: {arrToStr(arr)}")
