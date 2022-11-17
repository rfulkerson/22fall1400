prices = [6.87, 887.12, 39.99, 77.12, 21.12]
val = float(input("Enter value: "))

results = [p for p in prices if p <= val]
print(results)