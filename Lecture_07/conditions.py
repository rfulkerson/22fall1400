# conditions

# test if a is odd

a = int(input())
if a % 2 == 1:
    print("a is an odd number")
    
if a % 2 != 0:
    print("a is an odd number")
    
    
# if e or f is even and the other is odd

e = 3
f = 4

if e % 2 != f % 2:
    print("They're even and odd!")
    
# test if g is a multiple of h
g = 18
h = 6

if g % h == 0:
    print("{} is a multiple of {}".format(g,h))
    
# i not zero

i = -3
if i != 0:
    print("i is not 0")

# is u equal to "funky"
u = input("Enter a word")
if u == 'funky':
    print("your input is funky")
    

# v equal to FuNky regardless of case

v = input("Enter your funky word")
if v == "FuNkY":
    print("you entered a variation of funky")
    
if v.casefold() == "funky":
    print("you entered a variation of funky")
    