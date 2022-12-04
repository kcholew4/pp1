arr = [[-38, 19], [5,40],[-7,11],[29,16]]

minVal = {"row": None, "column": None, "value": None}
maxVal = {"row": None, "column": None, "value": None}

for iidx, i in enumerate(arr):
  for jidx, j in enumerate(i):
    if minVal["value"] == None or j < minVal["value"]:
      minVal = { "row": iidx, "column": jidx, "value": j }
    if maxVal["value"] == None or j > maxVal["value"]:
      maxVal = { "row": iidx, "column": jidx, "value": j }

print(f"min: {minVal}")
print(f"max: {maxVal}")