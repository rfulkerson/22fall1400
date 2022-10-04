# Generate a randomized password consisting of 8 random lowercase letters.
# Modify the code to also incorporate uppercase letters.
# Modify the code to also incorporate punctuation marks.

# We'll need tools from the random library and the material from lecture 6 (strings).

import random

password = ""
source = "abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+:,.?"

x = 0

while x < 30:
    # do something
    howmany = len(source)
    which = random.randint(0,howmany-1)
    #print(source[which], end="")
    password = password + source[which]
    x += 1

print(password)