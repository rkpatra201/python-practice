# LEGB
name = 'global variable'  # global


def greet():
    name = 'shane'  # enclosing

    def hello():
        name = 'bond'  # local
        print(name)

    hello()


greet()

x = 50


def display():
    x = 25
    print(x)
    return x


print(display())
print(x)

x = 100


def show(x):
    print(f'glabl x {x}')
    x = 200
    print(f'modified locally x {x}')


show(x)
print(x)


def execute():
    global x # with gloabl use function parameter not allowed
    print(f'glabl x {x}')

    x = 200
    print(f'modified locally x {x}')


execute()
print(x)
