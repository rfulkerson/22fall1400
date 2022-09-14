# highlights from lecture 7

expr = input("Enter expression X ? Y: ")

left = float(expr[0])
oper = expr[2]
right = float(expr[4])

#print(left,oper,right)

if oper == "-":
    result = left - right
elif oper == "+":
    result = left + right
elif oper == "*":
    result = left * right
elif oper == "x":
    result = left * right
elif oper == "/":
    result = left / right
elif oper == "%":
    result = left % right
elif oper == "^":
    result = left ** right
else:
    result = "x"

if result != "x":
    print(f"{expr} = {result:.2f}")
else:
    print(f"{expr} is not supported")

