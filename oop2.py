import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Ask user for radius
r = float(input("Enter the radius of the circle: "))

# Create Circle object
my_circle = Circle(r)

# Display results
print(f"Area of the circle: {my_circle.area():.2f}")
print(f"Perimeter (Circumference) of the circle: {my_circle.perimeter():.2f}")