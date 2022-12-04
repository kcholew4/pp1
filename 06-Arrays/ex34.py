arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

strArr1 = ",".join([str(i) for i in arr1])
strArr2 = ",".join([str(i) for i in arr2])

print(f"arr1 is {'' if strArr2.find(strArr1) != -1 else 'not '}a subset of arr2")