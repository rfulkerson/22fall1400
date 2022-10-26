import math
def temp1(a, b):
    return (math.sqrt(a) * a) + (math.sqrt(b) * b)
def temp2(a, b):
    x = 0
    if temp1(a, b) - a * b >= 0:
        x = "positive"
    else:
        x = "negative"
    return x
print(temp2(9, 4))
