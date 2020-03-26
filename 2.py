class Human:
    def __init__(self, name):
        self.name = name


def function1(self):
    print('I am Student '+self.name)

Student = type('Student', (Human,), {'f1': function1})
st1 = Student('Petr')
st1.f1()
