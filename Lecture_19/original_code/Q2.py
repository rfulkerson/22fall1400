def determine(inc):
    if 9876 <= inc <= 40125:
        taxRate = 0.12
    elif 40126 <= inc <= 85525:
        taxRate = 0.22
    elif 0 < inc <= 9875:
        taxRate = 0.10
    else:
        taxRate = 0.24
    return taxRate

#(determine(9874))
#print(determine(9876))
#print(determine(40125))
#print(determine(85525))
#print(determine(100000))
