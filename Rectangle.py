
class Rectangle:
    def __init__(self, length, breadth):     # correct constructor
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Creating two rectangle objects
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)

# Comparing the area
if r1.area() > r2.area():
    print("Rectangle 1 has a larger area")
elif r1.area() < r2.area():
    print("Rectangle 2 has a larger area")
else:
    print("Both rectangles have the same area")