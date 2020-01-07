def func1(a, b):
    print('two parameter')
    return sum((a, b))


def func2(*nums): #*args
    print(nums)
    return sum(nums)


print(func2(10, 20,30))

print(func1(10, 20))
