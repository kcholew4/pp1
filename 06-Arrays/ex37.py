arr = [
  [7, 3, 7, 9, 0],
  [2, 9, 0, 1, 5],
  [3, 8, 6, 4, 7],
  [8, 7, 1, 1, 5],
]

_sum = 0

for i in arr:
  _sum += i[-1:][0]

print(_sum)