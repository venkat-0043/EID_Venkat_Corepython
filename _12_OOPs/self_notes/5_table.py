class Table:
    # stores the table data

    # STATE
    def __init__(self, price, weight, height, wood_type):
        # initializing instance attributes
        # initialize self.warranty at the end
        self.warranty = None
        self.price = price
        self.weight = weight
        self.height = height
        self.wood_type = wood_type

    # BEHAVIOR
    def get_details(self):
        # displays the table details
        print("table price is : ", self.price)

        print("table weight is : ", self.weight)

        print("table wood is : ", self.wood_type)

        print("table warranty is : ", self.warranty)


t = Table(2000, '5kg', '1 meter', 'Teak')

t.warranty = True
t.get_details()




