def determine(inc):    
    if inc <= 9875:
        taxRate = 0.10
    elif inc <= 40125:
        taxRate = 0.12
    elif inc <= 85525:
        taxRate = 0.22


    return taxRate

#print(determine(12500))
print(determine(125000))