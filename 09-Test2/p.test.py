try:
  import p1

  assert p1.f("AJ972","AQT72") == False
  assert p1.f("9532","K8") == True
  assert p1.f("987","AT4") == False

  print("p1: OK")
except:
  print("p1: FAILED")

try:
  import p2

  assert p2.f(15) == 72
  assert p2.f(2) == 20

  print("p2: OK")
except:
  print("p2: FAILED")

try:
  import p3

  assert p3.f([[3, 6, 2, 7], [9, 5, 4, 0], [2, 8, 0, 9]]) == [14, 19, 6, 16]

  print("p3: OK")
except:
  print("p3: FAILED")

try:
  import p4

  assert p4.f({"arr1": [4, 5, 6], "arr2": [7, 5]}, 5, 6) == 16

  print("p4: OK")

  print("p4: ", end="")
  print(p4.f({"arr1": [2, 6, 5], "arr2": [7, 1], "arr3": [2, 9, 8, 1]}, 5, 10))
except:
  print("p4: FAILED")

import p5

print("p5: ", end="")
print(p5.f("w", "d"))

import p6

print("p6: ", end="")
print(p6.f(21, "statistics", 4))