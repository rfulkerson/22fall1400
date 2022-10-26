# highlights from lecture 17

number = int(input("Enter a num: "))

if number % 2 == 0:
    print("It's even!")

# below is wrong; could be managed by calling function
if number % 23 == 0:
    print("It's even!")

if number % 2 == 0:
    print("It's even!")
    
if number % 2 == 0:
    print("It's even!")
    
# below is wrong; could be managed by calling function    
if number % 3 == 0:
    print("It's even!")



def isEven(x):  # call whatever is sent to me "x"
    if x % 2 == 0:
        return True
    else:
        return False

def isEven_two(x):
    result = False
    if x % 2 == 0:
        result = True
    return result
    
def isEven_three(x):
    return x % 2 == 0


num2 = int(input("Enter a num: "))
if isEven(num2):
    print("Other It's even!")

num3 = int(input("Enter a num: "))
if isEven_two(num3):
    print("Another It's even!")

num4 = int(input("Enter a num: "))
if isEven_three(num4):
    print("The last It's even!")
