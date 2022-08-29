# code written during the highlights section of class

print("Hello world!")
print('Hello world 2!')
print("A")
print("B")
print("C")
print("D")
print("E")
print("F")

print("Hello", end=" and ")
print("World!")

print("H\ne\nl\nlo\n")
print("Should be a blank line before this!")

print("Hi","there",42)

# this is a logic error because mathematical pi isn't 3.267
pi = 3.267
radius = int(input("Please enter radius of circle:"))

area_of_circle = pi * radius * radius
print("The area of your circle is", area_of_circle)

# this is a runtime error; uncomment to see what happens!
#print(6/0)  


fave_color = input()

print("your favorite color is", fave_color)

ff = input("Enter your favorite food: ")

print("Fave food appears to be:", ff)

fn = input("Enter your favorite number: ")
print("Fave number appears to be:", fn)

other_number = int(input("Enter a number:"))
print("Fave number appears to be:", other_number)
