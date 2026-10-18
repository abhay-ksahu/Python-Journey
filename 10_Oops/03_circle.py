import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def circumference(self):
        return 2* math.pi * self.radius    

    def display(self):
        print(f"Area of circle : {self.area():.2f}")

        print(f"Circumference of circle : {self.circumference():.2f}")

radius = float(input("Enter radius of circle: "))

circle1 = Circle(radius)
circle1.display()
