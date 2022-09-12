# highlights code

phrase = "hello"

print(phrase)

ph2 = "h\ne\nl\nl\no"
print(ph2)

ph3 = "backslash: \\"
print(ph3)

print('I don\'t want to use double quotes')
print("I don't want to use double quotes")

print("She said, \"Hi there.\"")
print('She said, "Hi there."')

ph4 = "supercalifragilisticexpealidociousx"
len_ph4 = len(ph4)
print(f'{ph4} is {len_ph4} characters long.')

print(f'The first char of {ph4} is {ph4[0]}')
print(f'The last char of {ph4} is {ph4[len_ph4-1]}')

character = ph4[7]
print(character)

# can't do the following
#ph4[7] = 'x'

ph4 = "what's up?"
print(ph4)

ph5 = ph4 + " :::::: " + ph3
print(ph5)

a = 5
b = 21.12
c = "hello"

print(f'{a} ..... {b} ..... {c}')

print(f'{a:d} ..... {b:f} ..... {c:s}')

# this will fail because b is not an
print(f'{a:f} ..... {b:d} ..... {c:s}')

print(f'{a:d} ..... {b:.3f} ..... {c:s}')
print(f'{a:d} ..... {b:.0f} ..... {c:s}')


foo = 5
bar = 6.0
print(foo) # output an int
print(bar) # output a float
print(foo*bar) # implicit conversion, will be float

data = int(input("enter a number: ")) # explicit conversion of data
print(data)
print(f'{data:d}')

foobar = int(bar)
print(foobar)