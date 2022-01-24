import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


point1 = Point(2, 2)
point2 = Point(-2, -2)
print(point1.distance(point2))
