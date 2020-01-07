message = 'welcome'
datalist = []
for char in message:
    datalist.append(char)
print(datalist)
datalist = [data for data in 'input']
print(datalist)
datalist = [x for x in range(0, 10, 3)]
print(datalist)
datalist = [x ** 2 for x in range(10) if x % 2 == 0]
print(datalist)
datalist = [x if x % 2 == 0 else 'ODD' for x in range(10)]
print(datalist)
datalist = []
for x in [1, 2, 3]:
    for y in [10, 100, 1000]:
        datalist.append(x * y)
print(datalist)

datalist = []
datalist = [x * y for x in [2, 4, 6] for y in [1, 2, 3]]
print(datalist)
str = 'welcome to india'
for x in str.split(" "):
    print(x)
datalist = [x[0] for x in str.split(" ")]
print(datalist)
datalist = [x for x in list(range(1, 10)) if x % 3 == 0]
print(datalist)
