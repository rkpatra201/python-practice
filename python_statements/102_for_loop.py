numbers = [1, 45, 6, 7, 8, 9]
for i in numbers:
    print(i)

# even odd
for i in range(1, 10):
    if i % 2 == 0:
        print(f'even {i}')
    else:
        print(f'odd {i}')
# sum of all numbers
sum = 0
for i in numbers:
    sum += i
print(sum)

# string is character array
message = 'hello world'
for char in message:
    print(char)
# tuple iteration
tup = (1, 7, 8)
for i in tup:
    print(i)
# 2d point iteration
points = [(1, 2), (2, 3), (3, 4)]

for point in points:
    print(point)
for (a, b) in points:
    print(f'{a},{b}')

points = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for point in points:
    print(point)

for (a, b, c) in points:
    print(f'{a},{b},{c}')
keyVal = {'k1': 1, 'k2': 2}
for key, val in keyVal:
    print(f'{key},{val}')
for item in keyVal:
    print(item)
for item in keyVal.items():
    print(item)
for key, val in keyVal.items():
    print(f'{key},{val}')
for key in keyVal.keys():
    print(key)
for value in keyVal.values():
    print(value)

dataList = [1, 6, 3, 8, 9, 2, 6, 8]
max = dataList[0]
for i in dataList:
    if i > max:
        max = i
print("max value {}".format(max))
