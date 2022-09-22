# You are driving a little too fast, and a police officer stops you.
# Write code to input your driving speed and if it's your birthday (y/n)
#   and determine what kind of ticket you might receive.

#   If your speed was 60 or less, the result is "no ticket". 
#   If your speed was between 61 and 80 inclusive, the result is "small ticket".
#   If your speed was 81 or more, the result is "big ticket". 

# Unless it's your birthday; on that day, your speed can be 5 higher in all
#   cases.
#
# Adapted from https://codingbat.com/prob/p195669

speed = int(input("How fast were you going? "))
bday = input("Is it your birthday (y/n)? ")

low = 60
mid = 80

if bday == "y":
    low += 5
    mid += 5

if speed <= low:
    print("You get no ticket!")
elif speed <= mid:      # assume speed >= 61
    print("You get a small ticket!")
else:
    print("You get a large ticket!")



if speed <= 60:
    print("You get no ticket!")
elif 61 <= speed <= 80:
    print("You get a small ticket!")
elif speed >= 81:
    print("You get a large ticket!")



