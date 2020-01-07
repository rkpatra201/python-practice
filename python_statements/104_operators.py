dataList = [1, 5, 6, 3, 7]
for i in range(len(dataList)):
    print(i)

dataList = list(range(10))
print(dataList)

dataList = list(range(3, 10))
print(dataList)

dataList = list(range(3, 10, 2))
print(dataList)

for item in enumerate(dataList):
    print(item)
for k, v in enumerate(dataList):
    print(f'{k},{v}')

list1 = {1, 2}
list2 = {'a', 'b'}
list3 = {'x', 'y'}
result = zip(list1, list2, list3)  # doubt
print(result)
for item in result:
    print(item)

print('a' in 'sam')
print(1 in [1, 2, 3])
print('k1' in {'k1': 1})
print('k1' in {'k1': 1}.keys())
print('k11' in {'k1': 1}.keys())
print(1 in {'k1': 1}.values())

dataList = list(range(10))
from random import shuffle
shuffle(dataList)
print(dataList)

from random import randint
print(randint(0,100))
result = input('your age?')
print(result)
print(type(result))
print(float(result))
print(int(result))