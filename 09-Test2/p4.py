def f(dictionary, x, y):
  _sum = 0

  for key, value in dictionary.items():
    _sum += sum([i for i in value if i >= x and i <= y])

  return _sum
