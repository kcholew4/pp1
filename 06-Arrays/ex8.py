arr = [-15, 8, -31, 47, -2, 19]

_max = arr[0]
_min = arr[0]

for i in arr[1:]:
  if i > _max:
    _max = i

  if i < _min:
    _min = i


print(_max)
print(_min)