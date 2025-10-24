class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        self.diameter = diameter
        print('New circle with diameter: ' + str(self.diameter))


teaching_table = Circle(36)
