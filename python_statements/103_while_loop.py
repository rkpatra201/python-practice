x = 1
while x < 5:
    # print('x is less than 5')
    break

while x < 5:
    x = x + 1
    print(f'x={x}')
x = 1

while x < 5:
    x = x + 1
    print(f'x={x}')
else:
    print(f'{x} is not less than 5')

# break pass continue
input_name = 'sammy'
for char in input_name:
    if char == 'a':
        break
    else:
        print(char)

for char in input_name:
    if char == 'a':
        continue
    else:
        print(char)
for char in input_name:
    pass # does nothing
print('input_name: '+input_name)
