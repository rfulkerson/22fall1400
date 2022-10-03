# highlights from lecture 11

# Prompt the user to enter a number
# (assume it is greater than or equal to 5)
# and then output all numbers from 1 to the
# entered number, inclusive.

top = int(input("Enter top value: "))
x = 1    # loop control variable (LCV) AND it's initial value

while x <= top:   # test for the final value
    print(x)
    x += 1
    
print("Final",x)
    


# Prompt the user to enter a number
# (assume it is greater than or equal to 5)
# and then output all multiples of 5 from 1
# to the entered number, inclusive.

top = int(input("Enter top value: "))
x = 1    # loop control variable (LCV) AND it's initial value

while x <= top:   # test for the final value
    if x % 5 == 0:
        print(x)
    x += 1
    
print("Final",x)


top = int(input("Enter top value: "))
x = 5    # loop control variable (LCV) AND it's initial value

while x <= top:   # test for the final value
    print(x)
    x += 5
    
print("Final",x)

    

# Prompt the user to enter a number
# (validate that it is greater than or equal to 5 first)
# and then output all numbers from 1 to the
# entered number, inclusive.

top = int(input("Enter top value: "))

while top < 5:
    top = int(input("Enter top value: "))


x = 1    # loop control variable (LCV) AND it's initial value

while x <= top:   # test for the final value
    print(x)
    x += 1
    
print("Final",x)
