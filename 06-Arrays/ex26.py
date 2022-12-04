arr = [5, 1, 9, 6, 1]

_arr = set(arr.copy())
_arr.remove(max(_arr))

secondLargest = max(_arr)

print(f"Array: {arr}")
print(f"Result: {secondLargest}")