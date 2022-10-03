age = int(input("Enter your age (1 - 125): " ))
while age < 1 or age > 200:
    print("Invalid age! Try again!")
    age = int(input("Enter your age (1 - 125): " ))
