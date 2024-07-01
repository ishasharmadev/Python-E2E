from abc import ABC, abstractmethod

class Shape(ABC) :
    def area(self) :
        pass

    def perimeter(self) : 
        pass

class Triangle(Shape) :
    def __init__(self, base, height) :
        self.base = base
        self.height = height

    def area(self) : 
        return 0.5 * self.base * self.height
    

class Square(Shape) :
    def __init__(self, side) :
        self.side = side

    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side
    

tri = Triangle(10, 5)
sq = Square(5)

triArea = tri.area()
print(f"Area of triangle is {triArea}")

sqArea = sq.area()
sqPeri = sq.perimeter()
print(f"Area of square is = {sqArea} and its perimeter is {sqPeri}")