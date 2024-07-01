class Point : 
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def distance(self, otherPoint) : 
        return ((self.x - otherPoint.x) + (self.y - otherPoint.y))


point1 = Point(10, 8)
point2 = Point(5, 5)

distance = point1.distance(point2)

print(f"The distance is : {distance}")
