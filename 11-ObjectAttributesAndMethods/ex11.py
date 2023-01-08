import math

class Area:
  @staticmethod
  def triangle(base, height):
    return (base * height) / 2

  @staticmethod
  def rectangle(a, b):
    return a * b

  @staticmethod
  def circle(radius):
    return math.pi * radius**2

area = Area()


print(area.circle(3))
print(area.rectangle(4, 7))
print(area.triangle(6, 2))