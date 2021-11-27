class Bitwise(object):
    # calculate the bitwise AND, OR, XOR

    # STATE
    def __init__(self, a, b):
        # initializing instance attributes
        self.a = a
        self.b = b

    # BEHAVIOUR
    def bitwise_and(self):
        # calculates the bitwise AND
        return self.a & self.b

    def bitwise_or(self):
        # calculates the bitwise OR
        return self.a | self.b

    def bitwise_xor(self):
        # calculates bitwise XOR
        return self.a ^ self.b


b = Bitwise(5, 6)

print("bitwise AND is : ", b.bitwise_and())
print("bitwise OR is :", b.bitwise_or())
print("bitwise XOR is : ", b.bitwise_xor())
