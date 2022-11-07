gas = {"Casey's" : 3.17,
       "Costco" : 3.14 }
print("12345678901234567890")
for loc in gas:
    print(f"{loc:12}{gas[loc]:6.2f}")
    #print(f"{loc:12}{gas[loc]:2.6f}")
    #print(f"{loc:>12}{gas[loc]:^6.2f}")
    #print(f"{loc:^12}{gas[loc]:6.2f}")
