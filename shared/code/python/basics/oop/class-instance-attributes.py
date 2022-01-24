class Point:
    coeff = 5  # Attribut de classe accessible à toutes les instances

    def __init__(self, x, y):
        self.x = x  # Attribut d'instance
        self.y = y  # Attribut d'instance


point1 = Point(1, 2)
point2 = Point(3, 4)
print(point1.x, point1.y, point1.coeff)
print(point2.x, point2.y, point2.coeff)
