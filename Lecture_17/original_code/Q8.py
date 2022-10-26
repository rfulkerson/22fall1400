def fun1(num):
    return num + 25
def fun2(a, b):
    return fun1(a) + fun1(b)

print(fun2(10, 20))
