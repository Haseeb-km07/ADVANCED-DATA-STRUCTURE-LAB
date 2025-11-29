
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


l1 = float(input("Enter length of Rectangle 1: "))
w1 = float(input("Enter width of Rectangle 1: "))

l2 = float(input("Enter length of Rectangle 2: "))
w2 = float(input("Enter width of Rectangle 2: "))

r1 = Rectangle(l1, w1)
r2 = Rectangle(l2, w2)

if r1 < r2:
    print("Rectangle 1 has smaller area")
elif r2 < r1:
    print("Rectangle 2 has smaller area")
else:
    print("Both rectangles have equal area")