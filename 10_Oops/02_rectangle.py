class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width 

    def perimeter(self):
        return 2*(self.length + self.width)

    def display(self):
        print(f"Area of rectangle : {self.area()}")
        print(f"Perimeter of rectangle : {self.perimeter()}")

length = int(input("Enter lendth: "))
width = int(input("Enter width: "))

rectangle1 = Rectangle(length, width)
rectangle1.display()
