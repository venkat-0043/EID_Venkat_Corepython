class Arithmetic:
    # performs the arithmetic operations

    # STATE
    def __init__(self, a, b):
        # initializing instance attributes
        self.a = a
        self.b = b

    # BEHAVIOR
    def addition(self):
        # performs the addition operation
        return self.a + self.b

    def subtraction(self):
        # performs the subtraction operations
        return self.a - self.b

    def multiplication(self):
        # performs the multiple operation
        return self.a * self.b

    def division(self):
        # performs the division operation
        return self.a / self.b


a = Arithmetic(10, 20)

print("addition is : ", a.addition())
print("subtraction is : ", a.subtraction())
print("multiplication is : ", a.multiplication())
print("division is  : ", a.division())



