# Generating a receipt

item_name = input("Enter food item name: ")
item_price = float(input("Enter item price: "))
item_quant = int(input("Enter item quantity: "))
item_cost = item_price * item_quant

print("\nRECEIPT\n-------")

# using an f"" string
print(f"{item_quant} {item_name} @ ${item_price:.2f} = ${item_cost:.2f}")
