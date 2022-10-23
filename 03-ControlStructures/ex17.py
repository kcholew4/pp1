x = int(input("x = "))
y = int(input("y = "))

print(f"Point P({x}, {y}) ", end="")

if x == 0 and y == 0:
  print("is in the (0, 0) position")
elif x == 0:
  print("is on the y axis")
elif y == 0:
  print("is on the x axis")
elif x > 0 and y > 0:
  print("is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
  print("is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
  print("is in the third quadrant of the coordinate system")
elif x > 0 and y < 0:
  print("is in the fourth quadrant of the coordinate system")