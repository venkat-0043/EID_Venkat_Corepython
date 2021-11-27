class Square:
    # calculate the area, perimeter of Square

    # STATE
    def __init__(self, length):
        # initializing the instance attributes

        self.length = length

    # BEHAVIOR
    def area(self):
        # calculate the area of square
        return self.length * self.length

    def perimeter(self):
        # calculate and return the perimeter of square
        return 4 * self.length


s = Square(20)

print("area of square is : ", s.area())
print("perimeter of square is : ", s.perimeter())

