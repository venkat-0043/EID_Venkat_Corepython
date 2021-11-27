class Email:
    # Generates the employ emails

    # STATE
    def __init__(self, first, last):
        # initializing the instance attributes

        self.first = first
        self.last = last

    def get_firstname(self):
        # returns the first name of employ
        return self.first

    def get_lastname(self):
        # returns the last name of employ
        return self.last

    def email(self):
        # returns the email of employ
        return self.first + self.last + '@gmail.com'


e = Email('john', 'mike')

print("first name is : ", e.first)
print("last name is : ", e.last)
print("email is : ", e.email())



