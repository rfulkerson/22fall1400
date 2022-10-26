# highlights from lecture 18

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

def isEven2(x):
    return x % 2 == 0
   
def isEven3(x):
    result = False
    if x % 2 == 0:
        result = True
    return result

def isFactor(x,y):
    return x % y == 0



foo = 68
if isEven(foo):
    print("YAY")
    
if isEven(73):
    print("YAY")
    
if isEven(8812):
    print("YAY")
    
if isEven(873734):
    print("YAY")
    
    
def doit(x):
    print("Hello", x * 2)
    
def hi_there(y,a,b):
    return "what"


def doit(x):
    print("Hello", x * 2)
    
def hi_there(y,a,b):
    return "what"
    
    
doit(5)
doit("there")
doit(3.14159)
doit(False)



print(hi_there(1,2,3))

x = "Hello"
x = 12
x = 5.6
x = True
