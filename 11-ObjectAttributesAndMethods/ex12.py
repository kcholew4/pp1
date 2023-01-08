import math

class Point:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return f"P({self.x}, {self.y})"

  def __eq__(self, __o: object) -> bool:
    return __o.x == self.x and __o.y == self.y

  @staticmethod
  def distance(point_a: object, point_b: object):
    p = (point_a.x, point_a.y)
    q = (point_b.x, point_b.y)

    return math.dist(p, q)


point_a = Point(9, 0)
point_b = Point(0, 0)

if point_a == point_b:
  print("points are equal!")
else:
  print(Point.distance(point_a, point_b))