num_list = [1, 20, 3, 30, 7, 424]
print(num_list)
str_list = ['one', 'two', 'three']
print(str_list)
mix_list = ['one', 2, 3.2]
print(mix_list)
nested_list = [mix_list, num_list]
print(nested_list)  # nested_list

print(nested_list[0])  # index access
print(nested_list[0][1])  # 2d list index access
print(nested_list[0][1:])  # slicing
join_list = num_list + str_list
print(join_list)  # join_list
join_list[0] = '11'  # assigning to index
print(join_list)
print(num_list)

num_list.append(9)
print(num_list)
mix_list.append(num_list)
print(mix_list)

# removing items from list
print(num_list.pop())
print(num_list)
print(num_list.pop(-1))  # remove by index . -ve index
print(num_list)

# reverse & sorting
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)

str_list.sort()
print(str_list)
print(len(num_list))