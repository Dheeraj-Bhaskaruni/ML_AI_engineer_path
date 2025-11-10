class School():
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudents(self, new_numberOfStudents):
        self.numberOfStudents = new_numberOfStudents

    def __repr__(self):
        return ('A {level} school named {name} with {numberOfStudents} students'.format(level, name, numberOfStudents))


# abc = School('dheeraj', '10', 120)

# print(abc.get_name())


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def getPickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + " The pickup policy is {pickupPolicy}.".format(pickupPolicy=self.pickupPolicy)






