import copy

arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

table = copy.deepcopy(arr)

for iidx, i in enumerate(arr):
  for jidx, j in enumerate(i):
    table[iidx][jidx] = (iidx + 1) * (jidx + 1)

print(table)