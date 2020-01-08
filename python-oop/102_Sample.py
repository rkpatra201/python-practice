# inheritance & polymorphism
class Employee:

    def __init__(self, name):
        print('employee init')
        self.name = name

    def show_name(self):
        print('executing employee show_name')
        print(self.name)

    def display_name(self):
        # raise NotImplementedError('subclass must implement this')  really this is called abstract method in python
        print('executing employee display_name')
        print('display: ' + self.name)


class HrEmployee(Employee):  # inheritance
    def __init__(self, name):
        Employee.__init__(self, name)

    def display_name(self):
        print('calling parent method')
        super().display_name()


hr_employee = HrEmployee('sachin')
hr_employee.show_name()
hr_employee.display_name()
