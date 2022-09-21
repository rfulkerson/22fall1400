# highlights from lecture 9

# Given an input year, determine and output if the year is a leap year.
# Leap years are divisible by 4 and not by 100 or are divisible by 400.

# Leap years: 2024, 2028, and 2000
# Not leap years: 2022, 1900, 1800, 2100, 2021

year = int(input("What is the year? "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is NOT a leap year!")
    


# When squirrels get together for a party, they like to have cupcakes. 
# A squirrel party is successful when the number of cupcakes is 
#   between 40 and 60, inclusive. Unless it is the weekend, in which
#   case there is no upper bound on the number of cupcakes. 
# Input the number of cupcakes and if it's the weekend (y/n) and then
#   determine if it's a successful squirrel party with appropriate output.

cupcakes = int(input("How many cupcakes? "))
weekend = input("Weekend (y/n)? ")

# Using chained operators for range testing
if 40 <= cupcakes <= 60:
    print("Successful squirrel party!")
elif 40 <= cupcakes and weekend =="y":
    print("Successful squirrel party!!")
else:
    print("Not a successful party or no party at all!")

# Using logical operators and consistent relational operators <=
if 40 <= cupcakes and cupcakes <= 60:
    print("Successful squirrel party!")
elif 40 <= cupcakes and weekend =="y":
    print("Successful squirrel party!!")
else:
    print("Not a successful party or no party at all!")

# Another way to approach it that places the importance on the variable
#   being tested even though it ends up using two different operators    
if cupcakes >= 40 and cupcakes <= 60:
    print("Successful squirrel party!")
elif cupcakes >= 40 and weekend =="y":
    print("Successful squirrel party!!")
else:
    print("Not a successful party or no party at all!")
