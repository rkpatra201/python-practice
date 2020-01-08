class Employee():
    department = 'hr'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age, self.department)
        print('name is {}, age is {}'.format(self.name, self.age))


emp = Employee('rahul', 10)
print(emp.name, emp.age, emp.department)

emp.display()


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumferenece(self):
        return 2 * Circle.pi * self.radius;


circle = Circle();
print(circle.get_circumferenece())
