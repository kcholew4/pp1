arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

name = arr[0]

for i in arr[1:]:
  if (len(i) > len(name)):
    name = i

print(name)