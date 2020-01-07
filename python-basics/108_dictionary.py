data_dict = {'a': 'alska', 'b': ['bombay', 'bbsr'], 'c': {'d': 'derahdun'}}
print(data_dict)
print(data_dict['a'])
print(data_dict['c']['d'])
print(data_dict['c']['d'].upper())
data_dict['c']['d'] = 'darjeeling'
print(data_dict['c']['d'])
print(data_dict.keys())
print(data_dict.values())
print(data_dict.items())

# dictionaries not have order . but ordereddict have order.