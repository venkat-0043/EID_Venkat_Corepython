class Fan:
    # stores the fan details

    # STATE
    def __init__(self, brand, price, speed):
        # initializing instance attributes
        self.brand = brand
        self.price = price
        self.speed = speed

    # BEHAVIOR
    def get_brand(self):
        # return the fan brand
        return self.brand

    def get_price(self):
        # returns the fan price
        return self.price

    def get_speed(self):
        # returns the fan speed
        return self.speed


f = Fan('Havells', 3000, '100 RPM')

print("brand is : ", f.get_brand())
print("fan price is : ", f.get_price())
print("fan speed is : ", f.get_speed())