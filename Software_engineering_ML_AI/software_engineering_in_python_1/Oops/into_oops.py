# Write your code below
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print('My id is {}'.format(self.id))


e1 = Employee()
e2 = Employee()
print(e1, e2)