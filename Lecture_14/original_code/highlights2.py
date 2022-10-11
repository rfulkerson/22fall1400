# Given a string of 25 characters representing a 5x5 word search,
# output the contents of the string in a 5x5 grid.

# For example, the string "GWORDRAEBPFLMNLULPEANEASY" would generate
# the 5x5 grid seen here:

# G    W    O    R    D    
# R    A    E    B    P    
# F    L    M    N    L    
# U    L    P    E    A    
# N    E    A    S    Y

import math

source = "GWORDRAEBPFLMNLULPEANEASY"
# uncomment the following to make a 10x10
# instead of a 5x5 because source has 100 chars
#source = "GWORDRAEBPFLMNLULPEANEASYGWORDRAEBPFLMNLULPEANEASYGWORDRAEBPFLMNLULPEANEASYGWORDRAEBPFLMNLULPEANEASY"
count = 0

length = len(source)
foo = int(math.sqrt(length))

for ch in source:
    print(ch, end=" ")
    count += 1
    if count % foo == 0:
        print()
    