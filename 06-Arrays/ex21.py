def compare(arr1, arr2):
  if (len(arr1) != len(arr2)):
    return False
  
  for idx, i in enumerate(arr1):
    if arr2[idx] != i:
      return False

  return True

arrays = [
  [["water","book","sky"], ["water","book","sky"]],
  [[True,False], [True,False,True]],
  [[5, 3, 1], [5, 3, 1]],
  [[3, 2, 1], [3, 2]]
]

for i in arrays:
  arr1, arr2 = i[0], i[1]
  print(f"Array1: {arr1}")
  print(f"Array2: {arr2}")
  print(f"Comparasion: arrays are {'' if compare(arr1, arr2) else 'not '}the same\n")