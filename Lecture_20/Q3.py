def process(s):
    s *= 2
    return s
    
val = int(input("Number: "))
print(val)
print(process(val))
val = process(val)
print(val)
