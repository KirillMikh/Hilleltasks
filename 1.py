class Person:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def __str__(self):
        return "{0}; dict={1}".format(self.__class__.__name__, self.__dict__)


class Manager(Person):
    def __init__(self, age, job, salary, department):
        super().__init__(age, job, salary)
        self.department = department



person1 = Person("Morty", "teacher", 10000)
manager1 = Manager("Rick", "builder", 30000, "Novaja Budova")
print(person1)
print(manager1)

