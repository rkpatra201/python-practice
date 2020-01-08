class Sample():
    pass


sample = Sample()
print(type(sample))


class Employee():

    def __init__(self, name, age):
        self.name = name
        self.age = age


empl = Employee('rahul', 10)
print(empl.name)
print(empl.age)
