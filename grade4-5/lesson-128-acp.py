import math  # for using pi

# Creating Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius   # attribute

    # Method to calculate area
    def area(self):
        return math.pi * (self.radius ** 2)

    # Method to calculate perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius


# Creating an object of Circle
r = float(input("Enter the radius of the circle: "))
circle1 = Circle(r)

# Calling methods
print("Area of the circle:", circle1.area())
print("Perimeter of the circle:", circle1.perimeter())
