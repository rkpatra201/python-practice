# check if a given word present in a given string
def func(search, str):
    return search in str


print(func('don', 'don is a good boy'))


# swap last character of string with first and append 'yes' if the given string start with alphabet

def funcswap(str):
    if str[0] in 'aeiou':
        return str[len(str) - 1] + str[1:len(str) - 1] + str[0]
    else:
        return str


print(funcswap('east'))
