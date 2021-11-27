class Rectangle:
    # calculate the area, perimeter of rectangle

    # STATE
    def __init__(self, length, width):
        # initializing instance attributes

        self.length = length
        self.width = width

    # BEHAVIOR
    def area(self):
        # calculate the area of rectangle
        return self.length * self.width

    def perimeter(self):
        # calculate the perimeter of the rectangle
        return 2 * (self.width + self.length)


r1 = Rectangle(20, 30)

print("area of rectangle is : ", r1.area())
print("perimeter of rectangle is : ", r1.perimeter())