def hello_func():
    '''

    :return: string value
    '''
    return 'hello world'


message = hello_func()
print(message)

help(hello_func)

def display(name='doe'):
    print('welcome: ' + name)


display('john')
display()  # default arguments
