class Employee(object):
    # stores employee details

    # STATE
    def __init__(self, name, eid, salary):
        # initializing instance attributes

        self.name = name
        self.eid = eid
        self.salary = salary

    # BEHAVIOR
    def get_details(self):
        # display employee details

        print("employee name is : ", self.name)
        print(self.name, " id is : ", self.eid)
        print(self.name, " salary is : ", self.salary)


e1 = Employee('venkat', '123', 10000)
e1.get_details()

e2 = Employee('satish', '456', 20000)
e2.get_details()
