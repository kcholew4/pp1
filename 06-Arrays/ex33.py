arr = [1, 23, 5, 382, 1, 17, 4, 906]

print('-'*(len(arr) * 5 + 1))
print("|" + "|".join([str(i).rjust(4, " ") for i in arr]) + "|")
print('-'*(len(arr) * 5 + 1))