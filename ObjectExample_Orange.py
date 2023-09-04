class Orange():
    def __init__(self, w, c):
        """weights are in ounces"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("created!")

    def rot(self, days, temp):
        self.mold = days*temp

orange = Orange(6, "orange")
print(orange.mold)
print(orange.color)
orange.rot(10,98)
print(orange.mold)

orange.color = "dark orange"
print(orange.color)


print("\n")

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width*self.length

    def change_size(self,w,l):
        self.width = w
        self.length = l

rectangle = Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())
