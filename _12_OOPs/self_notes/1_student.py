class Student:
    # stores student details

    # STATE
    def __init__(self, name, id, percentage):
        # initializing instance attributes

        self.name = name
        self.id = id
        self.percentage = percentage

    # BEHAVIOUR
    def get_details(self):
        # displays the student details

        print(self.name, " id is : ", self.id)
        print("student name is : ", self.name)
        print(self.name, " percentage is : ", self.percentage)


student1 = Student('mike', '101', '85%')
student1.get_details()

student2 = Student('john', '102', '70%')
student2.get_details()
