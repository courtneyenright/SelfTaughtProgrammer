import math

#Challenge 1
class Apple():
    def __init__(self,a,b,c,d):
        self.quality = a
        self.brand = b
        self.color = c
        self.diam = d

apple = Apple("good", "Pink Lady", "red", 1.25)
print(apple.color)

#Challenge 2
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*math.pi

circ = Circle(5)
print(circ.area())

#Challenge 3
class Triangle():
    def __init__(self,b,h):
        self.base = b
        self.height = h

    def area(self):
        return self.height*self.base/2

triangle = Triangle(2,1)
print(triangle.area())

#Challenge 4
class Hexagon():
    def __init__(self, a):
        self.side = a
    def perimeter(self):
        return 6*self.side

hexa = Hexagon(4)
print(hexa.perimeter())

