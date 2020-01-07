# using format method and f-string
# https://pyformat.info/
print('this is a string {} {}'.format('inserted','here'))
print('this is a string {1} {0}'.format('inserted','here'))
print('this is a string {0} {0}'.format('inserted','here'))
print('this is a string {h} {i}'.format(i='inserted',h='here'))
# value:width.precision f
print(5/7)
result = 5/7
print("result {v:10.5f}".format(v=result))
name = 'john'
message = "how are you"
print(f'hello {name}, {message} ?')