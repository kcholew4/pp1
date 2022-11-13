def power(x, n):
  return x*power(x, n-1) if n > 1 else x #Does not work for n < 1

print(power(5, 3))