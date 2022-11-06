# highlights from lecture 20

# immutable
x = 10
print(x, id(x))
x = 12
print(x, id(x))

# mutable
y = [10, 20, 30]
print(y, id(y))
y[2] = 40
print(y, id(y))

# a is immutable, assuming it's an int, float, string, Boolean
def foo(a):
    a *= 2
    
g = 10
print(g)
foo(g)
print(g)

# b is mutable, assuming it's a list or dictionary
def bar(b):
    b[2] = 651
    
f = [ 1, 2, 3 ]
print(f)
bar(f)
print(f)

dont_change_me = [ 1.23, 5.78, 1882 ]
print(dont_change_me)
bar(dont_change_me[:])    # prevent mutability of the list with [:]
print(dont_change_me)


