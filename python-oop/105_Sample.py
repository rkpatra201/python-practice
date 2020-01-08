# python str, len, del methods for class

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'employee name {self.name} and age {self.age}'

    def __len__(self):
        return self.age

    def __del__(self):
        print(self)
        print('deleting one instance')


emp = Employee('rahul', 34)
print(emp)
print(str(emp))
print(len(emp))
del (emp)
