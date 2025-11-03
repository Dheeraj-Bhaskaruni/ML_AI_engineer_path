class Employee():
    def __init__(self):
        self.id = None
        # Write your code below
        self._id = 10
        self.__id = 20


e = Employee()
print(dir(e))