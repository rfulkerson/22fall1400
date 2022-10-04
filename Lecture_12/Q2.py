# How many times would the following loop execute if the user input is 53 and 6?

top = int(input("What should I count to? "))
step = int(input("What should I count by? "))
x = 0
while x <= top:
    print(f"Look at this value: {x}")
    x += step
