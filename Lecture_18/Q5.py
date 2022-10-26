import math
def temp1(a, b):
    return (math.sqrt(a) * a) + (math.sqrt(b) * b)
def temp2(a, b):
    return temp1(a, b) * 2
print(temp2(4, 4))

