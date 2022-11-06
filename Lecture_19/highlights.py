# highlights from lecture 19

def demo_one():  # demo_one has global scope
    x = 12       # local scope
    print(x)

print()
print("Calling demo_one()")
demo_one()
# this won't work because x isn't in scope
#print(x)







def demo_two():  # demo_two has global scope
    print(y)     # accessing global y

print()
print("Calling demo_two()")
y = 2112         # global scope var y
demo_two()
print(y)










def demo_three(): # demo_three has global scope
    global z
    print(z)      # accessing global z
    z = 15

print()
print("Calling demo_three()")
z = 42            # define z to have global scope
demo_three()
print(z)          # print() has built-in scope










def demo_four(): # demo_four has global scope
    a = 156      # a has local scope
    print(a)     # accessing local a, not affecting global a

print()
print("Calling demo_four()")
a = 134          # global scope
demo_four()
print(a)
