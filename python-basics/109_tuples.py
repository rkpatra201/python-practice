# tuples are same as list but are immutable
item = (1, 1, "test", 3.2, {'a': 'b'})
print(item)
print(type(item))
print(item[0])
print(item[2:])
print(len(item))

print(item.index(1))
print(item.count(1))

#item[2] = 20 #'tuple' object does not support item assignment
