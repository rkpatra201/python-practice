def square(num):
    return num ** 2


print(square(10))
# using map
result = map(square, [10, 20, 30])
print(result)
# print(list(result))
for i in result:
    print(i)


# using filter

def is_even(num):
    return num % 2 == 0


result = filter(is_even, list(range(10)))
print(list(result))
result = filter(lambda num: num % 2 == 0, list(range(16)))
print(list(result))
