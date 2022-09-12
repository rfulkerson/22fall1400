# Choose the correct line of code so that the following is printed:
#
#Pi to 4 places is 3.1416

places = 4
pi = 3.14159

print(f'Pi to {places} places is {pi}')
print(f'Pi to {places:d} places is {pi:f}')
print(f'Pi to {places:d} places is {pi:4f}')
print(f'Pi to {places:d} places is {pi:.4f}')

