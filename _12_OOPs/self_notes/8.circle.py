# creating a variable PI at the module level
PI = 3.14


class Circle(object):
    # calculates the area, circumference

    # STATE
    def __init__(self, radius):
        # initializing the instance variable
        self.radius = radius

    # BEHAVIOR
    def circle_area(self):
        # returns the area of the circle
        return PI * (self.radius ** 2)

    def circle_perimeter(self):
        # returns the perimeter of the circle
        return 2 * PI * self.radius


c1 = Circle(20)

print("area of circle is : ", c1.circle_area())
print("perimeter of circle is : ", c1.circle_perimeter())






